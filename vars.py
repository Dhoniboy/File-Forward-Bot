from os import environ
import re

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

SESSION = environ.get("SESSION", "forward bot")
API_ID = int(environ.get("API_ID", "17737625"))
API_HASH = environ.get("API_HASH", "7240d6ee4fbe1e00053e107c56912c52")
BOT_TOKEN = environ.get("BOT_TOKEN", "5873739312:AAH3qyTm1bdsKQu-tTBsNyh6pkjlCa7aZMg")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1001883577267"))
PORT = int(environ.get("PORT", "8080"))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1293572362').split()]
TARGET_DB = int(environ.get("TARGET_DB", ""))
UPSTREAM_REPO = environ.get("UPSTREAM_REPO", "https://github.com/Joelkb/File-Forward-Bot")
