import os
import time
import requests
import schedule
import logging
from instagrapi import Client
from dotenv import load_dotenv
from PIL import Image, ImageDraw, ImageFont
import openai

# Load .env
load_dotenv()

INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
INSTAGRAM_CHANNEL_ID = os.getenv("INSTAGRAM_CHANNEL_ID")  # Channel ID
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# API for fetching motivational quotes
QUOTE_API_URL = "https://api.quotable.io/random?tags=motivational"

# Instagram Client
cl = Client()

# Setup
logging.basicConfig(
    filename="insta_channel_bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def login():
    """Login to Instagram with error handling"""
    try:
        cl.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
        logging.info("✅ Successfully Logged in!")
    except Exception as e:
        logging.error(f"❌ Login Failed: {e}")

def fetch_quote():
    """Fetch Motivational Quote from API & Format it"""
    try:
        response = requests.get(QUOTE_API_URL)
        data = response.json()

        # Formatting Quote for better readability
        quote = f'🌟 **"{data["content"]}"** 🌟\n\n📝 - {data["author"]}'
        return data["content"], data["author"], quote
    except Exception as e:
        logging.error(f"❌ Failed to fetch quote: {e}")
        return None, None, None

def generate_ai_caption(quote):
    """Generate AI-based caption using OpenAI GPT"""
    try:
        openai.api_key = OPENAI_API_KEY
        prompt = f"Create an engaging Instagram caption for this motivational quote: {quote}. Keep it short, inspiring, and add 3 trending hashtags."
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": prompt}]
        )
        caption = response["choices"][0]["message"]["content"].strip()
        return caption
    except Exception as e:
        logging.error(f"❌ Failed to generate AI caption: {e}")
        return "🚀 Stay motivated! #Motivation #Success #Inspiration"

def create_motivational_image(quote, author):
    """Generate an image with the motivational quote"""
    img = Image.new('RGB', (1080, 1080), color=(30, 30, 30))  # Dark gray background
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 45)
    except:
        font = ImageFont.load_default()

    draw.text((100, 400), f'"{quote}"', fill=(255, 255, 255), font=font)
    draw.text((100, 500), f"- {author}", fill=(255, 255, 255), font=font)

    img_path = "quote_post.jpg"
    img.save(img_path)
    return img_path

def post_to_instagram_channel():
    """Post Motivational Quote to Instagram Channel"""
    try:
        quote, author, formatted_quote = fetch_quote()
        if not quote:
            logging.warning("⚠️ No quote found. Skipping post.")
            return

        # Generate AI-based caption
        caption = generate_ai_caption(quote)
        
        # Generate Image with Quote
        img_path = create_motivational_image(quote, author)

        # Post Image
        cl.photo_upload_to_story(img_path, caption, links=[{"webUri": f"https://www.instagram.com/{INSTAGRAM_CHANNEL_ID}/"}])
        logging.info("📢 Motivational Quote Image Posted to Channel Successfully!")
    
    except Exception as e:
        logging.error(f"❌ Failed to post: {e}")

# Auto Re-login
def relogin():
    """Re-login to Instagram every day to avoid session issues"""
    logging.info("🔄 Re-logging into Instagram...")
    login()

# Schedule tasks
schedule.every().day.at("09:00").do(post_to_instagram_channel)
schedule.every().day.at("00:00").do(relogin)  # Re-login at midnight


login()

while True:
    schedule.run_pending()
    time.sleep(60)  # Wait for 60 seconds before checking again
  
