from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

# Получаем токен из переменной окружения
TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    miniapp_url = "https://telegram-mini-app-umber-kappa.vercel.app/"
    
    # Создаём кнопку для открытия MiniApp
    keyboard = [
        [InlineKeyboardButton("Открыть поиск", web_app={"url": miniapp_url})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Привет! Нажмите на кнопку ниже, чтобы открыть поиск.",
        reply_markup=reply_markup
    )

def main():
    # Создаем приложение
    app = Application.builder().token(TOKEN).build()

    # Обработчик команды /start
    app.add_handler(CommandHandler("start", start))

    # Запускаем бота
    app.run_polling()

if __name__ == '__main__':
    main()
