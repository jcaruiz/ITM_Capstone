
import telebot

bot = telebot.TeleBot("5531528662:AAG8f7IStNHrocbUfU1T9Fchpqc80WbFrck", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Manifesting an A for ITM")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()
