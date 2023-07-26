from recipe_2 import Recipe
from book import Book
from time import sleep

def main():
    test = Recipe("Barbecue", 4, 5, ["Saucisses", "Viande", "Charbon"], "lunch")
    book_test_1 = Book("Book1")
    print(book_test_1.creation_date)
    try:
        book_test_1.add_recipe("test")
    except Exception as e:
        print(e)

    sleep(2)

    book_test_1.add_recipe(test)

    #print because is the correct name
    book_test_1.get_recipe_by_name("Barbecue")
    #Doesn't print because name doen't exist
    book_test_1.get_recipe_by_name("Couscous")


    test2 = Recipe("Pancakes", 2, 15, ["Flour", "Eggs", "Milk"], "dessert")
    test3 = Recipe("Salad", 1, 10, ["Lettuce", "Tomato", "Cucumber"], "starter")
    book_test_1.add_recipe(test2)
    book_test_1.add_recipe(test3)

    print("Lunch Recipes:", book_test_1.get_recipes_by_types("lunch"))
    print("Dessert Recipes:", book_test_1.get_recipes_by_types("dessert"))
    print("Starter Recipes:", book_test_1.get_recipes_by_types("starter"))
    book_test_1.add_recipe(test3)
    print("Starter Recipes:", book_test_1.get_recipes_by_types("starter"))
    salad = book_test_1.get_recipe_by_name("Salad")
    salad.name = "Salad OGM"
    print("salad.name = 'Salad OGM'")
    print("On peut voir que c'est bien le meme objet au quel on fait reference 2 fois dans la liste")
    print("Starter Recipes:", book_test_1.get_recipes_by_types("starter"))

    print(book_test_1.last_update)

if __name__ == '__main__':
    main()
