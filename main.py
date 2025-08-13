import logging
import asyncio

from src.application.application import app

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    asyncio.run(app.run())