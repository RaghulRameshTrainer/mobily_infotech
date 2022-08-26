import sqlite3

dbh=sqlite3.connect('mobily_infotech.db')
c=dbh.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS employee(empname TEXT, tech TEXT, exp TEXT)')
def load_data():
    #c.execute('INSERT INTO employee VALUES("Ashwin","Python",10)')
    #c.execute('INSERT INTO employee VALUES("Malini","Java",12)')
    e_name=input("Enter your name:")
    e_tech=input("Enter your technology:")
    e_exp=int(input("Enter your experience:"))
    c.execute("INSERT INTO employee VALUES(?,?,?)",(e_name,e_tech,e_exp))
    dbh.commit()

def update_data():
    c.execute("UPDATE employee SET exp=11 WHERE empname='Ashwin'")
    dbh.commit()
    c.close()
    dbh.close()
def delete_data():
    c.execute("DELETE FROM employee WHERE tech='Mainframe'")
    dbh.commit()
    c.close()
    dbh.close()
def fetch_data():
    c.execute("SELECT * FROM employee")
    '''
    fetchone
    fetchmany
    fetchall
    '''
    #print(c.fetchone())
    #print(c.fetchmany(1))
    #print(c.fetchall())
    for row in c.fetchall():
        print(row[0] + ' is working in '+row[1] + ' for past ' +row[2]+' years')
#create_table()
# for x in range(5):
#     load_data()
#update_data()
#delete_data()
fetch_data()
