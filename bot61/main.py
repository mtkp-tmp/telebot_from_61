# -*- coding: utf-8 -*-
import telebot

token = "LaLaLaLaLa"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['Start'])
def on_message(message):
  bot.send_message(message.chat.id, 'Здравствуйте! Я совместо создание группы\n'
                                     'ТМП-61 bot61 v0.0. Что я умею делать:\n'
                                     '-- blablabla')

if __name__ == "__main__":
    bot.polling(none_stop=True)

