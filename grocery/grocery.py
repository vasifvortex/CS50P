d = {}
try:
    while True:
        i = input().strip().title()
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
except EOFError:
    pass
d=dict(sorted(d.items()))
for item in d:
    print(f"{d[item]} {item.upper()}")
