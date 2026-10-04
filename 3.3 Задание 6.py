from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests

def update_currency_label(event):
    code = combobox.get()
    name = cruptos[code]
    currency_label.config(text=name)

def exchange():
    code = combobox.get()
    if code:
        try:
            response = requests.get('https://open.er-api.com/v6/latest/USD')
            response.raise_for_status()
            data = response.json()
            if code in data['rates']:
                exchange_rate = data['rates'][code]
                currency_name = cryptos[code]
                mb.showinfo("Курс обмена", f"Курс к доллару: {exchange_rate:.1f} {currency_name} за 1 доллар")
            else:
                mb.showerror("Ошибка", f"Валюта {code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите код валюты")


cryptos = {
    "EUR": "Евро",
    "JPY": "Японская йена",
    "GBP": "Британский фунт стерлингов",
    "AUD": "Австралийский доллар",
    "CAD": "Канадский доллар",
    "CHF": "Швейцарский франк",
    "CNY": "Китайский юань",
    "RUB": "Российский рубль",
    "KZT": "Казахстанский тенге",
    "UZS": "Узбекский сум"
}

window = Tk()
window.title("Курс обмена криптовалюты к доллару")
window.geometry("360x180")
Label(text="Выберите код валюты:").pack(padx=10, pady=10)

combobox = ttk.Combobox(values=list(cryptos.keys()))
combobox.pack(padx=10, pady=10)
combobox.bind("<<ComboboxSelected>>", update_currency_label)

currency_label = ttk.Label()
currency_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)

window.mainloop()