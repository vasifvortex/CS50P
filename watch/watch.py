import re


def main():
    print(parse(input("HTML: ")))

def parse(s):
    if r:=re.search(r"^.+https?://(?:www\.)?youtube\.com/embed/(.+)\".+$",s):
        return "https://youtu.be/"+r.group(1)
    else:
        return None

if __name__ == "__main__":
    main()
