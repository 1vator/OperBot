import telebot
from telebot import types
from datetime import *
import openpyxl
import time

wb = openpyxl.reader.excel.load_workbook(filename='duty.xlsx')
wb.active = 0
sheet = wb.active

bot = telebot.TeleBot('5714164970:AAH2ZUIXLorzO5NI7_D9U1xIN7gnmU2DNc4')

# def global_def():
#     @bot.message_handler(commands=['start'])
#     def start(message):
#         bot.send_message(message.chat.id, 'Привет, напиши команду /help')
#
#     @bot.message_handler(commands=['help'])
#     def list(message):
#         bot.send_message(message.chat.id, '/list - список оперотряда\n /akt - файлик акта\n /rules - правила внутреннего ра'
#                                                   'порядка')
#     @bot.message_handler(commands=['list'])
#     def list(message):
#         photo = open('opera.jpg', 'rb')
#         bot.send_photo(message.chat.id, photo)
#
#     @bot.message_handler(commands=['akt'])
#     def akt(message):
#         document = open('akt.docx', 'rb')
#         bot.send_document(message.chat.id, document)
#
#     @bot.message_handler(commands=['rules'])
#     def rules(message):
#         document = open('rules.docx', 'rb')
#         bot.send_document(message.chat.id, document)
#
#     @bot.message_handler(commands=['duty'])
#     def duty(message):
#         bot.send_message(message.chat.id, 'Сегодня дежурит:')
#         bot.send_message(message.chat.id, sheet['A2'].value)

a = 1
b = 2
@bot.message_handler()
def reminder():
    bot.send_message(-660500640, 'Сегодня дежурит: @' + sheet['A'+str(b)].value)




while True:
    deadline1 = datetime(2022, 11, a, 10, 0, 10)
    deadline = datetime(2022, 11, a, 21, 30, 10)

    if datetime.now().day == deadline1.day and datetime.now().month == deadline1.month\
            and datetime.now().year == deadline1.year and datetime.now().hour == deadline1.hour\
            and datetime.now().minute == deadline1.minute\
            and datetime.now().second == deadline1.second:
        reminder()
        time.sleep(2)

    if datetime.now().day == deadline.day and datetime.now().month == deadline.month\
            and datetime.now().year == deadline.year and datetime.now().hour == deadline.hour\
            and datetime.now().minute == deadline.minute\
            and datetime.now().second == deadline.second:
            # and datetime.now().microsecond == deadline.microsecond:
        reminder()
        a += 1
        b += 1
        time.sleep(2)



# while True:
#     now = datetime.now()
#     deadline = datetime(2022, 9, 22, 16, 51, 1, 1)
#     if now.day == deadline.day and datetime.now().month == deadline.month and\
#             datetime.now().year == datetime.now().year and now.hour == datetime.now().hour\
#             and now.minute == datetime.now().minute and now.second == datetime.now().second\
#             and now.microsecond == datetime.now().microsecond:
#         wwhile()


bot.polling(non_stop=True)