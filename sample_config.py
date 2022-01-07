import os

class Config(object):
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "")
    # database uri (mongodb)
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    
    #log channel
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    
    #update channel
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
