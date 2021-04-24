import psycopg2
from getpass import GetPassWarning, getpass

db_host = "localhost"
db_user = "postgres"
db_name = "lab100"
db_pwd = getpass(prompt="Password ",stream=None)

def insert(columns):
    keys = []
    values = []
    for k,v in columns.items():
        keys.append(k)
        values.append(v)
    print(keys,values)
    query = """INSERT INTO """

def column_names(name):
    cur.execute("SELECT * FROM {}".format(name))
    desc = cur.description
    print(cur.fetchall())
    columns = {}
    for i in desc:
        # cur.execute("""SELECT typname FROM pg_type WHERE oid={oid}""".format(oid=i[1]))
        # print(cur.fetchone())
        value = input(i[0]+"\n")
        try:
            value = int(value)
        except:
            pass
        columns[i[0]]=value
    insert(columns)

con = psycopg2.connect(host=db_host,database=db_name,user=db_user,password=db_pwd)
print("connected to database")
cur = con.cursor()
# cur.execute("""SELECT typname,oid FROM pg_type""")
# print(cur.fetchall())
# cur.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'""")
name = input("name\n")
column_names(name)