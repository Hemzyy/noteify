# 🎵 Noteify  

**Automatically share your Spotify listening activity to Instagram Notes in real time**  

![Noteify Preview](/assets/CaptureNoteify.PNG)  

## 🚀 About  

Noteify is a Python script that connects to **Spotify** and **Instagram** APIs to automatically update your Instagram Notes with your currently playing song on Spotify.  

## ✨ Features  

- **Real-time updates**: Detects your currently playing song and updates your Instagram Notes instantly.  
- **Seamless integration**: Uses `spotipy` for Spotify API and `instagrapi` for Instagram automation.  
- **Lightweight & efficient**: Runs in the background and updates only when the song changes.  

## 🛠️ Installation  

### 1️⃣ Clone the repository  

```bash
git clone https://github.com/Hemzyy/noteify.git
cd noteify

### 2️⃣ Install dependencies (imports)

### 3️⃣ Set up environment variables

Create a .env file in the project directory and add your credentials:
```
SPOTIPY_CLIENT_ID=your_spotify_client_id
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
SPOTIPY_REDIRECT_URI=your_redirect_uri

ACCOUNT_USERNAME=your_instagram_username
ACCOUNT_PASSWORD=your_instagram_password
```

## ⚠ Important: Using your Instagram password directly in scripts is risky.

### 🎯 Usage

Run the script by providing your Spotify username:
```
python noteify.py your_spotify_username
```

### 🛡️ Disclaimer

This project is for educational purposes only. Automating Instagram interactions may violate Instagram's terms of service. Use at your own risk.
