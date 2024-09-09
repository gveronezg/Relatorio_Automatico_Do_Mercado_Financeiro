import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import mplcyberpunk

tickers = ['^BVSP','^GSPC','^BRL=X']

dados_mercado = yf.download(tickers, period='6mo')

print(dados_mercado)