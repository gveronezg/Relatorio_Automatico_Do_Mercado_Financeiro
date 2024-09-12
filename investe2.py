from datetime import datetime, date
from matplotlib import pyplot as plt
import numpy as np
from bcb import sgs

# Inputs para receber dados
capital = float(input('Digite o capital investido: '))
frequencia = input('Digite a frequência do período (Y, M, D): ').upper()
inicio = input('Digite a data inicial maior do que 1995/01/01 no formato YYYY/MM/DD: ')
final = input('Digite a data inicial final no formato YYYY/MM/DD: ')

# Formatando as datas recebidas para datetime
data_inicial = datetime.strptime(inicio, '%Y/%m/%d').date()
data_final = datetime.strptime(final, '%Y/%m/%d').date()

# Pegar os dados da CELIC
taxas_selic = sgs.get({"selic":11}, start=data_inicial, end=data_final)

# Calculando o retorno no período
taxas_selic = taxas_selic/100
capital_acumulado = capital * (1 + taxas_selic['selic']).cumprod() - 1

# Mostrando o valor final de cada mês
capital_com_frequencia = capital_acumulado.resample(frequencia).last()

# Filtrar os dados da selic num período específico
data_inicial = date(2000,1,1)
data_final = date(2022,3,31)
taxas_selic = sgs.get({"selic":11}, start=data_inicial, end=data_final)/100
print(taxas_selic)

# Calcular rentabilidade das janelas de 500 dias
janelas_500_dias = ((1 + taxas_selic).rolling(window=500).apply(np.prod)-1)
print(janelas_500_dias)

# Criar range de datas na tabela
janelas_500_dias = janelas_500_dias.reset_index()
janelas_500_dias['data_inicial'] = janelas_500_dias['Date'].shift(500)

janelas_500_dias = janelas_500_dias.dropna()
janelas_500_dias.columns = ['data_final','retorno_selic_500d','data_inicial']
print(janelas_500_dias)

# Pegar o maior retorno da tabela
maior_retorno = janelas_500_dias['retorno_selic_500d'].max()
gabarito = janelas_500_dias[janelas_500_dias['retorno_selic_500d'] == maior_retorno]
print(gabarito)