def main():
    i=input("Enter value:")
    print(shorten(i))


def shorten(word):
    l=['a','e','i','o','u','A','E','I','O','U']
    for item in word:
        if item in l:
            word=word.replace(""+item+"","")
        else:
            pass
    return word



if __name__ == "__main__":
    main()
