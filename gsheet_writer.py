import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# ✅ Define scope
scope = ["https://www.googleapis.com/auth/spreadsheets"]

# ✅ ใช้ google-auth แทน oauth2client
creds = Credentials.from_service_account_file(
    "credentials.json",  # ใช้ path เดิมได้เลย (หรือเปลี่ยนเป็น absolute path ถ้าใช้บน Render)
    scopes=scope
)

client = gspread.authorize(creds)

def write_to_sheet(data):
    sheet = client.open_by_key("1wE_j1tnjTK8C7WOxf5KvHJY6_GMYySQ-B4SlixHHyPo").sheet1  # <— เปลี่ยนเป็น sheet ของคุณ

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    row = [
        data.get("displayName"),
        data.get("userId"),
        data.get("name"),
        data.get("surname"),
        data.get("nickname"),
        data.get("department"),
        data.get("employeeCode"),
        now
    ]

    sheet.append_row(row)
