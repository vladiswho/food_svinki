import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from src.handlers import start_router, get_recipes_router
from src.utils.config import Config
from src.utils.utils import get_files
from src.utils.recipes_cache import recipes_cache

logger = logging.getLogger(__name__)

class Application:
    def __init__(self, config: Config):
        self.config = config
        self.dp: Dispatcher = Dispatcher(storage=MemoryStorage())
        self.admins = [int(admin_id) for admin_id in self.config.ADMINS.split(",")]

    async def run(self):
        try:
            logger.info(f"Bot starting")
            bot = Bot(token=self.config.BOT_TOKEN)

            self.dp.include_router(start_router)
            self.dp.include_router(get_recipes_router)

            os.makedirs("./recipes/breakfast", exist_ok=True)
            os.makedirs("./recipes/lunch", exist_ok=True)
            os.makedirs("./recipes/dinner", exist_ok=True)

            recipes_cache.BREAKFAST = get_files("./recipes/breakfast")
            recipes_cache.LUNCH = get_files("./recipes/lunch")
            recipes_cache.DINNER = get_files("./recipes/dinner")

            await self.dp.start_polling(bot)
        finally:
            logger.info(f"Bot stopping")

    def get_config(self):
        return self.config

