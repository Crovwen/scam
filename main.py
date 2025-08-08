import telebot
import threading
from flask import Flask
import os

TOKEN = "8437336707:AAEOanY7dPCDno66-7s9ImupM_xNcIlUduo"
bot = telebot.TeleBot(TOKEN)

# متن پیام
MESSAGE = """🟢 Owner $ADA 100X 💲: @Owner_ADA100x_free
.
🟢Robot $ADA 100X 💲 : @free100x_ADAbot
.
🟢Chanel $ADA 100X 💲 : @ADA100x_free
.
🟢Group $ADA 100X 💲: @Company_ADA100x_free
.

Hello to all $ADA Mining 100x members. As the name of our large and reputable company suggests, we are here to multiply your money by a hundred. ♥️✔️

You may be wondering how this is possible? The answer is that we are a very powerful team of whales and holders of $ADA, and the rise and fall of $ADA's price is in our hands. We are very wealthy (80% of the world's $ADA are in our accounts), and whenever we want, we can lower its price and whenever we like, we can raise its price. Therefore, we can earn a lot of profit from this work and provide you with a hundredfold profit.💲🔈
"""

PHOTO_PATH = "ada.jpg"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    with open(PHOTO_PATH, 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption=MESSAGE)

# تابع اجرای بات
def run_bot():
    bot.infinity_polling()

# اجرای بات در یک Thread جدا
threading.Thread(target=run_bot).start()

# وب‌سرور Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
