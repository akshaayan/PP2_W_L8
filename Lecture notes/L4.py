import L3
import psycopg2

abc = 100
print(L3.abc)
print(dir(L3))


# print(L3.test_data)

# message = 'new'

def new_f():
    message = 'new'

    def outer():
        # nonlocal message 
        message = 'local'
        
        def inner(): 
            nonlocal message
            message = "nonlocal"
            
            print("inner:",message)
        
        inner()
        print("outer:", message)
        
    outer()
    print(message)
new_f()
# print(message)

from datetime import datetime

date_string = '2023:10:30'
format_string = '%Y-%m-%d'

datetime_object = datetime.strptime(date_string, format_string)

print(datetime_object)
print(type(datetime_object))
