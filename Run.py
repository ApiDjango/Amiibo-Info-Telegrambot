import telebot
from telebot import types
import requests

bot = telebot.TeleBot("", parse_mode=None)
bot.remove_webhook()

@bot.message_handler(commands=['name'])
def send(message):
    msg = bot.send_message(message.chat.id, 'Please name character') 
    bot.register_next_step_handler(msg,dname)
def dname(message):
    sname = message.text
    r=requests.get('https://www.amiiboapi.com/api/amiibo/?name='+sname).text
    bot.send_message(message.chat.id, r)

if __name__ == '__main__':
    bot.infinity_polling()