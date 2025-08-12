from dotenv import dotenv_values
from dataclasses import dataclass

config = dotenv_values(".env")


@dataclass
class Config:
    BOT_TOKEN = config["BOT_TOKEN"]
    ADMINS = config["ADMINS"]
