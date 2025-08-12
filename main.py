import logging
import asyncio

from src.utils.config import Config
from src.application.application import Application

logging.basicConfig(level=logging.INFO)

conf = Config()
app = Application(config=conf)

if __name__ == "__main__":
    asyncio.run(app.run())