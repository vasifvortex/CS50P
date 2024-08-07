i=input("Camel case:")
for j in range(len(i)):
    if i[j] == i[j].capitalize():
        i=i.replace(i[j],i[j].lower())
        i=i[:j]+"_"+i[j:]
        print("Snake case: "+i)
    else:
        print("Snake case: "+i)
