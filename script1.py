from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# 🔑 Вставьте сюда ваш токен от @BotFather
BOT_TOKEN = "8215439589:AAEQagxd3YomVV8ppttX9EdBIzNzJmX0VAk"

async def echo_ponya(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        if "поня" in update.message.text.lower():
            await update.message.reply_text("поня")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_ponya))
    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()