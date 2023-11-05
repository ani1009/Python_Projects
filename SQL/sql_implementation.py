import sqlite3
conn = sqlite3.connect("employee.db")
print("Connection created successfully")

create_table = "create table if not exists employee(emp_id int,dept_id int,emp_name char(20),salary int)"
conn.execute(create_table)
print("Table created successfully !!")

conn.execute("insert into employee values(1,1,'Ankur',1000)")
conn.execute("insert into employee values(2,2,'Milan',2000)")
conn.execute("insert into employee values(3,2,'Rahul',3000)")
conn.execute("insert into employee values(4,3,'Pankaj',4000)")
conn.execute("insert into employee values(5,4,'Ruchika',5000)")
conn.commit()
print("Records inserted successfully !!")

#query_result = conn.execute("Select count(emp_id),dept_id from employee group by dept_id")

#query_result = conn.execute("Select max(salary),dept_id from employee group by dept_id")

query_result = conn.execute("Select * from employee order by salary desc")

for x in query_result:
    print("Emp Id : ",x[0])
    print("Dept Id : ",x[1])
    print("Employee Name: ",x[2])
    print("Salary : ",x[3])