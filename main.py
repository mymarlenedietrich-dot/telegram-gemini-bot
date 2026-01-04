import telebot
import os
from groq import Groq

BOT_TOKEN = os.getenv("BOT_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

bot = telebot.TeleBot(BOT_TOKEN)

client = Groq(api_key=GROQ_API_KEY)

@bot.message_handler(func=lambda m: True)
def handle_message(message):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": message.text}
            ],
            model="llama3-8b-8192",
        )
        bot.send_message(
            message.chat.id,
            chat_completion.choices[0].message.content
        )
    except Exception as e:
        bot.send_message(message.chat.id, "Ошибка 😢")

bot.polling()
