class Coin:
    def __init__(self, name, value):
        #  Reorganized the order of the attributes. self.name first, then self.value.
        self.name = name
        self.value = value


#  Reorganized the order of each coin so it goes from least valuable to most.
class Penny(Coin):
    def __init__(self):
        super().__init__("Penny", 0.01)


class Nickel(Coin):
    def __init__(self):
        super().__init__("Nickel", 0.05)


class Dime(Coin):
    def __init__(self):
        super().__init__("Dime", 0.10)


class Quarter(Coin):
    def __init__(self):
        super().__init__("Quarter", 0.25)
