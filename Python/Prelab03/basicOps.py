#! /usr/bin/env python3.4

def addNumbers(num):
    sum_num = 0
    for value in range(1, num+1):
        sum_num += value
    return sum_num
    #return (num+1)*num/2

def addMultiplesOf(num):
    num_list = range(0, 1001, num)
    sum_mul = sum(num_list)
    return sum_mul

def getNumberFrequency(num):
    string = "The value of Pi is 3 . 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 2 6 4 3 3 8 3 2 7 9 5 0 2 8 8 4 1 9 7 1 6 9 3 9 9 3 7 5 1 0 5 8 2 0 9 7 4 9 4 4 5 9 2 3 0 7 8 1 6 4 0 6 2 8 6 2 0 8 9 9 8 6 2 8 0 3 4 8 2 5 3 4 2 1 1 7 0 6 7 9 8 2 1 4 8 0 8 6 5 1 3 2 8 2 3 0 6 6 4 7 0 9 3 8 4 4 6 0 9 5 5 0 5 8 2 2 3 1 7 2 5 3 5 9 4 0 8 1 2 8 4 8 1"
    char_list = string.split()
    count = 0
    for ch in char_list:
        if ch == str(num):
            count += 1
    return count
    #return string.count(str(num))

def getDigitalSum(num_str):
    num_sum = 0
    for num in list(num_str):  # for i in num_str
        num_sum += int(num)
    return num_sum


def getSequenceWithoutDigit(num):
    strList = ["736925233695599303035509581762617623184956190649483967300203776387436934399982",
               "943020914707361894793269276244518656023955905370512897816345542332011497599489",
               "627842432748378803270141867695262118097500640514975588965029300486760520801049",
               "153788541390942453169171998762894127722112946456829486028149318156024967788794",
               "981377721622935943781100444806079767242927624951078415344642915084276452000204",
               "276947069804177583220909702029165734725158290463091035903784297757265172087724",
               "474095226716630600546971638794317119687348468873818665675127929857501636341131"]
    wholestr = "".join(strList)
    return max(wholestr.split(str(num)), key=len)

def capitalizeMe(string):
    str_list = string.split()
    capped_list = []
    for s in str_list:
        if len(s) == 1:
            capped_list.append(s.upper())
        else:
            capped_list.append(s[0].upper() + s[1:-1] + s[-1].upper())
    return " ".join(capped_list)
