import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    return stock.history(period='1d', interval='15m')

def plot_stock_chart(symbol):
    data = get_stock_data(symbol)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(data.index, data['Close'])
    ax.set_xlabel('Date', color='white')
    ax.set_ylabel('Price', color='white')
    ax.set_title(f'{symbol} Stock Price Chart', color='white')
    ax.tick_params(colors='white')
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    return fig

def show_stock_chart():
    symbol = symbol_entry.get().upper()
    fig = plot_stock_chart(symbol)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=1, column=0)
    
root = tk.Tk()
root.title('Stock Price Chart')
root.configure(bg='black')

symbol_label = tk.Label(root, text='Enter Stock Symbol:', bg='black', fg='white')
symbol_label.grid(row=0, column=0)

symbol_entry = tk.Entry(root)
symbol_entry.grid(row=0, column=1)

button = tk.Button(root, text='Show Chart', command=show_stock_chart, bg='white', fg='black')
button.grid(row=0, column=2)

root.mainloop()