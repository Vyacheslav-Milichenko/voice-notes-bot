from telegram.ext import CommandHandler, ContextTypes
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from db.supabase_client import get_user_id, get_notes

async def list_notes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = get_user_id(update.effective_user.id)
    notes = get_notes(user_id)
    if not notes:
        await update.message.reply_text("У тебя нет заметок.")
        return

    for note in notes:
        btn = InlineKeyboardMarkup([
            [InlineKeyboardButton("Удалить", callback_data=f"delete_{note['id']}")]
        ])
        await update.message.reply_text(note["text"], reply_markup=btn)

list_handler = CommandHandler("list", list_notes)
