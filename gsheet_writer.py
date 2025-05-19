import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

def write_to_sheet(data):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    # เปิด Google Sheet
    sheet = client.open_by_key("YOUR_SHEET_ID").sheet1

    # ✅ ดึง userId ทั้งหมดใน column B (index 2)
    existing_user_ids = sheet.col_values(2)

    if data["userId"] in existing_user_ids:
        raise Exception("ผู้ใช้นี้ได้ลงทะเบียนแล้ว")

    # ✅ เพิ่มแถวใหม่
    sheet.append_row([
        data["displayName"],
        data["userId"],
        data["name"],
        data["surname"],
        data["nickname"],
        data["department"],
        data["employeeCode"],
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ])
