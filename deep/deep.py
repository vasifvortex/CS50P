i=input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
i=i.strip().lower().replace("-"," ")
if i == "42" or i == "forty two":
    print("Yes")
else:
    print("No")
