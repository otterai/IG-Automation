<h1 align="center">📢 Instagram Auto Post Bot 🤖</h1>

<p align="center">
  <img src="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif" width="300px">
</p>

<p align="center">
  <b>📰 Automatically Post Daily Motivational Quotes to Instagram Channels 📩</b><br>
  Fetches quotes from an API & posts them!
  <br><br>
  <img src="https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Telethon-1.24-lightgrey?style=for-the-badge">
  <img src="https://img.shields.io/badge/Auto--Posting-Bot-red?style=for-the-badge">
</p>

<img align="right" alt="count" src="https://count.getloli.com/get/@:otterai?theme=rule34">
    


## 🔥 **Features**
✅ **Auto-Posts Motivational Quotes Daily**  
✅ **Uses a Free Quotes API**   
✅ **Scheduled Posting** (Set Custom Time Intervals)  
✅ **Secure `.env` Config** (API Keys, Channel IDs, etc.)  
✅ **Fast & Lightweight** (Runs 24/7)  

    
> [!CAUTION]
> _```INSTAGRAM CHANNEL I'D FINDER```_
    

```python
from instagrapi import Client

cl = Client()
cl.login("your_username", "your_password")

# Fetch user’s following list (includes channels)
user_id = cl.user_id
following = cl.user_following(user_id)

# Print all joined channels
for user in following.values():
    if user.is_channel:  # Only show channels
        print(f"Channel Name: {user.username} | Channel ID: {user.pk}")
```

---

## 🎯 **How It Works?**
1️⃣ **Fetches a new motivational quote from API**  
2️⃣ **Formats it beautifuly**  
3️⃣ **Auto-posts to Instagram Channel**  
4️⃣ **Repeats at scheduled intervals**  

---

## 📦 **Installation & Setup**  

### 🛠 **1️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
python3 main.py
