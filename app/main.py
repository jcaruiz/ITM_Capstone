from flask import Flask, jsonify, request
import telebot as tb
import datetime
import requests

app = Flask(__name__)
bot = tb.TeleBot('5482676415:AAGzr5b6d2vfP7XnxK6Iz3YGD156chTVHjI')
SendChannel = '@itmgt25MariTestBot'
token = '5482676415:AAGzr5b6d2vfP7XnxK6Iz3YGD156chTVHjI'

# send message
def sendMessage(message, text):
   bot.send_message(message.chat.id, text)

# start
@bot.message_handler(commands=['start'])
def send_info(message):
   text = (
   "<b>Welcome to the MariTest Bot 🤖!</b>\n"
   "What can I do for you?\n"
   "\n"
   "Here's my list of commands: \n"
   "<b>/products</b> to check the products we sell\n"
   "<b>/prices</b> to check the prices of our products\n"
   "<b>/pay</b> to check our available payment methods\n"
   "<b>/feedback</b> to give us feedback on your experience\n"
   "<b>/rate</b> to rate your experience with us\n"
   "<b>/ratings</b> to check the rating of our business\n"
   "<b>/reviews</b> to check other customers' reviews of our business\n"
   "<b>/customers</b> to check how many customers we've served\n"
   "<b>/completed</b> to complete a transaction\n"
   "<b>/help</b> to access our command list"
   )
   bot.send_message(message.chat.id, text, parse_mode='HTML')

# products
@bot.message_handler(commands=['products'])
def send_info(message):
   text = (
   "Thank you for your interest in our shop!\n"
   "Our products include:\n"
   "- T-shirt\n"
   "- Bucket Hat\n"
   "- Tote Bag\n"
   "\n"
   "To see our price list please use the <b>/prices</b> command"
   )
   bot.send_message(message.chat.id, text, parse_mode='HTML')

# prices
@bot.message_handler(commands=['prices'])
def send_info(message):
   text = (
   "Thank you for your interest in our shop!\n"
   "Here's our price list:\n"
   "T-shirt - 300\n"
   "Bucket Hat - 250\n"
   "Tote Bag - 180\n"
   "Standard Shipping Fee - 100\n"
   "\n"
   "To see our payment options please use the <b>/pay</b> command"
    )
   bot.send_message(message.chat.id, text, parse_mode='HTML')

# help
@bot.message_handler(commands=['help'])
def send_info(message):
   text = (
   "<b>Welcome to the MariTest Bot 🤖!</b>\n"
   "How can I help you?\n"
   "\n"
   "Here's my list of commands: \n"
   "<b>/start</b> to start chatting the bot\n"
   "<b>/products</b> to check the products we sell\n"
   "<b>/prices</b> to check the prices of our products\n"
   "<b>/pay</b> to check our available payment methods\n"
   "<b>/feedback</b> to give us feedback on your experience\n"
   "<b>/rate</b> to rate your experience with us\n"
   "<b>/ratings</b> to check the rating of our business\n"
   "<b>/reviews</b> to check other customers' reviews of our business\n"
   "<b>/customers</b> to check how many customers we've served\n"
   "<b>/completed</b> to complete a transaction\n"
   "<b>/help</b> to access our command list"
   )
   bot.send_message(message.chat.id, text, parse_mode='HTML')

# feedback
@bot.message_handler(commands =['feedback'])
def send_info(message):
   text = (
   "Thank you for your interest in giving feedback!\n"
   "Please type in your feed back and don't forget to mention me, <b>@maritest2_bot</b>! \n"
   "You may attach an image of your order as proof." 
   )
   bot.send_message(message.chat.id, text, parse_mode='HTML')   

# forward image
@bot.message_handler(content_types=['photo'])
def handle_text_doc(message):
    bot.forward_message(SendChannel, message.chat.id, message.message_id)


# to see others' reviews
@bot.message_handler(commands =['reviews'])
def send_info(message):
   text = (
   "ITM Bot is the small business you can trust!\n"
   "Check our channel for reviews from other customers: <b>@itmgt25MariTestBot</b>"
   )
   bot.send_message(message.chat.id, text, parse_mode='HTML') 

# give feedback
@bot.message_handler(regexp="@maritest2_bot")        
def repeat_messages(message): 
    bot.forward_message(SendChannel, message.chat.id, message.message_id)

# pay
@bot.message_handler(commands =['pay'])
def send_info(message):
   text = (
   "Our payment options include:\n"
   "- GCash\n"
   "- BPI Online Banking\n"
   "How would you like to pay?"
   )
   bot.send_message(message.chat.id, text, parse_mode='HTML')  

# pay with gcash
@bot.message_handler(regexp="GCASH")
def replyCash(message):
    text = (
    "Chosen payment method: Gcash\n"
    "\n"
    "Our Gcash payment details are:\n"
    "Name: ITM Bot\n"
    "Number: 09876543210"
    )
    bot.send_message(message.chat.id, text, parse_mode = 'HTML')

# pay with bpi
@bot.message_handler(regexp="BPI Online Banking")
def replyCash(message):
    text = (
    "Chosen payment method: BPI Online Banking\n"
    "\n"
    "Our BPI Online Banking payment details are:\n"
    "Name: ITM Bot\n"
    "Number: 012345678910"
    )
    bot.send_message(message.chat.id, text, parse_mode = 'HTML')

ratingsList = [4]

# rate 
@bot.message_handler(commands =['rate'])
def ratings(message):
    text = (
    "Give us a rating out of 5!"
    )
    bot.send_message(message.chat.id, text, parse_mode = 'HTML')

@bot.message_handler(regexp="0")
def replyCash(message):
    givenRating = (message.text)
    ratingsList.append(int(givenRating))
    text = ("Thank you for your rating of {}⭐️ out of 5⭐️!").format(givenRating)
    var1 = len(ratingsList)
    var2 = sum(ratingsList)
    ratingsvalue = (var2/var1)
    text2 = ("{} customers have rated us!\n \nRating: {}⭐️ out of 5.0⭐️").format(var1, ratingsvalue)
    bot.send_message(message.chat.id, text, parse_mode = 'HTML')
    bot.send_message(SendChannel, text2, parse_mode = 'HTML')

@bot.message_handler(regexp="1")
def replyCash(message):
    givenRating = (message.text)
    ratingsList.append(int(givenRating))
    text = ("Thank you for your rating of {}⭐️ out of 5⭐️!").format(givenRating)
    var1 = len(ratingsList)
    var2 = sum(ratingsList)
    ratingsvalue = (var2/var1)
    text2 = ("{} customers have rated us!\n \nRating: {}⭐️ out of 5.0⭐️").format(var1, ratingsvalue)
    bot.send_message(message.chat.id, text, parse_mode = 'HTML')
    bot.send_message(SendChannel, text2, parse_mode = 'HTML')

@bot.message_handler(regexp="2")
def replyCash(message):
    givenRating = (message.text)
    ratingsList.append(int(givenRating))
    text = ("Thank you for your rating of {}⭐️ out of 5⭐️!").format(givenRating)
    var1 = len(ratingsList)
    var2 = sum(ratingsList)
    ratingsvalue = (var2/var1)
    text2 = ("{} customers have rated us!\n \nRating: {}⭐️ out of 5.0⭐️").format(var1, ratingsvalue)
    bot.send_message(message.chat.id, text, parse_mode = 'HTML')
    bot.send_message(SendChannel, text2, parse_mode = 'HTML')

@bot.message_handler(regexp="3")
def replyCash(message):
    givenRating = (message.text)
    ratingsList.append(int(givenRating))
    text = ("Thank you for your rating of {}⭐️ out of 5⭐️!").format(givenRating)
    var1 = len(ratingsList)
    var2 = sum(ratingsList)
    ratingsvalue = (var2/var1)
    text2 = ("{} customers have rated us!\n \nRating: {}⭐️ out of 5.0⭐️").format(var1, ratingsvalue)
    bot.send_message(message.chat.id, text, parse_mode = 'HTML')
    bot.send_message(SendChannel, text2, parse_mode = 'HTML')

@bot.message_handler(regexp="4")
def replyCash(message):
    givenRating = (message.text)
    ratingsList.append(int(givenRating))
    text = ("Thank you for your rating of {}⭐️ out of 5⭐️!").format(givenRating)
    var1 = len(ratingsList)
    var2 = sum(ratingsList)
    ratingsvalue = (var2/var1)
    text2 = ("{} customers have rated us!\n \nRating: {}⭐️ out of 5.0⭐️").format(var1, ratingsvalue)
    bot.send_message(message.chat.id, text, parse_mode = 'HTML')
    bot.send_message(SendChannel, text2, parse_mode = 'HTML')

@bot.message_handler(regexp="5")
def replyCash(message):
    givenRating = (message.text)
    ratingsList.append(int(givenRating))
    text = ("Thank you for your rating of {}⭐️ out of 5⭐️!").format(givenRating)
    var1 = len(ratingsList)
    var2 = sum(ratingsList)
    ratingsvalue = (var2/var1)
    text2 = ("{} customers have rated us!\n \nRating: {}⭐️ out of 5.0⭐️").format(var1, ratingsvalue)
    bot.send_message(message.chat.id, text, parse_mode = 'HTML')
    bot.send_message(SendChannel, text2, parse_mode = 'HTML')

# compute ratings
@bot.message_handler(commands =['ratings'])
def ratings(message):
    var1 = len(ratingsList)
    var2 = sum(ratingsList)
    ratingsvalue = (var2/var1)
    text = ("{} customers have rated us!\n \nRating: {}⭐️ out of 5.0⭐️").format(var1, ratingsvalue)
    bot.send_message(message.chat.id, text, parse_mode = 'HTML')

customers = [1,1]

# customers
@bot.message_handler(commands =['customers'])
def complete(message):
    var3 = len(customers)
    text = ("<b>MariTest Bot 🤖</b> is happy to serve! \n"
    "We've completed {} transactions!").format(var3)
    bot.send_message(message.chat.id, text, parse_mode = 'HTML')

# completed
@bot.message_handler(commands =['completed'])
def complete(message):
    text = ("Are you done with your transaction? \n")
    bot.send_message(message.chat.id, text, parse_mode = 'HTML')

@bot.message_handler(regexp="yes")
def yesCompleted(message):
    customers.append(1)
    var3 = len(customers)
    text = ("Thank you for choosing <b>MariTest Bot 🤖</b>! \n"
    "We've completed {} transactions!").format(var3)
    bot.send_message(message.chat.id, text, parse_mode = 'HTML')

@bot.message_handler(regexp="no")
def noCompleted(message):
    text = ("How can I help you?\n"
    "\n"
    "Here's my list of commands: \n"
    "<b>/start</b> to start chatting the bot\n"
    "<b>/products</b> to check the products we sell\n"
    "<b>/prices</b> to check the prices of our products\n"
    "<b>/pay</b> to check our available payment methods\n"
    "<b>/feedback</b> to give us feedback on your experience\n"
    "<b>/rate</b> to rate your experience with us\n"
    "<b>/ratings</b> to check the rating of our business\n"
    "<b>/reviews</b> to check other customers' reviews of our business\n"
    "<b>/customers</b> to check how many customers we've served\n"
    "<b>/completed</b> to complete a transaction\n"
    "<b>/help</b> to access our command list"
    )
    bot.send_message(message.chat.id, text, parse_mode = 'HTML')

bot.infinity_polling()

def welcome_msg(item):
    global token
    if item["text"].lower() == "hi":
        msg = 'hello'
        chat_id = item["chat"]["id"]
        user_id = item["from"]["id"]
        user_name = item["from"].get("username",user_id)
        welcome_msg = '''{}'''.format(msg)
        to_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=HTML'.format(token, chat_id, welcome_msg)
        resp = requests.get(to_url)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.get_json()
        data = data["message"]
        welcome_msg(data)
        return { 'statusCode' : 200, 'body' : 'Success' , 'data' : data }
    else:
        return { 'statusCode' : 200, 'body' : 'Success'}



