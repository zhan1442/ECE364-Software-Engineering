import glob
import filecmp


def getWordFrequency():
    files = glob.glob('files/*')
    return freqcount(files)

def fcmp(name1, name2):
    file1 = "files/" + name1 + ".txt"
    file2 = "files/" + name2 + ".txt"
    return filecmp.cmp(file1, file2)

def freqcount(files):
    content = []
    for file in files:
        with open(file, 'r') as myfile:
            content.extend(myfile.readlines())
    words = " ".join(content)
    word_l = words.split()
    word_list = [x.strip(",.?;:/") for x in word_l]
    dic = {}
    for word in word_list:
        if word in dic.keys():
            dic[word] += 1
        else:
            dic[word] = 1
    return dic

def unicount(group):
    files = ["files/" + name + ".txt" for name in group]
    return len(freqcount(files))

def getDuplicates():
    files = glob.glob('files/*')
    groups = []
    for file in files:
        found = False
        for group in groups:
            if fcmp(group[0], file[6:9]):
                group.append(str(file[6:9]))
                found = True
                break
        if not found:
            groups.append([str(file[6:9])])
    dic = {}
    for group in groups:
        group.sort()
        dic[group[0]] = (unicount(group), group)
    return dic

def getPurchaseReport():
    with open('purchases/Item List.txt', 'r') as myfile:
        content = myfile.readlines()
    price_dic = {}
    for i in range(2, len(content)):
        [item, price] = content[i].split()
        price_dic[item] = float(price.strip('$'))
    files = glob.glob('purchases/purchase_*')
    dic = {}
    for file in files:
        with open(file, 'r') as myfile:
            content = myfile.readlines()
        tot = 0
        for i in range(2, len(content)):
            [item, quantity] = content[i].split()
            tot += int(quantity) * price_dic[item]
        q = file.strip(".t/_xtpurchase")
        dic[int(q)] = round(tot, 2)
    return dic

def getTotalSold():
    files = glob.glob('purchases/purchase_*')
    dic = {}
    for file in files:
        with open(file, 'r') as myfile:
            content = myfile.readlines()
        for i in range(2, len(content)):
            [item, quantity] = content[i].split()
            if item in dic.keys():
                dic[item] += int(quantity)
            else:
                dic[item] = int(quantity)
    return dic