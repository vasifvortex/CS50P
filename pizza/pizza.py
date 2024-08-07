from sys import argv
from tabulate import tabulate
import sys
#print(tabulate([["Name","Age"],["Alice",24],["Bob",19]],
#...                headers="firstrow"))
try:
    count=0
    table=[]
    if len(argv)<2:
        sys.exit("Too few command-line arguments")
    elif len(argv)>2:
        sys.exit("Too many command-line arguments")
    else:
        if argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")
        else:
            with open(argv[1],"r") as file:
                for line in file:
                    line=line.replace("\n","").split(",")
                    table.append(line)
                headers=table[0]
                table=table[1:]
                print(tabulate(table,headers, tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")
except IndexError:
    pass
