from postgrest import Client
from config import SUPABASE_URL, SUPABASE_KEY

supabase = Client(SUPABASE_URL + "/rest/v1")
supabase.auth(SUPABASE_KEY)

def register_user(telegram_id: int):
    res = supabase.from_("users").select("id").eq("telegram_id", telegram_id).execute().data
    if not res:
        supabase.from_("users").insert({"telegram_id": telegram_id}).execute()

def get_user_id(telegram_id: int):
    res = supabase.from_("users").select("id").eq("telegram_id", telegram_id).execute().data
    return res[0]["id"] if res else None

def save_note(user_id: int, text: str):
    supabase.from_("notes").insert({"user_id": user_id, "text": text}).execute()

def get_notes(user_id: int):
    return supabase.from_("notes").select("id", "text", "created_at").eq("user_id", user_id).order("created_at", desc=True).execute().data

def delete_note(note_id: int):
    supabase.from_("notes").delete().eq("id", note_id).execute()
