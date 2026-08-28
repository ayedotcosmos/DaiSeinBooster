import os
from flask import Flask, request
import telebot

# BotFather က ရထားသော Bot Token ကို ဒီမှာ ထည့်ပါ
TOKEN = "YOUR_BOT_TOKEN_HERE"
GITHUB_DOWNLOAD_URL = "https://github.com/ayedotcosmos/DaiSeinBooster/releases/download/v1.0.0/app-release.apk"

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Webhook Endpoint
@app.route('/api/webhook', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return 'OK', 200
    else:
        return 'Forbidden', 403

# /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    
    caption_text = f"""👋 မင်္ဂလာပါ {user_name} ဗျို့!

⚡ **DAI SEIN BOOSTER v1.0**
Dai Sein Booster သည် Root ပြုလုပ်ရန် မလိုဘဲ Shizuku API ကို အသုံးပြု၍ ဖုန်း၏ System Settings များနှင့် ဂိမ်း Performance များကို သီးသန့် Optimization ပြုလုပ်ပေးနိုင်သည့် Android Utility App တစ်ခု ဖြစ်ပါတယ်။

✨ **Key Features:**
• AOT Speed Compiler
• 120Hz Refresh Rate Lock
• GPU Debug Layers
• Phantom Process Killer Disable
• RAM Cache Expansion
• One-Tap System Reset

📌 **Requirements:** Android 7.0+ & Shizuku Service

အောက်ပါ Button ကိုနှိပ်ပြီး App ကို Download ရယူနိုင်ပါတယ် 👇"""

    markup = telebot.types.InlineKeyboardMarkup()
    download_button = telebot.types.InlineKeyboardButton("📥 Download APK (v1.0)", url=GITHUB_DOWNLOAD_URL)
    markup.add(download_button)
    
    bot.send_message(message.chat.id, caption_text, reply_markup=markup, parse_mode="Markdown")

# Home route
@app.route('/', methods=['GET'])
def index():
    return "🤖 Dai Sein Booster Webhook Server is LIVE 24/7!", 200
