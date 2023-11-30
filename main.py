from forex_python.converter import CurrencyRates
import json
from datetime import datetime

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    exchange_rate = c.get_rate(from_currency, to_currency)
    converted_amount = amount * exchange_rate
    return converted_amount, exchange_rate

def save_conversion_history(history, filename="conversion_history.json"):
    with open(filename, 'w') as file:
        json.dump(history, file, indent=2)

def load_conversion_history(filename="conversion_history.json"):
    try:
        with open(filename, 'r') as file:
            history = json.load(file)
        return history
    except FileNotFoundError:
        return []

def main():
    amount = float(input("Entrez le montant à convertir : "))
    from_currency = input("Entrez la devise source (code ISO, par exemple USD) : ")
    to_currency = input("Entrez la devise cible (code ISO, par exemple EUR) : ")

    converted_amount, exchange_rate = convert_currency(amount, from_currency, to_currency)

    print(f"{amount} {from_currency} équivaut à {converted_amount:.2f} {to_currency} (Taux de change : {exchange_rate:.4f})")

    # Enregistrement de l'historique de conversion
    history = load_conversion_history()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conversion_info = {
        "timestamp": timestamp,
        "from_currency": from_currency,
        "to_currency": to_currency,
        "amount": amount,
        "converted_amount": converted_amount,
        "exchange_rate": exchange_rate
    }
    history.append(conversion_info)
    save_conversion_history(history)

if __name__ == "__main__":
    main()

