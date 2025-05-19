from flask import Flask, request, jsonify
from gsheet_writer import write_to_sheet
import traceback

app = Flask(__name__)

@app.route("/register", methods=["POST"])
def register():
    try:
        data = request.json
        write_to_sheet(data)
        return jsonify({"message": "✅ Registered successfully"}), 200
    except Exception as e:
        print("🔥 Error in /register")
        traceback.print_exc()  # <--- เพิ่มบรรทัดนี้!
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # ถ้าไม่มี PORT จะ fallback ที่ 5000
    app.run(host="0.0.0.0", port=port, debug=True)