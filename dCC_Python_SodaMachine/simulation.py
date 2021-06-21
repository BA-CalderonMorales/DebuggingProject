from dCC_Python_SodaMachine import user_interface
from dCC_Python_SodaMachine.customer import Customer
from dCC_Python_SodaMachine.soda_machine import SodaMachine
from dCC_Python_SodaMachine.wallet import Wallet


class Simulation:
    def __init__(self):
        self.customer = Customer()
        self.soda_machine = SodaMachine()
        self.current_wallet = Wallet()
        self.transaction = 0
        self.will_proceed = True

    def run_simulation(self):
        """The central method called in main.py."""
        #  Missing import: from dCC_Python_SodaMachine.customer import Customer
        #  Missing import: from dCC_Python_SodaMachine.soda_machine import SodaMachine
        #  Missing import: Wallet class and called fill_wallet() to return
        #  a list of coins. Method name should be renamed.
        #  Bug: will_proceed was originally False.
        #  Bug: Before doing anything, the welcome function should be displayed.
        self.simulation_welcome()
        user_option = user_interface.simulation_main_menu()
        self.will_proceed = user_option
        while self.will_proceed:
            new_option = user_interface.simulation_main_menu()
            if new_option:
                pass
            else:
                self.will_proceed = False
            #  Missing import: from dCC_Python_SodaMachine import user_interface
            """
            Original if, elif, else before refactor:
            if user_option == "1":
                soda_machine.begin_transaction(customer)
            elif user_option == "2":
                customer.check_coins_in_wallet()
            elif user_option == "3":
                customer.check_backpack()
            else:
                will_proceed = False
            """

    def simulation_welcome(self):
        print("\nWelcome. Please choose from options '1' through '3' below. \n"
              "\tPress '4' to terminate the simulation.\n")
