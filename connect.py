import sqlite3
class myconnect:
      
      def __init__(self):
            #4
            self.conn = sqlite3.connect("emp1.db")
      
            #5
            try:
                 # self.conn.execute("ALTER TABLE emp1 RENAME TO emp")
                  self.conn.execute('''create table if not exists emp(name text , salary interger , emp_type char)''')
            
            except:
                  pass      
                  
      def savetodb(self,ename,eemail,emob,etype,eexp,esalary):
            #6
            self.conn.execute("insert into emp values (?,?,?)",(ename,esalary,etype))
            self.conn.commit()
            print("record Created")

      def display(self):
            #7
            name = input("Enter the emp name :")
            query = self.conn.execute("select * from emp where name=?",(name,))
            print(query.fetchall())

      
