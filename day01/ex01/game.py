class GotCharacter:
    def __init__(self, first_name="No name", is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

        if not isinstance(first_name, str):
            raise TypeError("first_name name must be a string")
        if not isinstance(is_alive, bool):
            raise TypeError("first_name name must be a string")


class Lannister(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Lannister"
        self.house_words = "Lannister always pays his debts."
        self.__doc__ = "A class representing the Lannister family."

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False