import sys
import os
import path
sys.path.append(str(path.Path(os.getcwd()).parent))
import json
from pathlib import Path


class FoodSkills:

    @classmethod
    def get_food_info(cls, question):
        d = Path(__file__).resolve().parents[1]
        with open(os.path.join(d, "files/foods.json"), "r", encoding="utf-8") as f:
            data = json.load(f)
            for food in data["items"]:
                if food["title"].lower() in question:
                 return food["description"]
       