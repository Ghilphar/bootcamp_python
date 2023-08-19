from datetime import datetime
from recipe import Recipe

class Book:
    def __init__(self, name):
        self.name = name
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = {
            "starter": [],
            "lunch": [],
            "dessert": []
        }

        if not isinstance(name, str):
            raise TypeError("Book name must be a string")

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for recipe_type in self.recipes_list:
            for recipe in self.recipes_list[recipe_type]:
                if recipe["name"] == name:
                    print(recipe)
                    return recipe
    
    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        recipes_names = []
        for recipe in self.recipes_list[recipe_type]:
            recipes_names.append(recipe.name)
        return recipes_names

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            raise TypeError("Recipe is not from Recipe class")
        recipe_type = recipe["recipe_type"]
        if recipe_type not in ["starter", "lunch", "dessert"]:
            raise ValueError("Invalid recipe_type. Must be one of 'starter', 'lunch', or 'dessert'.")
        self.recipes_list[recipe_type].append(recipe)
        self.last_update = datetime.now()
