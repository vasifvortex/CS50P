def main():
    while True:
        try:
            i=input("Enter fraction: ")
            i=convert(i)
            print(gauge(i))
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        except IndexError:
            break

def convert(fraction):
    i=fraction.strip().split("/")
    if int(i[0]) > int(i[1]):
        pass
    else:
        fraction=round(100*int(i[0])/int(i[1]))
    return fraction


def gauge(percentage):
            if percentage<=1:
                return "E"

            elif percentage>=99:
                return "F"
            else:
                percentage=str(percentage)+"%"
                return percentage


if __name__ == "__main__":
    main()
