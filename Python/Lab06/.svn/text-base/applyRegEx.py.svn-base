import re

def getRejectedUsers():
    rn1 = re.compile(r"^(?P<f>\w+) (?P<l>\w+)")
    rn2 = re.compile(r"^(?P<l>\w+), (?P<f>\w+)")
    r1 = re.compile(r"^(?P<l>\w+)\W+(?P<f>\w+)\W+\n$")
    with open("SiteRegistration.txt", 'r') as myfile:
        content = myfile.readlines()
    lst = []
    for line in content:
        l = rn1.match(line)
        if l is None:
            l = rn2.match(line)
        l2 = r1.match(line)
        if l2 is not None:
            lst.append(" ".join(l.group("f", "l")))
    lst.sort()
    return lst

def getUsersWithEmails():
    rn1 = re.compile(r"^(?P<f>\w+) (?P<l>\w+)")
    rn2 = re.compile(r"^(?P<l>\w+), (?P<f>\w+)")
    r2 = re.compile(r"[,; ]+([\w\.\-]+@[\w\.\-]+)[,; ]+")
    with open("SiteRegistration.txt", 'r') as myfile:
        content = myfile.readlines()
    dic = {}
    for line in content:
        l = rn1.match(line)
        if l is None:
            l = rn2.match(line)
        l2 = r2.search(line)
        if l2 is not None:
            dic[" ".join(l.group("f", "l"))] = l2.group(1)
    return dic

def getUsersWithPhones():
    rn1 = re.compile(r"^(?P<f>\w+) (?P<l>\w+)")
    rn2 = re.compile(r"^(?P<l>\w+), (?P<f>\w+)")
    r2 = re.compile(r"([0-9]{3})\W*([0-9]{3})\W*([0-9]{4})")
    with open("SiteRegistration.txt", 'r') as myfile:
        content = myfile.readlines()
    dic = {}
    for line in content:
        l = rn1.match(line)
        if l is None:
            l = rn2.match(line)
        l2 = r2.search(line)
        if l2 is not None:
            dic[" ".join(l.group("f", "l"))] = "("+l2.group(1)+")" + " " + l2.group(2)+"-"+l2.group(3)
    return dic

def getUsersWithStates():
    rn1 = re.compile(r"^(?P<f>\w+) (?P<l>\w+)")
    rn2 = re.compile(r"^(?P<l>\w+), (?P<f>\w+)")
    r2 = re.compile(r"\W+(?P<state>\w+ \w+|\w+)\n$")
    with open("SiteRegistration.txt", 'r') as myfile:
        content = myfile.readlines()
    dic = {}
    for line in content:
        l = rn1.match(line)
        if l is None:
            l = rn2.match(line)
        l2 = r2.search(line)
        if l2 is not None:
            dic[" ".join(l.group("f", "l"))] = l2.group("state")
    return dic

def getUsersWithoutEmails():
    rn1 = re.compile(r"^(?P<f>\w+) (?P<l>\w+)")
    rn2 = re.compile(r"^(?P<l>\w+), (?P<f>\w+)")
    r2 = re.compile(r"[,; ]+([\w\.\-]+@[\w\.\-]+)[,; ]+")
    with open("SiteRegistration.txt", 'r') as myfile:
        content = myfile.readlines()
    lst = []
    for line in content:
        l = rn1.match(line)
        if l is None:
            l = rn2.match(line)
        l2 = r2.search(line)
        if l2 is None:
            lst.append(" ".join(l.group("f", "l")))
    rejected = getRejectedUsers()
    for r in rejected:
        lst.remove(r)
    lst.sort()
    return lst

def getUsersWithoutPhones():
    rn1 = re.compile(r"^(?P<f>\w+) (?P<l>\w+)")
    rn2 = re.compile(r"^(?P<l>\w+), (?P<f>\w+)")
    r2 = re.compile(r"([0-9]{3})\W*([0-9]{3})\W*([0-9]{4})")
    with open("SiteRegistration.txt", 'r') as myfile:
        content = myfile.readlines()
    lst = []
    for line in content:
        l = rn1.match(line)
        if l is None:
            l = rn2.match(line)
        l2 = r2.search(line)
        if l2 is None:
            lst.append(" ".join(l.group("f", "l")))
    rejected = getRejectedUsers()
    for r in rejected:
        lst.remove(r)
    lst.sort()
    return lst

def getUsersWithoutStates():
    rn1 = re.compile(r"^(?P<f>\w+) (?P<l>\w+)")
    rn2 = re.compile(r"^(?P<l>\w+), (?P<f>\w+)")
    r2 = re.compile(r"\W+(?P<state>\w+ \w+|\w+)\n$")
    with open("SiteRegistration.txt", 'r') as myfile:
        content = myfile.readlines()
    lst = []
    for line in content:
        l = rn1.match(line)
        if l is None:
            l = rn2.match(line)
        l2 = r2.search(line)
        if l2 is None:
            lst.append(" ".join(l.group("f", "l")))
    rejected = getRejectedUsers()
    for r in rejected:
        lst.remove(r)
    lst.sort()
    return lst

def getUsersWithCompleteInfo():
    email_dic = getUsersWithEmails()
    phone_dic = getUsersWithPhones()
    state_dic = getUsersWithStates()
    dic = {}
    for name in email_dic.keys():
        if name in phone_dic:
            if name in state_dic:
                dic[name] = (email_dic[name], phone_dic[name], state_dic[name])
    return dic
