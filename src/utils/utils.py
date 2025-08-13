import os

from src.utils.recipes_cache import recipes_cache

from src.utils.config import config
def read_file(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def get_files(path: str) -> list[str]:
    list_files = []
    for file in os.listdir(path):
        list_files.append(file)
    return list_files

def get_admins():
    admins = [int(admin_id) for admin_id in config.ADMINS.split(",")]
    return admins

def check_if_admin(user_id: int) -> bool:
    admins = get_admins()
    return user_id in admins

def save_file(meal_type: str, recipe_text: str = None, photo_file_id: str = None, photo_bytes: bytes = None):
    save_dir = f"./recipes/{meal_type}"
    filename = ""
    if recipe_text:
        filename = f"recipe_{int(os.times().elapsed*1000)}.txt"
        with open(f"{save_dir}/{filename}", "w", encoding="utf-8") as f:
            f.write(recipe_text)
    elif photo_file_id and photo_bytes:
        filename = f"{photo_file_id}.jpg"
        with open(f"{save_dir}/{filename}", "wb") as f:
            f.write(photo_bytes)
    match meal_type:
        case "breakfast":
            recipes_cache.BREAKFAST.append(filename)
        case "lunch":
            recipes_cache.LUNCH.append(filename)
        case "dinner":
            recipes_cache.DINNER.append(filename)