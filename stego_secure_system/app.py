from flask import Flask, render_template, request, send_file
import os
import secrets
from cryptography.fernet import Fernet
import base64

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "output")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

MARKER = b"STEGO_DATA_START"


# -----------------------------
# Convert 32 char key to Fernet
# -----------------------------
def convert_key(key):
    key = key.encode()
    key = key.ljust(32)[:32]
    return base64.urlsafe_b64encode(key)


# -----------------------------
# Encrypt
# -----------------------------
def encrypt_message(message, key):

    f = Fernet(convert_key(key))
    return f.encrypt(message.encode())


# -----------------------------
# Decrypt
# -----------------------------
def decrypt_message(cipher, key):

    f = Fernet(convert_key(key))
    return f.decrypt(cipher).decode()


# -----------------------------
# Home
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# Embed
# -----------------------------
@app.route("/embed", methods=["POST"])
def embed():

    message = request.form["message"]
    file = request.files["file"]

    filename = file.filename

    upload_path = os.path.join(UPLOAD_FOLDER, filename)
    output_path = os.path.join(OUTPUT_FOLDER, filename)

    # Save uploaded file
    file.save(upload_path)

    # Generate 32 char key
    public_key = secrets.token_hex(16)
    private_key = public_key

    encrypted = encrypt_message(message, public_key)

    # Read original file
    with open(upload_path, "rb") as f:
        original = f.read()

    # Write embedded file
    with open(output_path, "wb") as f:
        f.write(original)
        f.write(MARKER)
        f.write(encrypted)

    return render_template(
        "index.html",
        public_key=public_key,
        private_key=private_key,
        download_file=filename
    )


# -----------------------------
# Download
# -----------------------------
@app.route("/download/<filename>")
def download(filename):

    path = os.path.join(OUTPUT_FOLDER, filename)

    if not os.path.exists(path):
        return "File not found. Try embedding again."

    return send_file(path, as_attachment=True)


# -----------------------------
# Extract
# -----------------------------
@app.route("/extract", methods=["POST"])
def extract():

    private_key = request.form["private_key"]
    file = request.files["file"]

    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    with open(path, "rb") as f:
        data = f.read()

    if MARKER not in data:
        return render_template(
            "index.html",
            extracted_message="No hidden message found."
        )

    encrypted = data.split(MARKER)[-1]

    try:

        message = decrypt_message(encrypted, private_key)

        return render_template(
            "index.html",
            extracted_message=message
        )

    except:

        return render_template(
            "index.html",
            extracted_message="Invalid Private Key"
        )


# -----------------------------
# Run
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)