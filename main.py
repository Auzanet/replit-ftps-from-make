import os
from flask import Flask, request
from ftplib import FTP_TLS
from io import BytesIO

app = Flask(__name__)

FTP_HOST = "ftp-eu9.praxedo.com"
FTP_PORT = 990
FTP_USER = os.getenv("FTP_USER")
FTP_PASS = os.getenv("FTP_PASS")

@app.route("/", methods=["POST"])
def upload_excel():
    if "file" not in request.files:
        return "❌ No file in request", 400

    file = request.files["file"]
    filename = file.filename or "uploaded.xlsx"

    try:
        ftps = FTP_TLS()
        ftps.connect(FTP_HOST, FTP_PORT)
        ftps.auth()
        ftps.prot_p()
        ftps.login(FTP_USER, FTP_PASS)
        ftps.cwd("success")
        ftps.storbinary(f"STOR {filename}", file.stream)
        ftps.quit()
        return f"✅ Uploaded {filename} to Praxedo", 200
    except Exception as e:
        return f"❌ Upload failed: {str(e)}", 500

app.run(host="0.0.0.0", port=8080)