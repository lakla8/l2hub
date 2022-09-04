import random as r
import telebot
import wikipedia
from telebot import types

token = "5402416687:AAHDIY373u8HDVzQ4YIsX4mpn8O2GybNNag"  # ВСТАВЬТЕ СЮДА ТОКЕН БОТА ИЗ @BOTFATHER

bot = telebot.TeleBot(token=token)

counts = {}
a = [0, 0, 0, 0]
#json read . comи

#def get_markup():
#    markup = types.ReplyKeyboardMarkup()
#    first_button = types.KeyboardButton('камень')
#    second_button = types.KeyboardButton('ножницы')
#    third_button = types.KeyboardButton('бумага')
#    res = types.KeyboardButton('рез')
#    markup.row(first_button, second_button, third_button)
#    markup.row(res)
#    return markup


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    bot.send_message(user_id, 'чтобы попасть в тгканал, пришли мне код из этого места')
    bot.send_message(user_id, 'https://ltdfoto.ru/images/2022/09/04/LEM91bquESJyf7qpg507h5S6jETijNp8ADsOVhU-vwr575_yM88XLC4p0zlajklWNHIy8dSislgivAr3AuF2awsQ--KOPIY.th.jpg')


@bot.message_handler(commands=['help'])
def pomogite(message):
    user_id = message.chat.id
    instruction = 'тебе никто не поможет'
    bot.send_message(user_id, instruction)


@bot.message_handler(content_types=['text'])
def game(message):
    user_id = message.chat.id
    ans = message.text
    print(a)
    if ans == '2efce946':
        bot.send_message(user_id, '1')
        a[0] += 1
    elif ans == '4532fb8f' and a[0] == 1:
        bot.send_message(user_id, '2')
        a[1] += 1
    elif ans == '4cb95014' and a[0] + a[1] == 2:
        bot.send_message(user_id, '3')
        a[2] += 1
    elif ans == '8ef28104' and a[0] + a[1] + a[2] == 3:
        bot.send_message(user_id, 'https://t.me/+WAnIvSWdmbk1ZTUy')
        bot.send_message('341230372', f'пользователь {user_id} прошел квест')
    else:
        pass

#'8ef28104' '4532fb8f' '4cb95014'
def results(message):
    user_id = message.chat.id
    ans = message.text
    if ans == 'рез':
        bot.send_message(user_id, f"выиграл: {counts[user_id]['v']}\nпроиграл: {counts[user_id]['l']}")
    return 0


bot.polling(none_stop=True)
