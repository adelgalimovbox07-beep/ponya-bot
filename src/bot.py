from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import os

# Получаем токен из переменной окружения
BOT_TOKEN = os.environ["BOT_TOKEN"]

async def echo_ponya(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        if "поня" in update.message.text.lower():
            await update.message.reply_text("поня")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_ponya))
    print("✅ Бот запущен и слушает сообщения...")
    app.run_polling()

if __name__ == "__main__":
    main()
