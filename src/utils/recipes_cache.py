from dataclasses import dataclass

@dataclass
class Recipes:
    BREAKFAST: list[str]
    LUNCH: list[str]
    DINNER: list[str]

recipes_cache = Recipes