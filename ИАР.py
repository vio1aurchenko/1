from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests


def update_currency_label(event):
    code = combobox.get()
    if code:
        currency_label.config(text=cryptos[code])


def exchange():
    code = combobox.get()
    name = cryptos[code]
    symbol = f"{code}USDT"
    if code:
        try:
            url = f"https://api.mexc.com/api/v3/ticker/price?symbol={symbol}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            if "price" in data:
                price = float(data["price"])  # Конвертируем строку в число
                mb.showinfo("Курс обмена", f"1 {code} ({name}) = {price:,.2f} USD")
            else:
                mb.showerror("Ошибка", f"Валюта {code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите код валюты")


cryptos = {
    "BTC": "Bitcoin",
    "ETH": "Ethereum",
    "BNB": "BNB",
    "XRP": "XRP",
    "LTC": "ULitecoin",
    "SOL": "Solana",
    "TRX": "TRON",
    "ZEC": "Zcash",
    "HYPE": "Hyperliquid"
}

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