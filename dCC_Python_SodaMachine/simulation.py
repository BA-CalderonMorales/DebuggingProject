from dCC_Python_SodaMachine import user_interface
from dCC_Python_SodaMachine.customer import Customer
from dCC_Python_SodaMachine.soda_machine import SodaMachine
from dCC_Python_SodaMachine.wallet import Wallet


class Simulation:
    def __init__(self):
        pass

    def run_simulation(self):
        """The central method called in main.py."""
        #  Missing import: from dCC_Python_SodaMachine.customer import Customer
        #  Missing import: from dCC_Python_SodaMachine.soda_machine import SodaMachine
        customer = Customer()
        soda_machine = SodaMachine()
        #  Bug: will_proceed was originally False.
        #  Bug: Before doing anything, the welcome function should be displayed.
        self.ui_display_welcome()
        # Bug: User wasn't being prompted before beginning any transaction.
        will_proceed = True
        while will_proceed:
            #  Missing import: from dCC_Python_SodaMachine import user_interface
            user_option = user_interface.simulation_main_menu()
            #  Missing "==". Had only single "=" sign. Single = sign is for assignment
            #  Bug: user_option list in the wrong order. Refactored.
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
            if user_option == "1":
                soda_machine.begin_transaction(customer)
            if user_option == "2":
                #  Imported Wallet class and called fill_wallet() to return
                #  a list of coins. Method name should be renamed.
                current_wallet = Wallet()
                current_wallet_amount = current_wallet.fill_wallet()
                user_interface.display_customer_wallet_info(current_wallet_amount)
            elif user_option == "3":
                customer.check_coins_in_wallet()
            elif user_option == "4":
                customer.check_backpack()
            else:
                will_proceed = False

    def ui_display_welcome(self):
        print("\nWelcome. Please choose from options '1' through '3' below. \n"
              "\tPress '4' to terminate the simulation.\n")