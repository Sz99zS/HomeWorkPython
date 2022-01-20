from random import randint
import telebot

BOT_TOKEN = "5024135180:AAF2CHvjNOX_LKqliAMiiulZVvXO_q4xwrw"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['Как дела','Привет', 'Как тебя зовут','Какая погода за окном','Который час','Сколько тебе дней','Что ты умеешь делать'])
def get_command(message):
    if message.text == '/Привет':
       with open("Привет.txt", "r") as file:
          list = file.readlines()
          bot.send_message(chat_id=message.chat.id, text=(list[randint(0,4)]))
          file.close()
    elif message.text == '/Как дела':
       with open("Как дела.txt", "r") as file:
          list = file.readlines()
          bot.send_message(chat_id=message.chat.id, text=(list[randint(0,4)]))
          file.close()
    elif message.text == '/Как тебя зовут':
       with open("Как тебя зовут.txt", "r") as file:
          list = file.readlines()
          bot.send_message(chat_id=message.chat.id, text=(list[randint(0,4)]))
          file.close()
    elif message.text == '/Какая погода за окном':
       with open("Какая погода за окном.txt", "r") as file:
          list = file.readlines()
          bot.send_message(chat_id=message.chat.id, text=(list[randint(0,4)]))
          file.close()
    elif message.text == '/Который час':
       with open("Который час.txt", "r") as file:
          list = file.readlines()
          bot.send_message(chat_id=message.chat.id, text=(list[randint(0,4)]))
          file.close()
    elif message.text == '/Сколько тебе дней':
       with open("Сколько тебе дней.txt", "r") as file:
          list = file.readlines()
          bot.send_message(chat_id=message.chat.id, text=(list[randint(0,4)]))
          file.close()
    elif message.text == '/Что ты умеешь делать':
       with open("Что ты умеешь делать.txt", "r") as file:
          list = file.readlines()
          bot.send_message(chat_id=message.chat.id, text=(list[randint(0,4)]))
          file.close()
    else:
        bot.send_message(chat_id=message.chat.id, text="сори")
bot.polling()




