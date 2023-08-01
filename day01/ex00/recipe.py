class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients,
                 recipe_type, description=None) -> None:
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.recipe_type = recipe_type
        self.descrioption = description

        if not isinstance(name, str):
            raise TypeError("Recipe name must be a string")
        if not isinstance(cooking_lvl, int) or cooking_lvl not in range(1, 6):
            raise TypeError("Cooking level must be an integer between 1 and 5")
        if not isinstance(cooking_time, int) and cooking_time > 0:
            raise TypeError("Cooking time must be a positive integer.")
        if not isinstance(ingredients, list) or \
           not all(isinstance(ingredient, str) for ingredient in ingredients):
            raise TypeError("Ingredients must be a list of strings.")
        if not isinstance(recipe_type, str) and \
           recipe_type not in ["starter", "lunch", "dessert"]:
            raise ValueError("Recipe type must be starter, lunch or dessert")
        if description and not isinstance(description, str):
            raise TypeError("Recipe description must be a string")

    def __str__(self):
        txt = ""
        txt = f"{self.name} ({self.recipe_type}): Difficulty level" + \
              f"{self.cooking_lvl}, takes {self.cooking_time} minutes to cook\n"
        txt += "Ingredients:\n"
        for ingredient in self.ingredients:
            txt += f"- {ingredient}\n"
        txt += "\nDescription:\n"
        if self.descrioption:
            txt += self.description
        return txt

    def __getitem__(self, key):
        return getattr(self, key, None)


#test = Recipe("felipe", 4, 5, ["test", "test2"], "dessert")
#print(vars(test))
