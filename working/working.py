import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    s=s.strip()
    try:
        if "-" in s:
            raise ValueError
    except ValueError:
        pass
    if x:=re.search(r"^((?:1[0-9]|2[0-4])?[0-9]?)(:[0-5][0-9])? (AM|PM) to ((?:1[0-9]|2[0-4])?[0-9]?)(:[0-5][0-9])? (AM|PM)$",s):
        x_1=str(x.group(1))
        x_2=str(x.group(2))
        x_4=str(x.group(4))
        x_5=str(x.group(5))
        if x.group(3) == "AM" and len(x_1)==1:
           x_1=x_1.replace("12","00")
           if x.group(6)=="AM" and len(x_4)==1:
               return ("0"+x_1 + x_2 + " to " +"0"+ x_4+ x_5).replace("None",":00")
           elif x.group(6)=="AM" and len(x_4)!=1:
               x_4=x_4.replace("12","00")
               return ("0"+x_1 + x_2 + " to " + x_4+ x_5).replace("None",":00")
           else:
               x_4=str(int(x.group(4))+12)
               x_4=x_4.replace("24","12")
               return ("0"+x_1 + x_2 + " to " + x_4+ x_5).replace("None",":00")

        elif x.group(3) == "AM" and len(x_1)!=1:
            x_1=x_1.replace("12","00")
            if x.group(6)=="AM" and len(x_4)==1:
               return (x_1 + x_2 + " to " +"0"+ x_4+ x_5).replace("None",":00")
            elif x.group(6)=="AM" and len(x_4)!=1:
               x_4=x_4.replace("12","00")
               return (x_1 + x_2 + " to " + x_4+ x_5).replace("None",":00")
            else:
               x_4=str(int(x.group(4))+12)
               x_4=x_4.replace("24","12")
               return (x_1 + x_2 + " to " + x_4+ x_5).replace("None",":00")
        else:
            x_1=str(int(x.group(1))+12)
            x_1=x_1.replace("24","12")
            if x.group(6)=="AM" and len(x_4)==1:
               return (x_1 + x_2 + " to " +"0"+ x_4+ x_5).replace("None",":00")
            elif x.group(6)=="AM" and len(x_4)!=1:
               x_4=x_4.replace("12","00")
               return (x_1 + x_2 + " to " + x_4+ x_5).replace("None",":00")
            else:
               x_4=str(int(x.group(4))+12)
               x_4=x_4.replace("24","12")
               return (x_1 + x_2 + " to " + x_4+ x_5).replace("None",":00")
    else:
        sys.exit(ValueError)

if __name__ == "__main__":
    main()
