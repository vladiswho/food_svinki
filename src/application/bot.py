from aiogram import Bot

from src.utils.config import config
class TelegramBot:
    def __init__(self):
        self.bot = Bot(token=config.BOT_TOKEN)

    def get_bot(self):
        return self.bot

bot = TelegramBot()
