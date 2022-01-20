import telebot
from random import choice,randint
from os import path,listdir

BOT_TOKEN = "5024135180:AAF2CHvjNOX_LKqliAMiiulZVvXO_q4xwrw"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(content_types='text')
def get_text(mes):
    #print(mes.text.split())

    ditc_title = {"природ":"природа"
                  "гор": "горы"
                  "мор": "море" 
                  "зим" "зима"
                  "лет":"лето" }

    if 'картин' in mes.text.lower():
#        for key in ditc_title.keys():
#            print(key)
        for key in ditc_title:
            if key in mes.text.lower():
                list_img = listdir(f'картинки/{ditc_title[key]}')
                print(list_img)
                with open(f'картинки/{ditc_title[key]}/{choice(list_img)}', 'rb') as img:
                    bot.send_photo(mes.chat.id, img.read(), caption=f'держи картинку на тематику {ditc_title}')

bot.polling()













