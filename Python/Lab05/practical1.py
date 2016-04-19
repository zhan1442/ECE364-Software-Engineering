import glob

def rowSumIsValid(mat):
    a = sum(mat[0])
    for line in mat:
        if sum(line) != a:
            return False
    return True

def columnSumIsValid(mat):
    col_sum = 0
    for line in mat:
        col_sum += line[0]
        l = len(line)
    for i in range(l):
        c = 0
        for line in mat:
            c += line[i]
        if c != col_sum:
            return False
    return True


def magicSquareIsValid(path):
    with open(path, 'r') as myfile:
        content = myfile.readlines()
    mat = []
    for line in content:
        s = line.strip().split()
        s = [int(a) for a in s]
        mat.append(s)
    return rowSumIsValid(mat) & columnSumIsValid(mat)

def getTotalCost(set):
    files = glob.glob('Stores/*')
    dic = {}
    for file in files:
        store_dic = {}
        with open(file, 'r') as myfile:
            content = myfile.readlines()
        for i in range(3, len(content)):
            [cpu, price] = content[i].split(",")
            cpu = cpu.strip()
            price = price.strip()
            price = float(price.strip("$"))
            store_dic[cpu] = price
        cost = 0
        for name, num in set:
            if (name in store_dic.keys()):
                cost += store_dic[name]*num
        storename = file.split("/")[1]
        storename = storename.split(".")[0]
        dic[storename] = round(cost,2)
    return dic

def getBestPrices(set):
    files = glob.glob('Stores/*')
    bestp_dic = {}
    for file in files:
        storename = file.split("/")[1]
        storename = storename.split(".")[0]
        with open(file, 'r') as myfile:
            content = myfile.readlines()
        for i in range(3, len(content)):
            [cpu, price] = content[i].split(",")
            cpu = cpu.strip()
            price = price.strip()
            price = float(price.strip("$"))
            if cpu in bestp_dic.keys():
                l_price, _ = bestp_dic[cpu]
                if price < l_price:
                    bestp_dic[cpu] = (price, storename)
            else:
                bestp_dic[cpu] = (price, storename)
    dic = {}
    for cpu in set:
        dic[cpu] = bestp_dic[cpu]
    return dic


def getMissingItems():
    files = glob.glob('Stores/*')
    c_set = set()
    for file in files:
        with open(file, 'r') as myfile:
            content = myfile.readlines()
        for i in range(3, len(content)):
            [cpu, _] = content[i].split(",")
            cpu = cpu.strip()
            if cpu not in c_set:
                c_set.update([cpu])
    files = glob.glob('Stores/*')
    m_dic = {}
    for file in files:
        storename = file.split("/")[1]
        storename = storename.split(".")[0]
        with open(file, 'r') as myfile:
            content = myfile.readlines()
        ones_set = set()
        for i in range(3, len(content)):
            [cpu, _] = content[i].split(",")
            cpu = cpu.strip()
            ones_set.update([cpu])
        m_dic[storename] = set()
        for item in c_set:
            if item not in ones_set:
                m_dic[storename].update([item])
    return m_dic