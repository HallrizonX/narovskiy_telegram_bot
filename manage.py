from handler import MainHandler
from settings import TELEGRAM_BOT_TOKEN
from utils import log

if __name__ == "__main__":
    bot = MainHandler(TELEGRAM_BOT_TOKEN)
    bot.run()
