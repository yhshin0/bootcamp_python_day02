import time
from random import randint


def log(func):
    def write_log(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        t = end - start
        if t < 0.5:
            t = "{:.3f} ms".format(t * 1000)
        else:
            t = "{:.3f} s".format(t)
        name = func.__name__.replace('_', ' ').title()
        f = open("machine.log", "at")
        f.write("(cmaxime)Running: {:<20}[ exec-time = {:<9}]\n"
                .format(name, t))
        f.close()
        return result
    return write_log


class CoffeeMachine():

    water_level = 100

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
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")
