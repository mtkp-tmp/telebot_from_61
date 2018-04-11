import telebot
import config
import requests, bs4



from telebot import types

bot = telebot.TeleBot(config.token)




@bot.message_handler(commands=['start_Weather_bot'])
def hello(message):
    bot.send_message(message.chat.id,
                     'Weather_bot by @loraxinio\n'
                     'Я Бот, который расскажет вам, \n'
                     'какая погода сегодня\n'
                     'Чтобы узнать погоду\n'
                     'напишите /weather')

s=requests.get('https://sinoptik.com.ru/погода-москва')
b=bs4.BeautifulSoup(s.text, "html.parser")
p3=b.select('.temperature .p3')
pogoda1=p3[0].getText()
p4=b.select('.temperature .p4')
pogoda2=p4[0].getText()
p5=b.select('.temperature .p5')
pogoda3=p5[0].getText()
p6=b.select('.temperature .p6')
pogoda4=p6[0].getText()
p=b.select('.rSide .description')
pogoda=p[0].getText()

@bot.message_handler(commands=['weather'])
def fi(message):
    bot.send_message(message.chat.id,
                        'Утром : '+ pogoda1 + ' ' + pogoda2 + '\n'+
                        'Днём : ' + pogoda3 + ' ' + pogoda4 + '\n'+
                        pogoda)


if __name__ == '__main__':
    bot.polling(none_stop=True)