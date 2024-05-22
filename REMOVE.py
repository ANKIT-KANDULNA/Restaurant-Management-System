def remove():
    import mysql.connector as c
    mydb=c.connect(host="localhost",user="root",passwd="ankit",database="RESTAURANT")
    mycursor=mydb.cursor()
    x=str(int(input('enter the ID you want to remove')))
    value=(x,)
    mycursor.execute("delete from DISHES where DishID=%s",value)
    mydb.commit()
remove()
