import telebot
from telebot import types
from os import listdir, path, mkdir
    from random import randint, choice

BOT_TOKEN = "5024135180:AAF2CHvjNOX_LKqliAMiiulZVvXO_q4xwrw"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands = ['get_photo'])
def get_command(message):
    if message.text == '/get_photo':
        list_photo_type = 'jpg jpeg png raw'.split()
        list_photo =[el for el in range()]
        rand_photo =

keyboard_markup_1 = types.ReplyKeyboardMarkup()

button_1 = types.KeyboardButton("Key_1 ")
keyboard_markup_1.add(button_1)

@bot.message_handler(commands = ['get_photo'])
def get_command(message):
    if message.text == '/start':
        bot.send_message(message.chat.id,
                         "LOLOLOLLCornvoer",
                         reply_markup= keyboard_markup_1)
    elif message.text == "/get_me_keyboard":
        keyboard_markup_local_2 = types.ReplyKeyboardMarkup()
@bot.message_handler(content_types = ['text'])
def get_text(message):
    if message.text == "Key_1 ":
        bot.send_message(message.chat.id
                         "Ну и зачем ты это трогаешь???")


keyboard_inline_1 = types.InlineKeyboardMarkup()
    button_inline_1 = types.InlineKeyboardButton("Knopka inline", callback_data="pressed_button_1")












bot.polling()























