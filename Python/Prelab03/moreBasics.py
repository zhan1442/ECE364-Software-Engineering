#! /usr/bin/env python3.4

def getAverage(l):
    if type(l) != list:
        return None
    if not len(l):
        return None
    return sum(l) / len(l)

def getHeadAverage(l, n):
    return sum(l, n) / n

def getTailMax(l, m):
    return max(l[-m:])

def getNumberAverage(l):
    num_sum = 0
    n = 0
    for item in l:
        if type(item) is int:
            num_sum += item
            n += 1
    return num_sum / n

def getNumberAverage(l):
    num_sum = 0
    n = 0
    for item in l:
        if type(item) is int:
            num_sum += item
            n += 1
    return num_sum / n


if __name__ == "__main__":
    a = [6, 5, 4, 3, 2, 1]
    getNumberAverage(a)
