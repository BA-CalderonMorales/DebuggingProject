from dCC_Python_SodaMachine import coins


class Wallet:
    def __init__(self):
        self.money = []
        #  AttributeError: 'Wallet' had a missing attribute in 'fill_wallet' error was due to scope.
        #  Sometimes, devs forget that having the methods left justified instead of inline with the
        #  scope of each method can lead to this error.

    def fill_wallet(self):
        """Method will fill wallet's money list with certain amount of each type of coin when called."""
        #  Missing import: from dCC_Python_SodaMachine import coins
        for index in range(8):
            self.money.append(coins.Quarter())
        for index in range(10):
            self.money.append(coins.Dime())
        for index in range(20):
            self.money.append(coins.Nickel())
        for index in range(50):
            self.money.append(coins.Penny())
        # Missing return statement. Needs to return the money in the current wallet
            # Will just return the wallet with the money[] list.
        return self.money
