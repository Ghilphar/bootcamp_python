import random

def guess_game():
    secret_number = random.randint(1, 99)
    trials = 0
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!\n")

    while True:
        user_input = input("What's your guess between 1 and 99?\n")
        trials += 1

        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        try:
            guessed_number = int(user_input)
            if guessed_number < secret_number:
                print("Too low!")
            elif guessed_number > secret_number:
                print("Too hight!")
            else:
                if secret_number == 42:
                    print("The answer to the ultimate question of life, the universe and everything is 42.")
                if trials == 1:
                    print("Congratulations! You got it on your first try!")
                else:
                    print("Congratulations, you've got it!")
                    print(f"You won in {trials} attempts!")
                break

        except ValueError:
            print("That's not a number.")

if __name__ == "__main__":
    guess_game()