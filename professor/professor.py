import random


def main():
    v=get_level()
    generate_integer(v)




def get_level():
    while True:
            try:
                n=int(input(""))
                if 1<=n<=3:
                    return n
                else:
                    pass
            except ValueError:
                pass




def generate_integer(level):
    count=0
    for i in range(10):
        if level==1:
            a=random.randint(0,9)
            b=random.randint(0,9)
            j=input(str(a)+" + "+str(b)+" =")
        elif level==2:
            a=random.randint(10,99)
            b=random.randint(10,99)
            j=input(str(a)+" + "+str(b)+" =")
        else:
            a=random.randint(100,999)
            b=random.randint(100,999)
            j=input(str(a)+" + "+str(b)+" =")
        i+=1
        if j == str(a+b):
            count+=1
        else:
            print("EEE")
            j=input(str(a)+" + "+str(b)+" =")
            if j == str(a+b):
                count+=1
                pass
            else:
                print("EEE")
                if j == str(a+b):
                    count+=1
                    pass
                else:
                    j=input(str(a)+" + "+str(b)+" =")
                    if j == str(a+b):
                        count+=1
                        pass
                    else:
                        print("EEE")
                        print(str(a+b))

    print(count)

if __name__ == "__main__":
    main()
