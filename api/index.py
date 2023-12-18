from telebot import TeleBot
from threading import Thread
import os

text1 = ""
text2 = ""
text3 = ""
text6 = ""

def bombs(number, id):
    global text1
    while True:
        with open(f"{id}.txt", "r") as file:
            text1 = file.read()
        if text1 == "Start":
            # Здесь должен быть код для обработки запуска сервисов, но он отсутствует в предоставленном фрагменте кода.
            pass

bot = TeleBot("6705628312:AAGmQ-CSIVZ9xQE-vnOkix6zOjM_mNBdhaA")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, """☁ Добро Пожаловать ☁
    Вы Находитесь В 💣 Бомбере 💣
    Тут Вы Можете Наказать Своего Обидчика И Друга
    Для Того Чтобы Узнать Больше Введите /help""")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, """★ /bomb (Номер Телефона) 
    ★ /status Посмотреть Свой Статус 
    ★ /buy Купить Премиум""")

@bot.message_handler(commands=['buy'])
def buy(message):
    bot.send_message(message.chat.id, "Напишите нам @progress135top")

@bot.message_handler(commands=['bomb'])
def bomb(message):
    global text1
    global text2
    global text3
    global text6
    text6 = os.path.abspath(f"{message.chat.id}.txt")
    with open(f"{message.chat.id}.txt", "w") as file2:
        file2.write("Start")
    text2 = message.text
    text3 = text2.split(' ')
    start = Thread(target=bombs, args=(" ".join(text3[1:2]), " ".join(text3[2:3])))  
    start.start()

@bot.message_handler(commands=['stop'])
def stop(message):
    global text6
   text6 = os.path.abspath(f"{message.chat.id}.txt")
    with open(f"{message.chat.id}.txt", "w") as file4:
        file4.write("Stop")
    bot.send_message(message.chat.id, "Атака окончена!")
            
bot.polling(none_stop=True)
