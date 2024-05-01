from datetime import datetime, timedelta
import random
import telebot
import time
from pytz import timezone
import requests

# Defina suas chaves e IDs aqui
api_key = '6926686287:AAF1HhKmRy-iMRJNs1unsLzirZLehGHi_EE'
chat_id = '-1002065218234'
LINK_SITE = 'https://1wnurc.com/v3/fortune-tiger#vgfn'

bot = telebot.TeleBot(api_key)

def ALERT_GAME1():
    tz = timezone('America/Sao_Paulo')
    now = datetime.now(tz)
    h = now.hour
    m = now.minute
    s = now.second

    if m > 59:
        h += 1
        m = 0
    if h == 9:
        m = f'0{h}'
    if m < 9:
        m = f'0{m}'
    if s > 9:
        s = f'0{s}'

    message_id = bot.send_message(chat_id=chat_id, text=f'nova oportunidade de entrada às {h}:{m}:{s}').message_id
    return message_id

while True:
    tz = timezone('America/Sao_Paulo')
    now = datetime.now(tz)
    h = now.hour
    m = now.minute
    s = now.second

    if m > 59:
        h += 1
        m = 0
    if h == 9:
        m = f'0{h}'
    if m < 9:
        m = f'0{m}'
    if s < 9:
        s = f'0{s}'
    print(f'{h}:{m}:{s}')

    numero_aleatorio1 = random.randint(1, 10)
    numero_aleatorio2 = random.randint(1, 10)

    for i in range(1, 10):
        print(numero_aleatorio1, numero_aleatorio2)

        # Obtenha a imagem do URL
        response = requests.get('https://fortune-tiger-slot.com.br/wp-content/uploads/splash-tiger.webp')
        photo_data = response.content

        # Envie a foto com a legenda
        dados = bot.send_photo(chat_id=chat_id, photo=photo_data, caption=f'''
🐯🐯🐯 SINAL ENTREGUE 🐯🐯🐯

🔥🔥🔥 QUENTE: {numero_aleatorio1} X NORMAL

🔥🔥🔥 QUENTE: {numero_aleatorio2} X TURBO

⏳ VÁLIDO POR 4 MIN

SOMENTE NA PLATAFORMA ABAIXO 👇👇👇
👉{LINK_SITE}''', parse_mode='MARKDOWN')

        time.sleep(240)

        bot.send_message(chat_id=chat_id, text=f'''
                         
   🃏 CARTA LIBERADA 🃏
🟢 GREEEN 🟢
FAÇA SUA CONTA 👇👇👇
{LINK_SITE}                         
''', parse_mode='MARKDOWN', disable_web_page_preview=True)

        time.sleep(60)

    ALERT_GAME1()
