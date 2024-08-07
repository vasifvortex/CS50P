import sys
import requests
try:
    n=float(sys.argv[1])
    r=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    amount=float(r.json()['bpi']['USD']['rate'].replace(",",""))
    if isinstance(n, float):
        amount=amount*n
        print(f"${amount:,.4f}")
    else:
        sys.exit("Command-line argument is not a number")
except requests.RequestException:
    pass
except IndexError:
    sys.exit("Missing command-line argument  ")
