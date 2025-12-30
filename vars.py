import os
from typing import List

API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_URI = os.getenv("MONGO_URI", "")
DATABASE_CHANNEL_ID = int(os.getenv("DATABASE_CHANNEL_ID", ""))
ADMIN_ID = int(os.getenv("ADMIN_ID", ""))
PICS = (os.environ.get("PICS", "https://i.ibb.co/vvXmVg7f/photo-2025-08-19-14-15-58-7540300909058719748.jpg https://i.ibb.co/v4FWxN8H/photo-2025-08-19-14-15-55-7540300874698981392.jpg https://i.ibb.co/wFtH4YL4/photo-2025-08-19-14-18-22-7540301046497673220.jpg")).split()
LOG_CHNL = int(os.getenv("LOG_CHNL", ""))
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "Zzoorrooo") # Without @
IS_FSUB = bool(os.environ.get("FSUB", True))
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-1002779576540 -1002331917822").split()))
DATABASE_CHANNEL_LOG = int(os.getenv("DATABASE_CHANNEL_LOG", ""))
FREE_VIDEO_DURATION = int(os.getenv("FREE_VIDEO_DURATION", "240"))
