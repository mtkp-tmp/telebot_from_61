# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "./search_bar")

import telebot
import search_bar

token = "LaLaLaLaLa"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['Start'])
def on_message(message):
  bot.send_message(message.chat.id, 'Здравствуйте! Я совместо создание группы\n'
                                     'ТМП-61 bot61 v1.0. Что я умею делать:\n'
                                     '- Находить ближайший бар')

if __name__ == "__main__":
    bot.polling(none_stop=True)

