from sys import argv
from tabulate import tabulate
import sys
import csv
#print(tabulate([["Name","Age"],["Alice",24],["Bob",19]],
#...                headers="firstrow"))
try:
    count=0
    table=[]
    if len(argv)<3:
        sys.exit("Too few command-line arguments")
    elif len(argv)>3:
        sys.exit("Too many command-line arguments")
    else:
        if argv[1][-4:] != ".csv" and argv[2][-4:] != ".csv":
            sys.exit("Not a CSV file")
        else:
            with open(argv[1],"r") as file:
                for line in file:
                    line=line.replace("\"","").strip().split(",")
                    table.append(line)
            table=table[1:]
            with open(argv[2], 'w', newline='') as csvfile:
                fieldnames = ['first','last','house']

                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for i in range(len(table)):
                    writer.writerow({fieldnames[0]: table[i][1].strip(), fieldnames[1]: table[i][0],fieldnames[2]: table[i][2]})

except FileNotFoundError:
    sys.exit(f"Could not read {argv[1]}")
except IndexError:
    pass
