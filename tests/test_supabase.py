import os
from supabase import create_client

def test_supabase_connection():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    client = create_client(url, key)
    res = client.table("prediction_logs").select("*").limit(1).execute()
    assert res.status_code == 200