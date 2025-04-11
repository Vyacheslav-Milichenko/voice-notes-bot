from telegram.ext import ApplicationBuilder
from config import BOT_TOKEN
from handlers.start import start_handler
from handlers.voice import voice_handler
from handlers.list_notes import list_handler
from handlers.callback import callback_handler

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(start_handler)
app.add_handler(voice_handler)
app.add_handler(list_handler)
app.add_handler(callback_handler)

if __name__ == '__main__':
    app.run_polling()
