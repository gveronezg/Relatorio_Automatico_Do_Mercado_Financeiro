import MetaTrader5 as mt5
import time

# Inicializa o metaTrade
mt5.initialize()

# Obter os simbolos disponiveis
simbolos = mt5.symbols_get()

# Selecionar o ativo escolhido
mt5.symbol_select('EGIE3')

preco_em_tempo_real = mt5.symbol_info('PETR4').last
retorno_em_tempo_real = mt5.symbol_info('PETR4').price_change

tempo = time.time() + 10

while time.time() < tempo:
    tick = mt5.symbol_info_tick('PETR4')
    print(f'O fechamento é {tick.last}')
    print(f'O valor de compra é {tick.ask}')
    print(f'O valor de venda é {tick.bid}')
    print('------------------------------')
    time.sleep(1)