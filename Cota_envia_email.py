import requests

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
requisicao_dic = requisicao.json()

cotacao_dolar = float(requisicao_dic["USDBRL"]["bid"])

import smtplib
import email.message
from datetime import datetime
def enviar_email(cotacao_dolar):
    data_now= datetime.now()
    data_format =  data_now.strftime("%d/%m/%Y %H:%M")
 
    corpo_email = f"""
    <p>A cotação do dolar atual é: R${cotacao_dolar} em {data_format}</p>
    """

    msg = email.message.Message()
    msg['Subject'] = f"Cotação atual do Dólar"
    msg['From'] = '2248usf@gmail.com'
    msg['To'] = 'comercial.higor@gmail.com'
    password = 'aozvgtumbrjwozsc' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


if cotacao_dolar < 5.20:
    enviar_email(cotacao_dolar)