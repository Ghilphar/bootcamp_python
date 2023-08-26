import time
from random import randint
import os

def log(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        username = os.getenv('USER', 'user')  # Get the username from the environment variable
        result = func(*args, **kwargs)
        end_time = time.time()
        exec_time_ms = (end_time - start_time) * 1000  # Execution time in milliseconds
        method_name = func.__name__.replace('_', ' ').title()

        if exec_time_ms >= 1000:
            exec_time = exec_time_ms / 1000
            time_unit = "s"
        else:
            exec_time = exec_time_ms
            time_unit = "ms"


        log_message = f"({username})Running: {method_name.ljust(20)} [ exec-time = {exec_time:.3f} {time_unit} ]\n"
        
        with open('machine.log', 'a') as log_file:
            log_file.write(log_message)

        return result
    
    return wrapper

class CoffeeMachine():
    water_level = 100
    
    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False
    @log
    def boil_water(self):
        return "boiling..."

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)