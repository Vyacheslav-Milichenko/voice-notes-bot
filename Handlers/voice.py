from telegram.ext import MessageHandler, filters, ContextTypes
from telegram import Update
from pydub import AudioSegment
import speech_recognition as sr
import os
import tempfile
from db.supabase_client import get_user_id, save_note

async def voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = get_user_id(update.effective_user.id)
    voice = await update.message.voice.get_file()
    with tempfile.NamedTemporaryFile(delete=False, suffix=".ogg") as temp:
        await voice.download_to_drive(temp.name)
        audio = AudioSegment.from_ogg(temp.name)
        wav_path = temp.name.replace(".ogg", ".wav")
        audio.export(wav_path, format="wav")

    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language="ru-RU")
            save_note(user_id, text)
            await update.message.reply_text(f"Заметка сохранена:\n{text}")
        except Exception:
            await update.message.reply_text("Не смог распознать голос :(")

    os.remove(temp.name)
    os.remove(wav_path)

voice_handler = MessageHandler(filters.VOICE, voice)
