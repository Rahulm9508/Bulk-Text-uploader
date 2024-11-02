import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7667053478:AAGUm8yEaroZVT-utmZVeachNUv0uK1IMwM")
    
    API_ID = int(os.environ.get("API_ID", "20346550"))
    API_HASH = os.environ.get("API_HASH", "bc79c3bea7a626887bdc0871eecf0327)
    AUTH_USERS = os.environ.get("AUTH_USERS","7081036509")
    
