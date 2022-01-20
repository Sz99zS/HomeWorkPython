import telebot
from random import randint, choice
from os import listdir, path, mkdir

bot = telebot.TeleBot("5024135180:AAF2CHvjNOX_LKqliAMiiulZVvXO_q4xwrw")

def save_photo(address, binary_data):
    with open(f"{photo_inf.file.path}", "wb") as ph:
       ph.write(binary_data)

@bot.message_handler(content_types = ['photo'])
def get_photo(message):
    # print(message.photo)
    # print(message.photo[0])
    # print(message.photo[0].file.id)

    link_photo = message.photo[-1].file.id
    photo_inf = bot.get_file(link_photo)

    download_photo = bot.download_file(bot.get_file(message.photo[-1].file.id).file_path )
    #print(download_photo)

    adr = photo_inf.file_path.split("/")[0]

    if path.exists(adr):
        save_photo(bot.get_file(message.photo[-1].file.id).file_path, download_photo)
    else:
        mkdir(adr)

        save_photo(bot.get_file(message.photo[-1].file.id).file_path, download_photo)

bot.polling()











































