import re

str1 = "an example word: cat!"

match = re.search(r"word: \w\w\w", str1)
a = match.group()

if match:
    print('found', match.group())

print(r"\w\w\w\n\w")

print("\w\w\w\n\w")

