from supabase import create_client, Client
from config import SUPABASE_URL, SUPABASE_KEY

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def register_user(telegram_id: int):
    res = supabase.table("users").select("id").eq("telegram_id", telegram_id).execute()
    if not res.data:
        supabase.table("users").insert({"telegram_id": telegram_id}).execute()

def get_user_id(telegram_id: int):
    res = supabase.table("users").select("id").eq("telegram_id", telegram_id).execute()
    return res.data[0]["id"] if res.data else None

def save_note(user_id: int, text: str):
    supabase.table("notes").insert({"user_id": user_id, "text": text}).execute()

def get_notes(user_id: int):
    return supabase.table("notes").select("id", "text", "created_at").eq("user_id", user_id).order("created_at", desc=True).execute().data

def delete_note(note_id: int):
    supabase.table("notes").delete().eq("id", note_id).execute()
