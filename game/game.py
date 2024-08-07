import random
while True:
    try:
        n=int(input("Enter number:"))
        i=random.randint(1,n)
        if n>0:
            m=int(input("Guess:"))
            if m==i:
                print("Just right!")
                exit()
            elif m<i:
                print("Too small!")
            else:
                print("Too large!")
        else:
            pass
    except ValueError:
        pass
