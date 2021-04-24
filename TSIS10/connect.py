import psycopg2
from getpass import GetPassWarning, getpass

db_host = "localhost"
db_user = "postgres"
db_name = "lab100"
db_pwd = getpass(prompt="Password ",stream=None)

def insert(*args):
    query = """INSERT INTO """


con = psycopg2.connect(host=db_host,database=db_name,user=db_user,password=db_pwd)
print("connected to database")
cur = con.cursor()
while True:
        inn = input("1 to create table\n2 to select table\nq to quit program\n")

        if inn=="1":
            name = input("Name of table\n")
            cur.execute(""" CREATE TABLE {} (part_id SERIAL PRIMARY KEY,part_name VARCHAR(255) NOT NULL)""".format(name))
        elif inn=="2":
            cur.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'""")
            print("select tables and write name which you want\n")
            for table in cur.fetchall():
                print(table[0])
            name = input("Name of Table\n")
            cur.execute("""SELECT * FROM {}""".format(name))
            if cur.fetchone():
                print(cur.fetchone())
            else:
                print("cannt found table\n")
        elif inn.lower()=="q":
            break 
        print('cannot connect check correctness of data') 
