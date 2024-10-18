import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "28837789"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "33c9162294cdd6c9d51d964e4469fadb")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://smallcapitaltrader1:XVsdQj8vu38ZIFoy@cluster0.9g3ri.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
