import psycopg2
from datetime import date
import mysql.connector

config = {
    'user':'root',
    'password': 'Welkom01',
    'host': '127.0.0.1',
    'database': 'Las',
    'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)
cnx.close()


try:
    conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='Welkom01'")
except:
    print "I am unable to connect to the database";
cur = conn.cursor()

def transformdate():
    daysofweld = []
    dateofweld = []
    x = 0
    cur.execute("""SELECT dateofweld FROM welddata ORDER BY weldid ASC """)
    rows = cur.fetchall()

    for row in rows:
        dateofweld.append(row)
    dateofweld = [i for sub in dateofweld for i in sub]


    for date in dateofweld:
        delta = date.today() - dateofweld[x]
        daysofweld.append(delta.days)
        x += 1
    return daysofweld


def transformnames():
    x = 0
    weldernames = []
    cur.execute("""SELECT namewelder FROM welddata """)
    rows = cur.fetchall()

    for row in rows:
        weldernames.append(row)
    weldernames = [i for sub in weldernames for i in sub]
    print weldernames

    for name in weldernames:
        if name == 'Visser':
            weldernames[x] = 1
        elif name == 'Putkamer':
            weldernames[x] = 2
        elif name == 'van den Oever':
            weldernames[x] = 3
        elif name == 'Mostert':
            weldernames[x] = 4
        elif name == 'van der Veken':
            weldernames[x] = 5
        elif name == 'de Leng':
            weldernames[x] = 6
        elif name == 'Hameetman':
            weldernames[x] = 7
        elif name == 'van Leest':
            weldernames[x] = 8
        else:
            weldernames[x] = 9

            x += 1
    return weldernames

print transformnames()
#print transformdate()




