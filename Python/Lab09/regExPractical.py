import re

def getAddress(s):
    r1 = re.compile(r'([a-fA-F0-9]{2}[:|\-]){5}[a-fA-F0-9]{2}')
    address = r1.search(s)
    if address is None:
        return None
    return address.group(0)

def getSwitches(commandline):
    r1 = re.compile(r'[\+\\](?P<switch>[a-z])\s+(?P<value>[^\+\\\s]+)')
    coms = r1.findall(commandline)
    coms.sort()
    return coms

def getElements(url):
    r1 = re.compile(r'^(http://|https://)(?P<base>[a-zA-Z0-9\.]+)/(?P<con>[a-zA-Z0-9]+)/(?P<act>[a-zA-Z0-9]+)$')
    u = r1.match(url)
    if u is not None:
        return u.group("base"),u.group("con"),u.group("act")
    else:
        return None
