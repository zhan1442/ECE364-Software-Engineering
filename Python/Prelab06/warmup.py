import re

#1
string = " AA AAA "
re.search(r" A{2,5} ", string)

#2
string = "12.113 is a number, 23.34 is also a number"
re.sub(r"\d+\.\d+", "float", string)

#3
_, n = re.subn(r"\d+\.\d+", "float", string)
print(n)

#4
string = "12 -44 +33 22 22 11 -445"
s = re.findall(r"\-?\d+", string)
l = list(map(int, s))
avg = sum(l) / len(l)

#5
string = "EE364EE364"
re.sub(r"EE364", "EE461", string, count=1)

#6
string = "126.216.011.007"
x = re.match(r"(\d{1,2}|[0-1]\d{2}|2[0-4]\d|25[0-5])(\.([0-1]\d{2}|2[0-4]\d|25[0-5]|\d{1,2})){3}", string)

#7
#search for "e" in input ignore case
#match from start for (.*) is a (.*) in input
#attach the tag for two (.*) above and "is a"
#search for I(like)(you), "like" more than 9 times, "you" 1-2 times