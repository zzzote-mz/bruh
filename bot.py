import logging
import logging.config

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)


from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from info import SESSION, API_ID, API_HASH, BOT_TOKEN, LOG_STR


class Bot(Client):

    def __init__(self):
        super().__init__(
            name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
        await super().start()
        await self.send_message(-1001126383177, "Upgrade Finished ✅")
        logging.info(LOG_STR)

    async def stop(self, *args):
        await self.send_message(-1001126383177, "Bot Stoped 🚫")
        await super().stop()
        logging.info("Bot stopped. Bye.")


app = Bot()
app.run()
