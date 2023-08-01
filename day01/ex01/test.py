from game import Lannister

tyrion = Lannister("Tyrion")

print(tyrion.__dict__)
tyrion.print_house_words()

print(tyrion.is_alive)
tyrion.die()
print(tyrion.is_alive)
print(tyrion.__doc__)
