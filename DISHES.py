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
DISHES()
