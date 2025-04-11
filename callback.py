from telegram.ext import CallbackQueryHandler, ContextTypes
from telegram import Update
from supabase_client import register_user

async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data.startswith("delete_"):
        note_id = int(query.data.split("_")[1])
        delete_note(note_id)
        await query.edit_message_text("Заметка удалена.")

callback_handler = CallbackQueryHandler(callback)
