from sys import argv
import sys
try:
    count=0
    if len(argv)<2:
        sys.exit("Too few command-line arguments")
    elif len(argv)>2:
        sys.exit("Too many command-line arguments")
    else:
        if argv[1][-3:] != ".py":
            sys.exit("Not a Python file")
        else:
            with open(argv[1],"r") as file:
                for line in file:
                    line=line.replace(" ","")
                    if line[0]=="#" or line.isspace():
                        pass
                    else:
                        count=count+1
except FileNotFoundError:
    sys.exit("File does not exist")
except IndexError:
    pass


print(count)


