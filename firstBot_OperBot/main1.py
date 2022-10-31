import telebot
from telebot import types

bot = telebot.TeleBot('5714164970:AAH2ZUIXLorzO5NI7_D9U1xIN7gnmU2DNc4')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, напиши команду /help')


@bot.message_handler(commands=['help'])
def list(message):
    bot.send_message(message.chat.id, '/list - список оперотряда\n /akt - файлик акта\n /rules - правила внутреннего ра'
                                      'порядка')


@bot.message_handler(commands=['list'])
def list(message):
    photo = open('opera.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(commands=['akt'])
def akt(message):
    document = open('akt.docx', 'rb')
    bot.send_document(message.chat.id, document)


@bot.message_handler(commands=['rules'])
def rules(message):
    document = open('rules.docx', 'rb')
    bot.send_document(message.chat.id, document)


@bot.message_handler(commands=['duty'])
def duty(message):
    bot.send_message(message.chat.id, 'Сегодня дежурит:')
    bot.send_message(message.chat.id, sheet['A2'].value)


bot.polling(non_stop=True)