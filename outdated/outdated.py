m=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
num=['0','1','2','3','4','5','6','7','8','9']
while True:

    i=input("Enter: ").strip()
    if i[0] in num:
        i=i.split("/")
        if len(i)>1:
            if int(i[1]) <= 31 and int(i[0]) <= 12:
                if len(str(i[0]))==1 and len(str(i[1]))==1:
                    print(str(i[2])+"-0"+str(i[0])+"-0"+str(i[1]))
                    break
                elif len(str(i[0]))==1 and len(str(i[1]))!=1:
                    print(str(i[2])+"-0"+str(i[0])+"-"+str(i[1]))
                    break
                elif len(str(i[0]))!=1 and len(str(i[1]))==1:
                    print(str(i[2])+"-"+str(i[0])+"-0"+str(i[1]))
                    break
                else:
                    print(str(i[2])+"-"+str(i[0])+"-"+str(i[1]))
                    break
            else:
                pass
        else:
            pass
    else:
        if "," in i:
            i=i.replace(",","").split(" ")
            if i[0] in m:
                i[0]=m.index(i[0])+1
                if int(i[1]) <= 31 and int(i[0]) <= 12:
                    if len(str(i[0]))==1 and len(str(i[1]))==1:
                        print(str(i[2])+"-0"+str(i[0])+"-0"+str(i[1]))
                        break
                    elif len(str(i[0]))==1 and len(str(i[1]))!=1:
                        print(str(i[2])+"-0"+str(i[0])+"-"+str(i[1]))
                        break
                    elif len(str(i[0]))!=1 and len(str(i[1]))==1:
                        print(str(i[2])+"-"+str(i[0])+"-0"+str(i[1]))
                        break
                    else:
                        print(str(i[2])+"-"+str(i[0])+"-"+str(i[1]))
                        break
                else:
                    pass
            else:
                pass
        else:
            pass




#11/11/3003
#9/8/1636 or September 8, 1636
#31 days
