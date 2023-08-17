import random

class Dice():
    def __init__(self,num_sides):
        self.sides = num_sides

    def roll(self):
        """
        Return a random number between 1 and the number of sides
        """
        return random.randint(1, self.sides)


if __name__ == "__main__":
    d = Dice(6)
    for i in range(100):
        print(d.roll())