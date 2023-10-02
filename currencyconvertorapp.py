import requests
import json

# Define the API endpoint
API_ENDPOINT = "https://api.exchangerate-api.com/v4/latest/USD"

# Get the exchange rates
def get_exchange_rates():
    response = requests.get(API_ENDPOINT)
    data = json.loads(response.content)
    return data["rates"]

# Convert a currency
def convert_currency(amount, from_currency, to_currency):
    exchange_rates = get_exchange_rates()
    from_currency_rate = exchange_rates[from_currency]
    to_currency_rate = exchange_rates[to_currency]
    converted_amount = amount * (to_currency_rate / from_currency_rate)
    return converted_amount

# Get the user input
amount = float(input("Enter the amount to be converted: "))
from_currency = input("Enter the source currency: ")
to_currency = input("Enter the target currency: ")

# Convert the currency
converted_amount = convert_currency(amount, from_currency, to_currency)

# Print the result
print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")