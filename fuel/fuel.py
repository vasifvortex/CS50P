while True:
    try:
        i=input("Enter fraction: ").strip().split("/")
        if int(i[0]) > int(i[1]):
            pass
        else:
            f=round(100*int(i[0])/int(i[1]))
            if f<=1:
                print("E")
                break
            elif f>=99:
                print("F")
                break
            else:
                f=str(f)+"%"
                print(f)
                break

    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    except IndexError:
        break

