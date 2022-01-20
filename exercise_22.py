import telebot
from random import randint as rnd, choice
from  os import path, mkdir

BOT_TOKEN = "5024135180:AAF2CHvjNOX_LKqliAMiiulZVvXO_q4xwrw"

bot = telebot.TeleBot(BOT_TOKEN)

list_stickers = []

@bot.message_handler(content_types = ['sticker'])
def get_sticker(message):
    global list_stickers
#    print(message)
#    list_stickers.append(message.sticker.file_id)
    #uniq_checker = False
    # for el in list_stickers:
    #     if el["file_unique_id"] == message.sticker.file_unique_id:
    #         uniq_checker = True
    #         break
    #
    # if not uniq_checker:
    #     list_stickers.append({'file_id' : message.sticker.file_id, 'file_unique_id' : message.sticker.file_unique_id})
    # else:
    #     bot.send_message(message.chat.id, "Стикер уже есть в хранилище")

    if path.exists("Storage_stick.txt"):
        with open('Storage_stick.txt', "r+") as file:
            uniq_checker = False
            str_1 = file.readline()
            while str_1:
                if message.sticker.file_unique_id in str_1.split()[-1]:
                    uniq_checker = True
                    break

                str_1 = file.readline()

            if uniq_checker:
                bot.send_sticker(message.chat.id, "Стикер уже есть в хранилище")
            else:
                file.write(f"\n{message.sticker.file_id} {message.sticker.file_unique_id}")
    else:
        with open('Storage of sticker is empty', "w") as file:
            file.write(f"{message.sticker.file_id} {message.sticker.file_unique_id}")
#    print(*list_stickers, sep='\n')

@bot.message_handler(content_types = ['get_stick'])
def get_command(mes):
    global list_stickers

    if mes.text == '/get_stick':
        # if list_stickers:
        #     stick = choice(list_stickers)
        #
        #     bot.send_sticker(mes.chat.id, stick)
        # else:
        #     bot.send_message(mes.chat.id, "Storage of sticker is empty")
        list_1 = []
        if path.exists("Storage_stick.txt"):
            with open("Storage_stick.txt") as file:
               list_1 =[el.split()[0] for el in file.readlines()]
               print(list_1)

        if list_1:
         bot.send_sticker(mes.chat.id, choice(list_1))
        else:
            bot.send_message(mes.chat.id, "Storage of sticker is empty")

bot.polling()

