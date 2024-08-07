from datetime import date
import inflect
import sys


class Birthdate:
    def __init__(self,dif_min):
        self.dif_min=dif_min


    @classmethod
    def get(cls):
        try:
            try:
                year,month,day = input("Date of Birth: ").strip().split("-")
            except ValueError:
                sys.exit("Format should be ####-##-##")
        except TypeError:
            pass
        year=int(year)
        month=int(month)
        day=int(day)
        birth=date(year, month, day)
        dif = date.today() - birth
        dif_min = int(dif.total_seconds() / 60)
        return cls(dif_min)


    def __str__(self):
        p = inflect.engine()
        return p.number_to_words(self.dif_min, andword="").capitalize()+" minutes"


def main():
    birthdate=Birthdate.get()
    print(birthdate)


if __name__=="__main__":
    main()
