from os import environ 

class Config:
    API_ID = environ.get("API_ID", "23685388")
    API_HASH = environ.get("API_HASH", "e36f028c26246e4f7d9143c481dfcdf8")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7584646681:AAEqNo0ejnI6XXL-2Tr8jOaBorp_2LiCELo") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://chhjgjkkjhkjhkjh@cluster0.xowzpr4.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5981648390').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
