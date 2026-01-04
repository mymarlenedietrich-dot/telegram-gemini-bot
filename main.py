import telebot
import os
from groq import Groq
from flask import Flask
import threading

BOT_TOKEN = os.getenv("BOT_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
PORT = int(os.getenv("PORT", 10000))

bot = telebot.TeleBot(BOT_TOKEN)
client = Groq(api_key=GROQ_API_KEY)

@bot.message_handler(func=lambda m: True)
def handle_message(message):
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": message.text}],
            model="llama3-8b-8192",
        )
        bot.send_message(message.chat.id, chat_completion.choices[0].message.content)
    except Exception:
        bot.send_message(message.chat.id, "Ошибка 😢")

def run_bot():
    bot.polling(non_stop=True)

app = Flask(__name__)

@app.route("/")
def home():
    return "OK"

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=PORT)
