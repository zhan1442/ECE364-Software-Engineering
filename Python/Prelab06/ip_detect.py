import re, sys

def detect(filename):
    r1 = re.compile(r"(\d+)\.(\d+)\.(\d+)\.(\d+)")
    r2 = re.compile(r".+:(?P<port>\d+)$")
    with open(filename, 'r') as myfile:
        content = myfile.readlines()
    for line in content:
        l = r1.match(line)
        valid = 1
        if l is not None:
            for i in l.groups():
                if int(i) > 255:
                    print(line.strip() + " - Invalid IP Address")
                    valid = 0
                    break
            if valid == 1:
                port = r2.match(line)
                if port is not None:
                    if int(port.group("port")) < 1024:
                        print(line.strip() + " - Valid", end="")
                        print(" (root privileges required)")
                    elif int(port.group("port")) > 32767:
                        print(line.strip() + " - Invalid Port Number")
                    else:
                        print(line.strip() + " - Valid")
                else:
                    print(line.strip() + " - Invalid Port Number")

if __name__ == '__main__':
    detect(sys.argv[1])

