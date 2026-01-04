import telebot
import google.generativeai as genai
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

bot = telebot.TeleBot(BOT_TOKEN)

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")

@bot.message_handler(func=lambda m: True)
def handle_message(message):
    try:
        response = model.generate_content(message.text)
        bot.send_message(message.chat.id, response.text)
    except Exception as e:
        bot.send_message(message.chat.id, "Ошибка 😢")

bot.polling()
