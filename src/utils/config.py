from dotenv import dotenv_values
from dataclasses import dataclass

dotenv_config = dotenv_values(".env")


@dataclass
class Config:
    BOT_TOKEN = dotenv_config["BOT_TOKEN"]
    ADMINS = dotenv_config["ADMINS"]

config = Config()