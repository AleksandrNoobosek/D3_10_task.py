
import telebot

bot = telebot.TeleBot('6100430233:AAGrHvs0IgEWHF4wALM_8_GBgVFnZTbLGW8')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello, {message.from_user.first_name}{message.from_user.last_name}'
    bot.send_message(message.chat.id,mess)

@bot.message_handler(commands=['help'])

def help(message):
    mess_help = f'How i can help you? '
    bot.send_message(message.chat.id,mess_help)

bot.polling(none_stop=True)