def calc_grades(d):
    res_dict = {}
    for i in d:
        grades_list = d[i]
        res = sum(grades_list)
        res_dict[i] = res
    return res_dict

test_data = {"25B010101" : [100, 30, 15, 6, 0], "25B020202":[20, 30, 70 , 18, 100]}
grades = calc_grades(test_data)
print(grades)

x = {"1" : 12, "2": 15, "3":20}
res = sum(x.values())
print(res)
# {ID : [x, c, v, v]} 
print(type("str"))

def addtwo (a, b):
    if isinstance(a, str) and isinstance(b, str):
        c = a+b
        print(c)
    else:
        print("Not suitable types")
        
addtwo(12, 'string')

def copmutepay(h, r):
    n_h = 40
    o_h = 0
    if h > n_h:
        o_h = h-n_h
        h = h - o_h
    return (o_h*r*2)+(h*r)
    
print(copmutepay(42, 15000))

def print_numbers(a, b, **kwargs):
    for i in kwargs.values():
        print(i)
        
print_numbers(1, 23, s=12, fr =1000)    

class Student:
    def __init__(self, name, id, major):
        self.name = name 
        self.id = id
        self.major = major
        
    def graduate(self):
        print("Graduated ", self.name)
    
    def sleep(self):
        print(self.name, " is sleeping! go off!")
        
class Human:
    def __init__(self, gender, age):
        self.gender = gender
        self.age = age
            
class Masterstudent(Student, Human):
    def __init__(self, name, id, major, gender, age):
        Student.__init__(self, name, id, major)
        Human.__init__(self, gender, age)
ms = Masterstudent("Bob", "25B000001", "CS", 'male', 19)
print(ms.age)