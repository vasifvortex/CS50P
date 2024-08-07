from validator_collection import checkers

def main():
    print(convert(input("Enter mail: ")))


def convert(s):
    if is_email_address := checkers.is_email(s.strip()):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
