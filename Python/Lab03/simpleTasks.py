def getPairwiseDifference(vec):
    for i in vec:
        if type(i) is not int:
            return None
    if vec == []:
        return None
    diff_list = []
    for ind in range(1, len(vec)):
        diff_list.append(vec[ind] - vec[ind - 1])
    return diff_list


def flatten(l):
    if type(l) is not list:
        return None
    for i in l:
        if type(i) is not list:
            return None
    flat_list = []
    for i in l:
        for j in i:
            flat_list.append(j)
    return flat_list


def partition(l, n):
    if type(l) is not list:
        return None
    if l == []:
        return None
    pa_list = []
    i = 0
    a = []
    count = 0
    while i < len(l):
        if count < n:
            a.append(l[i])
            count += 1
            i += 1
        else:
            pa_list.append(a)
            a = []
            count = 0
            continue
        if i == len(l):
            pa_list.append(a)
    return pa_list

# def partition(l, n):
    # while i+n <= len(l):
    #     a = []
    #     this_end = i + n
    #     while i < this_end:
    #         a.append(l[i])
    #         i += 1
    #     pa_list.append(a)
    # a = []
    # if i < len(l):
    #     while i < len(l):
    #         a.append(l[i])
    #         i += 1
    #     pa_list.append(a)
    # return pa_list


def rectifySignal(signal):
    if type(signal) is not list:
        return None
    if signal == []:
        return None
    for i in range(len(signal)):
        if signal[i] < 0:
            signal[i] = 0
    return signal


def getLongestWord(sentence):
    if type(sentence) is not str:
        return None
    if len(sentence.split()) <= 1:
        return None
    return max(sentence.split(), key=len)


def floatRange(a, b, s):
    if a >= b:
        return None
    float_list = []
    num = float(a)
    while num <= b:
        float_list.append(num)
        num = round(num + s, 1)
    return float_list


def decodeNumbers(numList):
    if type(numList) is not list:
        return None
    for i in numList:
        if type(i) is not int:
            return None
    c_list = []
    for c in numList:
        c_list.append(chr(c))
    return "".join(c_list)

def getCreditCard(s):
    if not len(s):
        return None
    num_list = []
    for c in s:
        if c.isdigit():
            num_list.append(int(c))
    return num_list

###
#def getCreditCard(s):
#   if not len(s):
#       return None
#   num = "0123456789"
#   card_list = []
#   for c in s:
#       if c in num:
#           card_list.append(int(c))
#   return card_list



