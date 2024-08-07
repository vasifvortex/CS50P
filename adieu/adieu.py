import inflect
p = inflect.engine()
a=[]
while True:
    try:
        i=input("Name:")
        a.append(i)

    except EOFError:
        if len(a)>1:
            mylist = p.join(a)
            print("Adieu, adieu, to", mylist)
            exit()
        else:
            print("Adieu, adieu, to", a[0])
            exit()
