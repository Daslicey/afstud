import mysql.connector

cnx = mysql.connector.connect(user='root', database='Las', password='Welkom01', host='127.0.0.1')
cursor1 = cnx.cursor(buffered=True)
cursor2 = cnx.cursor(buffered=True)
allWeldsQuery = ("SELECT Item, Weld, WelderID, Weldingdevice FROM lasdata")
cursor1.execute(allWeldsQuery)

allWelds = cursor1.fetchall()

allWeldsList = []

for weld in allWelds:
    allWeldsList.append(weld)
allWeldsList = [i for sub in allWeldsList for i in sub]

cursor1.close()

inspectionWeldsQuery = ("SELECT Item, Weld, WelderID, Weldingdevice FROM lasdata WHERE PT>0 OR MT>0 OR UT>0 OR RT>0 OR ET>0 OR LT>0")
cursor2.execute(inspectionWeldsQuery)

inspectWelds = cursor2.fetchall()

inspectWeldlist = []

for las in inspectWelds:
    inspectWeldlist.append(las)
inspectWeldlist = [i for sub in inspectWeldlist for i in sub]

cursor2.close()

cnx.close()

print inspectWeldlist



