z= -10

print(abs(z))

def summ(a, b):
    return a+b

def mult(a, b):
    return a*b

def divv(a, b):
    try: 
        return a/b
    except:
        return None

print(any([summ(3, 5), mult(10, 3), divv(12,'str')]))

print(bin(100))

print(chr(66))

s = compile('print("Compiled message")', 'test', 'eval')
exec(s)

class Person: 
    age = 0
    name = 'Default'
p = Person()
p_t=Person()
print(p_t.age)

# delattr(p, 'age')
print(p_t.age)


print(divmod(13, 3))

test = {'new': 546, 45.12: 'a'}
res = enumerate(test)
print(res)
for i in res:
    print(i)

def filter_f(x):
    if x<=10:
        if x>4:
            return 'Positive'
    else: 
        return ''
    
res = [120, 4, 6, 6, 10, 20]

z = filter(filter_f, res)
print(list(z))
for i in z:
    print(i)
    
def map_f(x):
    if x>=10:
        return 'Not ok'
    else: 
        return 'Ok'
    
print(list(map(map_f, res)))

a = ["John", "Charles", "Mike"]
b = ["Jenny", "Christy", "New"]
c = ["12", '23', '45']
x = zip(a, b, c)

#use the tuple() function to display a readable version of the result:

res = list(x)

fhand = open(r"Lecture notes\test.txt", 'w')
fhand.write('Test Message\n')
fhand.write('Test2 Message\n')
fhand.write('Test3 Message\n')
fhand.close()
# fhand.write()
fhand2 = open(r"Lecture notes\test.txt", 'a')
fhand2.write('New append message\n')
for i in res:
    print(i)
    for j in i:
        print(j)
        fhand2.write(j+'\n')
        
fhand2.close()
fhand3 = open(r"Lecture notes\test.txt", 'r')
str = fhand3.read()
print(str[:30])

import os 
print(os.path.abspath('.'))
inp = input('Enter file name: ')
print(os.path.abspath('.') + r"\\Lecture notes\\"+ inp)
fhand4 = open(os.path.abspath('.') + r"\\Lecture notes\\"+ inp, 'x')
fhand4.write('Test message')

with open(os.path.abspath('.') + r"\\Lecture notes\\"+ inp) as file:
    x = file.readline()
    print(x)

# os.remove(r"C:\Users\aksha\OneDrive\Рабочий стол\PP2_W_L8\Lecture notes\test2.txt")

