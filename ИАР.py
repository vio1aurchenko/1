from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests


def show_info():
    mb.showinfo('О программе', 'В списке представлены самые популярные криптовалюты на октябрь 2026г. '
                               'Для получения более подробной информации обращайтесь на сайт mexc.com')


def how_to():
    mb.showinfo('Руководство пользователя', 'Нажмите на стрелочку и выберите из списка интересующую Вас '
                                            'криптовалюту. Затем нажмите кнопку "Получить курс обмена".')


def quit_app():
    if mb.askyesno('Выход', 'Закрыть программу?'):
        window.destroy()


def update_currency_label(event):
    code = combobox.get()
    if code:
        currency_label.config(text=cryptos[code])


def exchange():
    code = combobox.get()
    if not code:
        mb.showwarning('Внимание', 'Выберите код криптовалюты')
        return
    name = cryptos[code]
    symbol = f'{code}USDT'
    try:
        url = f'https://api.mexc.com/api/v3/ticker/price?symbol={symbol}'
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        if 'price' in data:
            price = float(data['price'])
            mb.showinfo('Курс обмена', f'1 {code} ({name}) = {price:,.2f} USD')
        else:
            mb.showerror('Ошибка', f'Валюта {code} не найдена')
    except Exception as e:
        mb.showerror('Ошибка', f'Ошибка: {e}')


cryptos = {
    'BTC': 'Bitcoin',
    'ETH': 'Ethereum',
    'BNB': 'BNB',
    'XRP': 'XRP',
    'LTC': 'Litecoin',
    'SOL': 'Solana',
    'TRX': 'TRON',
    'ZEC': 'Zcash',
    'HYPE': 'Hyperliquid'
}

window = Tk()
window.title('Курс обмена криптовалюты к доллару')
window.geometry('400x200+760+400') # + чтобы посередине на 1920

Label(text='Выберите код криптовалюты:').pack(padx=10, pady=10)

combobox = ttk.Combobox(values=list(cryptos.keys()), state='readonly')
combobox.pack(padx=10, pady=10)
combobox.bind('<<ComboboxSelected>>', update_currency_label)

currency_label = ttk.Label()
currency_label.pack(padx=10, pady=10)

Button(text='Получить курс обмена', command=exchange).pack(padx=10, pady=10)

mainmenu = Menu(window)
window.config(menu=mainmenu)
infomenu = Menu(mainmenu, tearoff=0)
filemenu = Menu(mainmenu, tearoff=0)
infomenu.add_command(label='О программе', command=show_info)
infomenu.add_command(label='Руководство пользователя', command=how_to)
filemenu.add_command(label='Выход', command=quit_app)
mainmenu.add_cascade(label='Справка', menu=infomenu)
mainmenu.add_cascade(label='Файл', menu=filemenu)

window.mainloop()