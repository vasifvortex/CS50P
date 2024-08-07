def main():
    i=input("What time is it? ")
    t=float(convert(i))
    if 7<=t<=8:
        print("breakfast time")
    elif 12<=t<=13:
        print("lunch time")
    elif 18<=t<=19:
        print("dinner time")
    else:
        print("")

def convert(time):
    time=time.split(":")
    h,m=int(time[0]),int(time[1])
    return h+m/60

if __name__ == "__main__":
    main()
