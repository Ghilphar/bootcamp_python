class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description = None ) -> None:
        if (isinstance(name, str)):
            self.name = name
        else:
            print("name must be an str.")
        if (isinstance(cooking_lvl, int) and cooking_lvl in range(1, 6)):
            self.cooking_lvl = cooking_lvl
        else: 
            print("cooking_lvl must be an int between 1 and 5.")
        if (isinstance(cooking_time, int) and cooking_time > 0):
            self.cooking_time = cooking_time
        else:
            print("cooking time must be a possitive integer")
        if (ingredients and all(isinstance(ingredient, str) for ingredient in ingredients)):
            self.ingredients = ingredients
        else:
            print("Ingredients must be at least a list of one string.")
        if (isinstance(recipe_type, str) and recipe_type.lower() in ["starter", "lunch", "dessert"]):
            self.recipe_type = recipe_type
        else:
            print("recipe_type must be starter, lunch or dessert.")
        if (isinstance(description, str)):
            self.descrioption = description

test = Recipe("felipe", 4, 5, ["test", "test2"], "dessert")
print(vars(test))