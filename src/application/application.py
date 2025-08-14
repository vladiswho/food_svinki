import logging
import os
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from src.handlers import start_router, get_recipes_router, post_recipes_router
from src.utils.config import Config, config
from src.utils.utils import get_files
from src.utils.recipes_cache import recipes_cache
from src.application.bot import bot

logger = logging.getLogger(__name__)

class Application:
    def __init__(self, conf: Config):
        self.config = conf
        self.dp: Dispatcher = Dispatcher(storage=MemoryStorage())
        self.bot = bot.get_bot()

    async def run(self):
        try:
            logger.info(f"Bot starting")

            self.dp.include_router(start_router)
            self.dp.include_router(get_recipes_router)
            self.dp.include_router(post_recipes_router)

            os.makedirs("/data/recipes/breakfast", exist_ok=True)
            os.makedirs("/data/recipes/lunch", exist_ok=True)
            os.makedirs("/data/recipes/dinner", exist_ok=True)

            recipes_cache.BREAKFAST = get_files("/data/recipes/breakfast")
            recipes_cache.LUNCH = get_files("/data/recipes/lunch")
            recipes_cache.DINNER = get_files("/data/recipes/dinner")

            await self.dp.start_polling(self.bot)
        finally:
            logger.info(f"Bot stopping")

app = Application(conf=config)
