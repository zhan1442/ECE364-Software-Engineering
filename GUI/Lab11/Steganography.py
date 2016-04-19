import numpy
import numpy as np
from numpy import ndarray
import zlib
import base64
import re


class Payload:
    def __init__(self, img=None, compressionLevel=-1, xml=None):
        if img is None and xml is None:
            raise ValueError
        if not isinstance(compressionLevel, int) or compressionLevel < -1 or compressionLevel > 9:
            raise ValueError
        if not isinstance(img, ndarray) and not isinstance(xml, str):
            raise TypeError

        if img is not None:  # build xml by img
            # get header attributes
            payload_type, size = self.getTypeSizeS(img)  # get type, size
            #  get the serialized raw_array "array"
            if payload_type == "Gray":
                raw_array = img.flatten()
            else:
                row, col, _ = img.shape
                raw_array = img.reshape(row * col, 3).flatten('F')
            if compressionLevel != -1:
                compressed = "True"
                c_data = zlib.compress(raw_array, compressionLevel)  # compressed raw_array, implicit cast to bytes
                content = base64.b64encode(c_data)
            else:
                compressed = "False"
                content = base64.b64encode(raw_array)  # content type is bytes
            self.img = img
            self.xml = self.buildXml(payload_type, size, compressed, content)
        else:  # build img by xml
            # get the serialized raw_array "array" before compress&encode
            rs = re.search(r'type="(?P<payload_type>\w+)" size="(?P<row>[0-9]+),(?P<col>[0-9]+)" '
                           r'compressed="(?P<compressed>\w+)"', xml)
            payload_type = rs.group("payload_type")
            row = int(rs.group("row"))
            col = int(rs.group("col"))
            compressed = rs.group("compressed")
            content = xml.split("\n")[2].encode()
            if compressed == "True":
                c_data = base64.b64decode(content)
                raw_values = zlib.decompress(c_data)
            else:
                raw_values = base64.b64decode(content)
            # get original array
            if payload_type == "Gray":
                img_built = numpy.array(list(raw_values)).reshape(row, col)
            else:
                r = list(raw_values[0:row * col])
                g = list(raw_values[row * col:2 * row * col])
                b = list(raw_values[2 * row * col:])
                img_built = numpy.array([r, g, b]).transpose().reshape((row, col, 3))
            self.xml = xml
            self.img = img_built

    # To create xml
    def getTypeSizeS(self, img):  # get string representation of type and size
        if len(img.shape) == 2:
            payload_type = "Gray"
            row, col = img.shape
        else:
            payload_type = "Color"
            row, col, _ = img.shape
        size = "{},{}".format(row, col)
        return payload_type, size

    def buildXml(self, payload_type, size, compressed, content):
        xml = '<?xml version="1.0" encoding="UTF-8"?>\n' \
              '<payload type="{}" size="{}" compressed="{}">\n'.format(payload_type, size, compressed)
        xml += content.decode()
        xml += '\n</payload>'
        return xml


class Carrier:
    def __init__(self, img):
        if not isinstance(img, ndarray):
            raise TypeError
        self.img = img

    def payloadExists(self):
        if len(self.img.shape) == 2:
            bits_40 = self.img[0, 0:40].transpose().reshape(5, 8)
        else:
            bits_40 = self.img[0, 0:40, 0].transpose().reshape(5, 8)
        raw = numpy.packbits(bits_40 % 2)
        if numpy.all(raw == numpy.array([60, 63, 120, 109, 108])):
            return True
        return False

    def clean(self):
        return self.img & 254

    def embedPayload(self, payload, override=False):
        if override is False:
            if self.payloadExists():
                raise Exception
        if not isinstance(payload, Payload) or not isinstance(override, bool):
            raise TypeError
        if self.img.size < len(payload.xml) * 8:
            raise ValueError
        im = self.img
        if len(im.shape) == 2:
            rim = im.flatten()
        else:
            rim = im.reshape(int(im.size / 3), 3).flatten('F')
        i = numpy.unpackbits(numpy.fromstring(payload.xml, dtype='uint8'))
        rim[0:i.size] &= 254
        rim[0:i.size] += i
        if len(self.img.shape) == 2:
            img_built = rim.reshape(self.img.shape)
        else:
            row, col, _ = self.img.shape
            r = rim[0:row * col]
            g = rim[row * col:2 * row * col]
            b = rim[2 * row * col:]
            img_built = numpy.array([r, g, b]).transpose().reshape((row, col, 3))
        return numpy.array(img_built)

    def extractPayload(self):
        pay_array = self.img & 1
        if len(pay_array.shape) == 2:
            bi_array = pay_array.reshape(int(pay_array.size/8), 8)
        else:
            bi_array = pay_array.reshape(int(pay_array.size/3), 3).transpose().reshape(int(pay_array.size/8), 8)
        raw = numpy.packbits(bi_array)
        try:
            return Payload(xml="".join(map(chr, raw)))
        except:
            raise Exception
