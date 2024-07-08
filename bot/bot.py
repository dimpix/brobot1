import os
import telebot
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = '7025000933:AAFMlQnEjLeUw_ABPvuEaTYtuxSIeB0gTD4'
WEBAPP_URL = os.getenv('brobot1-production.up.railway.app')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Підключити гаманець', web_app=telebot.types.WebAppInfo(url=WEBAPP_URL)))
    bot.reply_to(message, "Ласкаво просимо! Натисніть кнопку нижче, щоб підключити свій гаманець:", reply_markup=markup)

bot.polling()
