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
        print(f,';',dc)
    print("Please enter your details:")
    date=input("Date(DD/MM/YY):")
    cn=input("Customer Name:")
    cph=int(input("Customer Phone.no.:"))
    print("Total Cost:Rs",tc)
    print('^'*50)
    print(' '*15,end=' ')
    print("<<<<<<<<<<THANK YOU FOR VISITING>>>>>>>>>>")
    print('^'*50)
ORDER()

            
    
        
