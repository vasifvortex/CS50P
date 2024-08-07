i=input("Expression: ").split(" ")
x=int(i[0])
y=i[1]
z=int(i[2])
match y:
    case "+":
        print(float(x+z))
    case "-":
        print(float(x-z))
    case "*":
        print(float(x*z))
    case _:
        print(float(x/z))
