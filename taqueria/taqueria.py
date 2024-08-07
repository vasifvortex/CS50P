d={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
t=0
try:
    while True:
        i=input("Item: ").strip().title()
        for item in d:
            if item==i:
                t=t+d[item]
                print("Total: $%.2f" % t)
            else:
                pass
except EOFError:
    pass

