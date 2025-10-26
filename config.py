
import os

API_ID =
API_HASH = ""
BOT_TOKEN = ""


DOWNLOAD_DIR = "downloads"


ALLOWED_GROUP_IDS = [
    ,
]

OWNER_ID =

MAX_FILE_SIZE = 4 * 1024 * 1024 * 1024

PREMIUM_USERS = {5756495153}
DAILY_LIMIT_FREE = 15
DAILY_LIMIT_PREMIUM = 30

os.makedirs(DOWNLOAD_DIR, exist_ok=True)
if not os.access(DOWNLOAD_DIR, os.W_OK):
    raise PermissionError(f"No write permission for {DOWNLOAD_DIR}")
