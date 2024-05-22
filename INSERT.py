#adding values in DISHES
def insert():
    import mysql.connector as c
    mydb=c.connect(host="localhost",user="root",passwd="ankit",database="RESTAURANT")
    mycursor=mydb.cursor()
    x=str(int(input('enter DishID:')))
    y=str(input('enter DishName:'))
    z=str(int(input('enter DishPrice:')))
    valu=(x,y,z)
    mycursor.execute("insert into DISHES values(%s,%s,%s)",valu)
    mydb.commit()
insert()
