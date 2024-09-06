import requests

API_KEY = 'fca_live_gzhtWa0oph1pnnh4dmfnPLVj0wXGTSl4g3Y4PG5z'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY"]

def convert_corrency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except Exception as e:
        print("Invalid currency")
        return None

while True:
    base = input("Enter the base currency (q foir quit): ").upper()

    if base == "Q":
        break˚

    data = convert_corrency(base)
    if not data:
        continue

    del data[base]
    for ticker, value in data.items():
         print(f"{ticker}: {value}")