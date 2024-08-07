import re

def main():
    print(count(input("Text: ")))


def count(s):
    s=str(s).strip().lower()
    if x:=re.search(r"^(.+)?(\?| |,|\.|)um(\?| |,|\.|)(.+)?$",s):
        if s[:2]=="um":
            return len(re.findall(r"((?:\?| |,|\.)um(?:\?| |,|\.))",s))+1
        else:
            return len(re.findall(r"((?:\?| |,|\.)um(?:\?| |,|\.))",s))

    else:
        return 0
if __name__ == "__main__":
    main()
