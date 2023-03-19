# -*- coding: utf-8 -*-
"""Samsung AI Project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13Y-IEKtQtzqyijYtvb53yEqMiFzRDzut
"""

!pip install pyTelegramBotAPI

import telebot

import re
import random


def unknown():
    response = ['puedes decirlo de nuevo ?', 'No estoy seguro de lo que quieres']
    return response[random.randrange(2)]

def get_response(txt):
    split_message = re.split(r'\s|[,:;.?!-_]\s*f',txt.lower())
    response = check_all_message(split_message)
    return response

def message_probability(user_msn, recognized_word, single_response=False,required_word = []):
    message_certainly = 0
    has_required_word = True
    print(f'user msn {user_msn}')
    for word in user_msn:
        if word in recognized_word:
            message_certainly+=1
    percentage = float(message_certainly)/float(len(recognized_word))
    for word in required_word:
        if word not in user_msn:
            has_required_word = False
            break
    if has_required_word or single_response:
        return float(percentage * 100)
    else:
        return 0


def check_all_message(txt):
    
    highest_prob = {}    
    
    def response(bot_response,list_of_words,single_response = False,required_words = []):
        nonlocal highest_prob
        highest_prob[bot_response]= message_probability(txt,list_of_words,single_response,required_words)
    
    #llamado a funcion response
    v_response = ['estoy','muy','bien']
    
    response('Buenas, que se le ofrece?',['hola','buenos dias','buenas tardes', 'buenas noches', 'como estas', 'hay alguien ahi', 'hey', 'saludos', 'buenas'],single_response=True)
    response('Estoy bien, y tu?',['como','estas','que','tal'], required_words=['como'])
    response('¡Excelente! ¿ Que deseas ?',v_response,required_words=['estoy'])
    response('Ha sido un placer, vuelva pronto', ['chao', 'adios', 'nos vemos', 'bye', 'hasta pronto', 'hasta la proxima'], single_response=True)
    response('de nada, ha sido un gusto ayudar', ['gracias', 'muchas gracias', 'mil gracias', 'muy amable', 'se lo agradezco', 'fue de ayuda', 'gracias por la ayuda', 'muy agradecido', 'gracias por su tiempo', 'ty', 'gracias por su ayuda'], single_response=True)
    response('¿Que pasa?', ['me sucede esto', 'me pasa esto', 'pasa que esto', 'sucede que esto', 'no puedo hacer esto'], required_words=['pasa que', 'sucede que', 'me pasa', 'no puedo', 'me sucede'])

    
    best_match = max(highest_prob,key=highest_prob.get)
    print(highest_prob)
    #
    return unknown() if highest_prob[best_match] < 1 else best_match

token = "5817652216:AAHawumXMn8yQ9srQ8mR8LFXjgv1JZzEeBg"

BOT_TOKEN = token

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
  response = get_response(message.text)
  bot.reply_to(message, response)
  print(f'Mensaje para usuario BOT : {response}')
  print(f'mensaje de Usuario: {message.text}')

from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

stopWords = set(stopwords.words('spanish'))

bot.infinity_polling()