# Replit FTPS Uploader (No Google Drive)

This is a Replit-hosted Flask app that accepts POST requests containing an Excel file, and uploads it to an FTPS server (Praxedo).

## 🔐 Required Replit Secrets

- `FTP_USER` – Your Praxedo FTP login
- `FTP_PASS` – Your Praxedo FTP password

## 📤 How to Use from Make.com

In Make.com:
1. Upload or access your Excel file
2. Add an HTTP module:
   - Method: POST
   - URL: your Replit URL (e.g. https://ftps-uploader.replit.app)
   - Body type: `multipart/form-data`
   - Add a field:
     - Name: `file`
     - Type: `File`
     - Value: your file object from previous module

When triggered, the file will be sent directly to the Replit app and forwarded to Praxedo FTPS.