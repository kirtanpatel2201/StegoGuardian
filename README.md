# 🔐 StegoGuardian

**StegoGuardian** is a secure steganography-based communication system that encrypts secret messages and hides them inside normal files such as **.txt, .pdf, and .png** for stealth data transmission.

This project combines **cryptography and steganography** to create a secure framework for hiding sensitive information inside everyday files.

---

# 🚀 Project Repository

GitHub Repository:
https://github.com/kirtanpatel2201/StegoGuardian

---

# 📂 Project Structure

```
StegoGuardian
│
└── stego_secure_system
    │
    ├── app.py
    │
    ├── templates
    │   └── index.html
    │
    ├── uploads
    │
    ├── output
    │
    └── README.md
```

---

# ✨ Features

* 🔐 Secure message encryption
* 🕵️ Hidden data inside normal files
* 📄 Supports multiple carrier files:

  * TXT files
  * PDF files
  * PNG images
* 🔑 Public and Private Key based message protection
* 📥 Automatic embedded file download
* 📤 Secure message extraction using private key
* 💻 Clean cybersecurity-themed UI
* ⚡ Lightweight Flask web application

---

# 🧠 How The System Works

## Sender Side

1️⃣ Enter a **secret message**

2️⃣ Upload a **carrier file**

* `.txt`
* `.pdf`
* `.png`

3️⃣ Click **Encrypt & Embed**

### System Process

The system will:

* Encrypt the secret message
* Hide the encrypted data inside the uploaded file
* Generate a **private key**
* Automatically start the download of the **embedded file**

The embedded file appears **completely normal**, but secretly contains the encrypted message.

---

## Receiver Side

1️⃣ Upload the **embedded file**

2️⃣ Enter the **private key**

3️⃣ Click **Decrypt Message**

The system extracts the hidden data and reveals the **original secret message**.

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```
git clone https://github.com/kirtanpatel2201/StegoGuardian.git
```

## 2️⃣ Navigate to Project Folder

```
cd StegoGuardian/stego_secure_system
```

## 3️⃣ Install Required Libraries

```
pip install flask pillow cryptography
```

## 4️⃣ Run Application

```
python app.py
```

## 5️⃣ Open in Browser

```
http://127.0.0.1:5000
```

# 🎯 Use Cases

* Secure communication
* Cybersecurity research
* Data hiding techniques
* Educational cryptography projects
* Privacy-focused messaging

---

# 📌 Future Improvements

* Advanced image steganography
* AES encryption support
* File integrity verification
* Multi-layer encryption
* Secure key exchange mechanism

---

# 👨‍💻 Author

**Kirtan Patel**
---
