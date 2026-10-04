from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests

cryptos = {
    "BTC": {"name": "Bitcoin",  "id": "bitcoin"},
    "ETH": {"name": "Ethereum", "id": "ethereum"},
    "BNB": {"name": "BNB",      "id": "binancecoin"},
    "XRP": {"name": "XRP",      "id": "ripple"},
    "USDC": {"name": "USDC",    "id": "usd-coin"},
    "SOL": {"name": "Solana",   "id": "solana"},
    "TRX": {"name": "TRON",     "id": "tron"},
    "ZEC": {"name": "Zcash",    "id": "zcash"},
}


def update_currency_label(event):
    code = combobox.get()
    if code:
        currency_label.config(text=cryptos[code]["name"])

def exchange():
    code = combobox.get()
    name = cryptos[code]["name"]
    coin_id = cryptos[code]["id"]
    if code:
        try:
            url = (f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd")
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            if coin_id in data and "usd" in data[coin_id]:
                price = data[coin_id]["usd"]
                mb.showinfo("Курс обмена",f"1 {code} ({name}) = {price:,.2f} USD")
            else:
                mb.showerror("Ошибка", f"Валюта {code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите код валюты")


window = Tk()
window.title("Курс обмена криптовалюты к доллару")
window.geometry("400x200+760+400") # + чтобы посередине на 1920

Label(text="Выберите код валюты:").pack(padx=10, pady=10)

combobox = ttk.Combobox(values=list(cryptos.keys()))
combobox.pack(padx=10, pady=10)
combobox.bind("<<ComboboxSelected>>", update_currency_label)

currency_label = ttk.Label()
currency_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)

window.mainloop()