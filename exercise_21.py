#dict_1 = {"key_1" : 453}

#TG bot
import telebot

BOT_TOKEN = "5024135180:AAF2CHvjNOX_LKqliAMiiulZVvXO_q4xwrw"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])

def get_command(message):
    if message.text == '/start':
        bot.send_message(chat_id = message.chat.id, text = "Привет я Ведроил e2d4!")
    elif message.text == '/help':
        bot.send_message(message.chat.id, """
1. /start - приветствие
2. /help -список доступных команд""")

@bot.message_handler(content_types=['text'])
def get_text(mes):
    spisok = "привет Привет Дороу".split()
    if set(mes.text.lower().split()) & set(spisok):
        bot.send_message(mes.chat.id, "привет попуск иди играть учись боже чел!!")
    else:
        bot.send_message(mes.chat.id, "ИИИ НЕ понимаю я глупый")
bot.polling()