import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb


def update_base_label(event):
    code = base_combobox.get()
    name = currencies[code]
    b_label.config(text=name)


def update_base2_label(event):
    code = base2_combobox.get()
    name = currencies[code]
    b2_label.config(text=name)


def update_target_label(event):
    code = target_combobox.get()
    name = currencies[code]
    t_label.config(text=name)


def exchange():
    target_code = target_combobox.get()
    base_code = base_combobox.get()
    base2_code = base2_combobox.get()
    if target_code and base_code and base2_code:
        try:
            result = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
            result.raise_for_status()
            result2 = requests.get(f'https://open.er-api.com/v6/latest/{base2_code}')
            result2.raise_for_status()
            data = result.json()
            data2 = result2.json()
            if target_code in data['rates'] and data2['rates']:
                exchange_rate = data['rates'][target_code]
                exchange_rate2 = data2['rates'][target_code]
                base = currencies[base_code]
                base2 = currencies[base2_code]
                target = currencies[target_code]
                mb.showinfo('Курс обмена', f'Курс {exchange_rate:.1f} {target} за 1 {base} и \n{exchange_rate2:.1f} {target} за 1 {base2}')
            else:
                mb.showerror('Ошибка', f'Валюта {target_code} не найдена')
        except Exception as e:
            mb.showerror('Ошибка', f'error 400 {e}')


currencies = {
    "USD": "Доллар США",
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

root = Tk()
root.title('Курс валют')
root.geometry('300x350+600+100')

Label(text='Базовая валюта:').pack(pady=10, padx=10)
base_combobox = ttk.Combobox(values=list(currencies.keys()))
base_combobox.pack()
base_combobox.bind('<<ComboboxSelected>>', update_base_label)

b_label = ttk.Label()
b_label.pack(pady=5, padx=10)

Label(text='Вторая базовая валюта:').pack(pady=10, padx=10)
base2_combobox = ttk.Combobox(values=list(currencies.keys()))
base2_combobox.pack()
base2_combobox.bind('<<ComboboxSelected>>', update_base2_label)

b2_label = ttk.Label()
b2_label.pack(pady=5, padx=10)

Label(text='Целевая валюта:').pack(pady=10, padx=10)
target_combobox = ttk.Combobox(values=list(currencies.keys()))
target_combobox.pack()
target_combobox.bind('<<ComboboxSelected>>', update_target_label)

t_label = ttk.Label()
t_label.pack(pady=5, padx=10)

button = ttk.Button(text='Получить курс обмена', command=exchange)
button.pack(pady=20, padx=10)

root.mainloop()