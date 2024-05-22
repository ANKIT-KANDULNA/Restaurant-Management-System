import mysql.connector as c
mydb=c.connect(host="localhost",user="root",passwd="ankit",database="RESTAURANT")
mycursor=mydb.cursor()

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

#removing values from DISHES
def remove():
    import mysql.connector as c
    mydb=c.connect(host="localhost",user="root",passwd="ankit",database="RESTAURANT")
    mycursor=mydb.cursor()
    x=str(int(input('enter the ID you want to remove:')))
    value=(x,)
    mycursor.execute("delete from DISHES where DishID=%s",value)
    mydb.commit()

#menu of the restaurant
def mm():
    import mysql.connector as c
    mydb=c.connect(host="localhost",user="root",passwd="ankit",database="RESTAURANT")
    mycursor=mydb.cursor()
    mycursor.execute("select * from dishes")
    m=mycursor.fetchall()
    print('-ID-','--NAME--','--PRICE--')
    for i in m:
        print(i)

#see the dishes
def DISHES():
    print("1.ADD    2.REMOVE    3.MAIN MENU")
    c=int(input("Enter your choice:"))
    if c==1:
        insert()
    elif c==2:
        remove()
    elif c==3:
        mm()
    else:
        print("Wrong Choice")

#name of cooks for retaurant
def COOKS():
    print("1.SANJEEV KAPOOR\n 2.VIKAS KHANNA\n 3.RANVEER BRAR\n 4.MOTHER'S SPECIAL\n 5.GORDON RAMSAY")

#placing a order
def ORDER():
    import mysql.connector as c
    mydb=c.connect(host="localhost",user="root",passwd="ankit",database="RESTAURANT")
    mycursor=mydb.cursor()
    mycursor.execute("select * from dishes")
    l=mycursor.fetchall()
    lst=[]
    while True:
        n=input("Enter DishID of which you want to order(enter 'OK' when done):")
        if n=='OK':
            break
        else:
            lst.append(n)
    print('*'*50)
    print(' '*25,end=' ')
    print("THANK YOU FOR ORDERING :)")
    print('*'*50)
    print('^'*50)
    print(' '*7,end=' ')
    print("<<<<<<<YOUR ORDER WILL BE PREPARED IN 5 MINUTES>>>>>>>")
    print('^'*50)
    s="select * from dishes"
    mycursor=mydb.cursor()
    mycursor.execute(s)
    d=mycursor.fetchall()
    dic1={}
    dic2={}
    for i in d:
        dic1[i[0]]=i[2]
    tc=0
    for i in lst:
        dc=dic1[int(i)]
        tc=tc+dc
    print("Your orders were:")
    for i in d:
        dic2[i[0]]=i[1]
    for i in lst:
        dc=dic1[int(i)]
        f=dic2[int(i)]
        print(f,':',dc)
    print("Please enter your details:")
    date=input("Date(DD/MM/YY):")
    cn=input("Customer Name:")
    cph=int(input("Customer Phone.no.:"))
    print("Total Cost:Rs",tc)
    print('^'*50)
    print(' '*15,end=' ')
    print("<<<<<<<<<<THANK YOU FOR VISITING>>>>>>>>>>")
    print('^'*50)

print('*'*50)
print(' '*13,end=' ')
print("Project:RETAURANT MANAGEMENT")
print(' '*15,end=' ')
print("WELCOME TO OUR RESTAURANT")
print('*'*50)
print("1.See the DISHES\n2. See the COOKS\n3.Place a ORDER/Take the BILL\n")
while True:
    choice=int(input("What Do You Want To Do?(1/2/3):"))
    if choice==1:
        DISHES()
    elif choice==2:
        COOKS()
    elif choice==3:
        ORDER()
    else:
        print("PLEASE VISIT AGAIN")
        break