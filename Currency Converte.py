import requests

def convert_currency(amount, from_currency, to_currency):
    # Make a request to the API
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        return "Error: Unable to fetch exchange rates."

    data = response.json()

    # Check if the target currency is in the response
    if to_currency not in data["rates"]:
        return f"Error: {to_currency} is not available in exchange rates."

    # Get the exchange rate for the desired currencies
    exchange_rate = data["rates"][to_currency]

    # Calculate the converted amount
    converted_amount = round(amount * exchange_rate, 2)
    return f"{amount} {from_currency} is equal to {converted_amount} {to_currency}."

# Get user input
amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the currency to convert from (example: USD): ").upper()
to_currency = input("Enter the currency to convert to (example: EUR): ").upper()

# Print the conversion result
print(convert_currency(amount, from_currency, to_currency))
