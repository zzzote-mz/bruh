import os

class Config(object):
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "")
    # database uri (mongodb)
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    
    #update channel
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
