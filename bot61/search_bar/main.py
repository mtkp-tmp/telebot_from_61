# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "./search_bar")

import telebot
from search_bar import getNearestBar
from time import sleep
import config

bot = telebot.TeleBot(config.token)
isBars = False


@bot.message_handler(commands=['SurdumBot', 'SB', 'bars'])
def hello(message):
    bot.send_message(message.chat.id,
                     'SearchBarBot by @adabsurdumus\n' +
                     'Привет, я помогу Вам найти ближайший бар.\n' +
                     'Работаю по московским барам.\n' +
                     'Найти бар -> /findbar')


@bot.message_handler(commands=["findbar"])
def loc(message):
    global isBars
    if message.chat.type == 'private':
        keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_geo = telebot.types.KeyboardButton(text="Отправить свое местоположение", request_location=True)
        keyboard.add(button_geo)
        rep_mark = keyboard
    elif message.chat.type == 'group':
        rep_mark = ''
    bot.send_message(message.chat.id,
                     "Для определения ближайшего бара необходимо узнать Ваше местоположение.\n" +
                     "Я никому его не скажу)", reply_markup=rep_mark)
    isBars = True


@bot.message_handler(content_types=['location'])
def bar(message: telebot.types.Message):
    # чтобы бот не реагировал на просто координаты в чате
    # и не конфликтовал с другими ботами
    # используется глобальная переменная
    global isBars
    if isBars:
        bar = getNearestBar(message.location)
        bot.send_message(message.chat.id,
                         'Ближайший к Вам бар, "' + bar[0] +
                         '", находится по адресу: ' + bar[1] +
                         '.\nТелефон: ' + bar[2] +
                         '\nExperimental: \n' +
                         'Пешком напролом ' + str(bar[5]) + '-' + str(int(bar[5] * 1.5)) + ' мин')
        bot.send_location(message.chat.id, bar[3], bar[4])
        isBars = False


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(e)
            sleep(15)
