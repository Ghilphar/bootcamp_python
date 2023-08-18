cookbook = {
    "Sandwich": {
        "ingredients":  ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "Cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "Salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}

def print_recipe_names():
    print("Recipes in the cookbook:")
    for recipe in cookbook:
        print(recipe)

def print_recipe_details(recipe_name):
    if recipe_name in cookbook:
        print(f"\nRecipe for {recipe_name}:")
        for key, value in cookbook[recipe_name].items():
            print(f"\t{key.capitalize()}: {value}")
    else:
        print(f"No recipe found for {recipe_name}")

def delete_recipe(recipe_name):
    if recipe_name in cookbook:
        del cookbook[recipe_name]
        print(f"{recipe_name} has been deleted from the cookbook.")
    else:
        print(f"No recipe found for {recipe_name}")

def add_recipe():
    recipe_name = input("Enter the name of the recipe:\n")

    if recipe_name in cookbook:
        print(f"{recipe_name} already exist in the cookbook.")
        return
    
    ingredients = []
    print("Enter ingredients:")
    while True:
        ingredient = input()
        if not ingredient:
            break
        ingredients.append(ingredient)

    meal = input("Enter the type of meal:")
    
    while True:
        try:
            prep_time = int(input("Enter a preparation time:"))
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

    cookbook[recipe_name] = {
        "ingredients": ingredients,
        "meal": meal,
        "prep_time": prep_time
    }

    print("Recipe has been added.")

def main():
    print("Welcome to the Python Cookbook !")
    while True:
        print("\nList of available option:")
        print("1: Add a recipe")
        print("2: Delete a recipe")
        print("3: Print a recipe")
        print("4: Print the cookbook")
        print("5: Quit")
        choice = input("\n Please select an option:\n")
        if choice == "1":
            add_recipe()
        elif choice == "2":
            recipe_name = input("Enter the name of the recipe to delete:\n")
            delete_recipe(recipe_name)
        elif choice == "3":
            recipe_name = input("Please enter a recipe name to get its details:\n")
            print_recipe_details(recipe_name)
        elif choice == "4":
            print_recipe_names()
        elif choice == "5":
            print("Cookbook closed. Goodbye !")
            break
        else:
            print("Sorry, this option does not exist.")


if __name__ == '__main__':
    main()