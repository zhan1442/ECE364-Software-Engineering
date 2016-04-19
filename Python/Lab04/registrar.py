import glob
import os

def getstdic():
    with open('files/students.txt', 'r') as myfile:
        content = myfile.readlines()
    students_dic = {}
    for i in range(2, len(content)):
        [name, sid] = content[i].split("|")
        students_dic[name.strip()] = sid.strip()
    return students_dic

def getiddic():
    with open('files/students.txt', 'r') as myfile:
        content = myfile.readlines()
    stid_dic = {}
    for i in range(2, len(content)):
        [name, sid] = content[i].split("|")
        stid_dic[sid.strip()] = name.strip()
    return stid_dic

def getiddetail():
    files = glob.glob('files/EECS*')
    id_dic = {}
    for file in files:
        with open(file, 'r') as myfile:
            content = myfile.readlines()
        for i in range(2, len(content)):
            [stid, grade] = content[i].split()
            if stid in id_dic.keys():
                tup = (file.strip('files/txt.EECS'), int(grade))
                id_dic[stid].add(tup)
            else:
                id_dic[stid] = set()
                tup = (file.strip('files/txt.EECS'), int(grade))
                id_dic[stid].add(tup)
    return id_dic


def getDetails():
    students_dic = getstdic()
    id_dic = getiddetail()
    dic = {}
    for name in students_dic.keys():
        dic[name] = id_dic[students_dic[name]]
    return dic


def getStudentList(c):
    if not os.access("files/EECS" + c + ".txt", os.R_OK):
        return []
    stid_dic = getiddic()
    with open("files/EECS" + c + ".txt", 'r') as myfile:
        content = myfile.readlines()
    list = []
    for i in range(2, len(content)):
        stid, _ = content[i].split()
        list.append(stid_dic[stid])
    list.sort()
    return list

def searchForName(name):
    dic = getDetails()
    if name not in dic.keys():
        return {}
    return {course: float(grade) for course, grade in dic[name]}

def searchForID(stid):
    dic = getiddetail()
    if stid not in dic.keys():
        return {}
    return {course: float(grade) for course, grade in dic[stid]}

def findScore(n, c):
    students_dic = getstdic()
    if not os.access("files/EECS" + c + ".txt", os.R_OK):
        return None
    if n not in students_dic.keys():
        return None
    with open("files/EECS" + c + ".txt", 'r') as myfile:
        content = myfile.readlines()
    for i in range(2, len(content)):
        stid, grade = content[i].split()
        if students_dic[n] == stid:
            return int(grade)
    return None

def getHighest(c):
    id_dic = getiddic()
    if not os.access("files/EECS" + c + ".txt", os.R_OK):
        return ()
    with open("files/EECS" + c + ".txt", 'r') as myfile:
        content = myfile.readlines()
    f_id, f_grade = content[2].split()
    h_id = f_id
    h_grade = int(f_grade)
    for i in range(2, len(content)):
        stid, grade = content[i].split()
        if int(grade) > h_grade:
            h_id = stid
            h_grade = int(grade)
    return id_dic[h_id], h_grade


def getLowest(c):
    id_dic = getiddic()
    if not os.access("files/EECS" + c + ".txt", os.R_OK):
        return ()
    with open("files/EECS" + c + ".txt", 'r') as myfile:
        content = myfile.readlines()
    f_id, f_grade = content[2].split()
    h_id = f_id
    h_grade = int(f_grade)
    for i in range(2, len(content)):
        stid, grade = content[i].split()
        if int(grade) < h_grade:
            h_id = stid
            h_grade = int(grade)
    return id_dic[h_id], h_grade


def getAverageScore(n):
    dic = getDetails()
    if n not in dic.keys():
        return None
    tot = 0
    num = 0
    for _, grade in dic[n]:
        tot += grade
        num += 1
    return tot / num
