def mm():
    import mysql.connector as c
    mydb=c.connect(host="localhost",user="root",passwd="ankit",database="RESTAURANT")
    mycursor=mydb.cursor()
    mycursor.execute("select * from dishes")
    m=mycursor.fetchall()
    for i in m:
        print(i)
mm()
