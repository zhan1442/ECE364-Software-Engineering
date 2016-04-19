import re

with open("Part2.in", 'r') as myfile:
    content = myfile.readlines()
r1 = re.compile("purdue\.edu")
new = {}
for line in content:
    s = r1.sub("ecn.purdue.edu", line)
    print(s.strip()+"/100")
print(new)

