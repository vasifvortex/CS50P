print("Amount Due: 50")
a=50
while True:
    i=int(input("insert a coin:"))
    if 0<a<=50:
        if a-i==0:
            print("Change Owed:",str(0))
            break
        elif a-i<0:
            if i == 5 or i == 10 or i == 25:
                print("Change Owed:",str(i-a))
                break
            else:
                print("Change Owed:",str(0))
                break
        else:
            if i == 5 or i == 10 or i == 25:
                a=a-i
                print("Amount Due:",str(a))
            else:
                print("Amount Due:",str(a))
    elif a<=0:
        if i == 5 or i == 10 or i == 25:
            print("Change Owed:",str(i-a))
            break
        else:
            print("Change Owed:",str(0))
            break
    else:
        break
