import psycopg2
conn = psycopg2.connect(
        dbname ='test_w8',
        user = 'jdm',
        password = 'test123',
        host='localhost',
        port = '5432'
    )


# try: 
    
#     cur = conn.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXIST Users ( 
#                 id SERIAL PRIMARY KEY
#                 )
#                 ;''')

#     conn.commit()
    
    
#     cur.close()
#     conn.close()
# except Exception as e: 
#     print(e)
    
    
# name = input("Enter name: ") 
try: 
    cur = conn.cursor()
    # cur.execute(f"""
    #             INSERT INTO Users (name) VALUES('{name}');
    #             """)
    
    cur.execute("""
                SELECT * From Users;
                """)
    res = cur.fetchall()
    print(res)
    conn.commit()
    cur.close()
    conn.close()
except Exception as e: 
    print(e)
    