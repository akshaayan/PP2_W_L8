import re

hand = open('Lecture materials\mbox-short.txt')
for line in hand:
    line = line.rstrip()
    # x = re.search('', line)
    # print(x)
    if re.search('^X-\S+:', line) :
        print(line)
        
x = 'My 2a favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)

s = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
res = re.findall('\S.. [0-9].+', s)
# print(re.search('^From (.+?[0-9])', s))
print(res)

import re
hand = open("Lecture materials\mbox-short.txt")
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1 :  continue
    num = stuff[0]
    numlist.append(num)
print(type(numlist[0]))
print('Maximum:', max(numlist))


x = 'We just received \$10.00 for cookies.'
y = re.findall('\\\\\$[0-9.]+',x)
z = re.findall(r'\\', x)
print(z)


import re

s = "5-5-2021 or 05-05-2021 or 5/5/2021"
pattern = re.compile(r"\d{1,2}-\d{1,2}-\d{4}")

res = pattern.findall(s)
print(res)
# matches = re.finditer('\d{1,2}-\d{1,2}-\d{4}', s)

# for match in matches:
    # print(match)