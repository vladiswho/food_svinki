__all__ = ("start_router", "get_recipes_router", "post_recipes_router")

from src.handlers.start import start_router
from src.handlers.get_recipes import get_recipes_router
from src.handlers.post_recipe import post_recipes_router
