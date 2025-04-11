from telegram.ext import CommandHandler, ContextTypes
from telegram import Update
from supabase_client import register_user

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    register_user(update.effective_user.id)
    await update.message.reply_text("Привет! Я бот для голосовых заметок. Просто отправь голосовое!")

start_handler = CommandHandler("start", start)
