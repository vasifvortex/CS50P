def main():
    i=input("Enter: ")
    print(shorten(i))


def shorten(word):
    l=['a','e','i','o','u','A','E','I','O','U']
    for item in l:
        word=word.replace(""+item+"","")
    return word


if __name__ == "__main__":
    main()
