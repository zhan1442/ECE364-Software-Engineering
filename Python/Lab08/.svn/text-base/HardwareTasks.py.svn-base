import re

def idIsAcceptable(name):
    r1 = re.compile(r'^\w+$')
    acc = r1.match(name)
    if acc is None:
        return 0
    return 1

def processSingle(ass):
    r1 = re.compile(r'^\.(\w+)\((\w+)\)$')
    acc = r1.match(ass)
    if acc is None:
        raise ValueError
    return acc.group(1), acc.group(2)

def processLine(line):
    r1 = re.compile(r'^\s*(?P<module>\w+)\s+(?P<name>\w+)\s*\('
                    r'\s*(\s*\.\w+\(\w+\)\s*,?\s*)+\s*\)$')
    r2 = re.compile(r'\.\w+\(\w+\)')
    l1 = r1.match(line)
    if l1 is None:
        raise ValueError
    ass_list = []
    port = r2.findall(line)
    for p in port:
        ass_list.append(processSingle(p))
    return l1.group("module"), l1.group("name"), tuple(ass_list)


