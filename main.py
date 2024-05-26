'''
    HEROKU: https://www.heroku.com/
    Executar um programa em Python em uma máquina virtual.
    https://www.youtube.com/watch?v=-Wro4N9qWEQ
    https://www.youtube.com/watch?v=ZWF-WQaLorg
'''
import requests
from datetime import datetime

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

requisicao_dic = requisicao.json()
cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
cotacao_euro = requisicao_dic["EURBRL"]["bid"]
cotacao_btc = requisicao_dic["BTCBRL"]["bid"]

print(f"Cotação Atualizada. {datetime.now()}\nDólar: R${cotacao_dolar}\nEuro: R${cotacao_euro}\nBTC: R${cotacao_btc}")