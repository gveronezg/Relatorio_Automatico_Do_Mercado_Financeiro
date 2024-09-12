import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import mplcyberpunk
import win32com.client as win32

# Definindo os ativos
tickers = ['^BVSP','^GSPC','BRL=X']

# Baixando os dados dos ativos escolhidos
dados_mercado = yf.download(tickers, period='6mo')

# Obtendo apenas uma das colunas de dados
dados_mercado = dados_mercado['Adj Close']

# Printando as primeiras 20 linhas
print(dados_mercado.head(20))

# Eliminando as linhas que possuem dados NaN
dados_mercado = dados_mercado.dropna()

# Renomeando as colunas
dados_mercado.columns = ['DOLAR','IBOVESPA','S&P500']

# Printando os dados
print(dados_mercado)

# Mudando o padrão visual dos graficos a serem desenhados
plt.style.use('cyberpunk')

for ativo in dados_mercado:
    # Desenhando o gráfico do 1º ativo
    plt.plot(dados_mercado[f'{ativo}'])
    plt.title(f'{ativo}')

    # Mostrando o gráfico
    # plt.show()

    # Salvar o grafico em PNG
    minusculo = ativo.lower()
    plt.savefig(f'{minusculo}.png')

    # Limpando o gráfico
    plt.clf()

# Calculando os retornos diários de variação
retornos_diarios = dados_mercado.pct_change()
print(retornos_diarios)

# Formatando e printando cada retorno
retorno_dolar = str(round((retornos_diarios['DOLAR'].iloc[-1]) * 100, 2)) + ' %'
print(retorno_dolar)
retorno_ibovespa = str(round((retornos_diarios['IBOVESPA'].iloc[-1]) * 100, 2)) + ' %'
print(retorno_ibovespa)
retorno_sp = str(round((retornos_diarios['S&P500'].iloc[-1]) * 100, 2)) + ' %'
print(retorno_sp)

# OBS: É possivel conectar a outros servidores de email usando a biblioteca 'smtplib'

# Abrindo o módulo de envio de email
outlook = win32.Dispatch('Outlook.Application')

# Criando o email
email = outlook.CreateItem(0)
email.To = 'gabrielveronezgiolo@gmail.com'
email.Subject = 'Relatório de Mercado'
email.Body = f'''Prezado diretor, segue o relatório de mercado:

* O Ibovespa teve o retorno de {retorno_ibovespa}
* O Dolar teve o retorno de {retorno_dolar}
* O S&P500 teve o retorno de {retorno_sp}

Segue em anexo a performance dos ativos nos últimos 6 meses.

Att,
Melhor JR da empresa
'''

# Módulo Path do pathlib para manipulação de caminhos de arquivos
from pathlib import Path
# Obtém o diretório absoluto onde o script está localizado
diretorio_atual = str(Path(__file__).parent.absolute())

anexo_ibovespa = diretorio_atual + '\ibovespa.png'
anexo_dolar = diretorio_atual + '\dolar.png'
anexo_sp = diretorio_atual + '\s&p500.png'

email.Attachments.Add(anexo_ibovespa)
email.Attachments.Add(anexo_dolar)
email.Attachments.Add(anexo_sp)

email.Send()