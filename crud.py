from pyhive import hive
import pandas as pd


def createConnection():
    con = hive.Connection(host="localhost", port=10000, database="CpuLogData")
    return con

def create_table():
    try:
        connection = createConnection()
        cur = connection.cursor()
        cur.execute("CREATE TABLE student.employee_trans (id int,name string,age int,gender string)STORED AS ORC TBLPROPERTIES ('transactional'='true')")
        print("Table Created Successfully")
    except Exception as e:
        print(e)
                

def insert_table():
    try:
        connection = createConnection()
        cur = connection.cursor()
        cur.execute("insert into student.employee_trans values(1,'James',30,'M'),(2,'Tom','M'),(3,'Harry','F')")
    except Exception as e:
        print(e)
        

def read_table():
    try:
        connection = createConnection()
        cur = connection.cursor()
        cur.execute("select * from table employee_trans")
        print(cur.fetchall())
    except Exception as e:
        print(e)


def update_table():
    try:
        connection = createConnection()
        cur = connection.cursor()
        cur.execute("update employee_trans set age=70 where id=2")
        print(cur.fetchall())
    except Exception as e:
        print(e)


def delete_table():
    try:
        connection = createConnection()
        cur = connection.cursor()
        cur.execute("delete from employee_trans where id=2")
        print(cur.fetchall())
    except Exception as e:
        print(e)


# create_table()
read_table()





# if __name__ == "__main__":

#     choice  = int(input('Enter Your Choice to Execute Program \n 1: Create Table, \n 2: Insert Table, \n 3: Read Table , \n 4: Update Table, \n 5: Delete Table -->'))
#     if choice == 1:
#         create_table()
#     elif choice == 2:
#         insert_table()
#     elif choice == 3:
#         read_table()
#     elif choice == 4:
#         update_table()
#     elif choice == 5:
#         delete_table()
#     else:
#         print('Enter Correct Option')
