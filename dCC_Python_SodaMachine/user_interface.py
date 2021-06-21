import os
import pdb
from math import floor

from dCC_Python_SodaMachine.customer import Customer
from dCC_Python_SodaMachine.soda_machine import SodaMachine
from dCC_Python_SodaMachine.wallet import Wallet


#  One thing I notice is that this Python file doesn't need a class header.
#  I figure this may be due to this being an actual Interface type in Python.
#  I'll come back here in case I find out otherwise.
def simulation_main_menu():
    """Main menu prompting user to choose an option"""
    validate_user_selection = (False, None)
    #  Bug: "Press -#- was off by one number. Updated to proper numeration 1 - 4.
    while validate_user_selection[0] is False:
        print("\t\t-Simulation menu-")
        print("\tPress -1- to begin transaction")
        print("\tPress -2- to check wallet for coins")
        print("\tPress -3- to check backpack for cans")
        print("\tPress -4- to terminate simulation\n")
        user_input = try_parse_int(input("Enter your choice here: "))
        print("\n")
        if user_input == 1:
            soda_machine = SodaMachine()
            new_customer = Customer()
            soda_machine.begin_transaction(new_customer)
            pass
        elif user_input == 2:
            new_wallet = Wallet()
            #  Fill a new_wallet with coins
            display_customer_wallet_info(new_wallet.fill_wallet())
            # Bug:  Added a re-prompt warning after showing the customer their wallet info
            print("\nNow that you've seen your current balance, here are your Main Menu "
                  "choices: \n")
            #  Re-prompted the customer with their options.
            simulation_main_menu()
        elif user_input == 3:
            pass
        elif user_input == 4:
            pass
        #  The following two lines of code just serve for validation of above
        #  prompted input text field.
        validate_user_selection = validate_main_menu(user_input)
    return validate_user_selection[1]


def validate_main_menu(user_input):
    """Validation function that checks if 'user_input' argument is an int 1-4. No errors."""
    switcher = {
        1: (True, 1),
        2: (True, 2),
        3: (True, 3),
        4: (True, 4),
    }
    return switcher.get(user_input, (False, None))


#  Bug: Why pass in the total value when you can just use it inside of the function?
#  Moved total_value from parameter and into a field inside the function.
def display_customer_wallet_info(coins_list):
    """Takes in a list of ints to display number of coins along with total value of coins."""
    # Bug: Missing f'...' at the beginning of the print statement.
    penny_amount = 0
    nickel_amount = 0
    dime_amount = 0
    quarter_amount = 0
    for index in coins_list:
        if index.name == "Penny":
            penny_amount += 1
        elif index.name == "Nickel":
            nickel_amount += 1
        elif index.name == "Dime":
            dime_amount += 1
        elif index.name == "Quarter":
            quarter_amount += 1
    print(f'You have {quarter_amount} Quarters')
    print(f'You have {dime_amount} Dimes')
    print(f'You have {nickel_amount} Nickels')
    print(f'You have {penny_amount} Pennies')
    total_value = add_coins(coins_list)
    #  Get the total_value and round to the nearest whole penny
    print(f"'Your wallet\'s total value is {total_value}")


#  After getting the total number of coins, now the total value should be printed
#  out to the screen. This will get you there.
def add_coins(coins_list):
    total = 0
    for index in coins_list:
        if index.name == "Penny":
            total += index.value
        elif index.name == "Nickel":
            total += index.value
        elif index.name == "Dime":
            total += index.value
        elif index.name == "Quarter":
            total += index.value
    return truncate(total, 2)


"""  
  Allows for precision printing of the current wallet value in $ and cents amounts.
  How this works: the f stands for a float number, and n stands for the decimal
  point position that you want to adhere to without rounding. If I use round(..)
  it would just round the number to the nearest whatever place, which does not sit
  well with money processing. Same logic applies to using floor(...) the following
  website helped me with this solution:
  https://stackoverflow.com/questions/29246455/python-setting-decimal-place-range-without-rounding
"""


def truncate(f, n):
    #  Returns the money currently in the wallet back to the add_coins method.
    return floor(f * 10 ** n) / 10 ** n


def display_welcome():
    """Initial method asking user if they'll make a purchase. No errors."""
    print("\nWelcome to the soda machine.  We only take coins as payment. \n")
    user_response = continue_prompt("Would you like to make a purchase? (y/n):")
    if user_response:
        return True, "y", "yes"
    else:
        print("Please step aside to allow another customer to make a selection")
        return False


def output_text(text):
    """User input method that will print to console any string passed in as an argument"""
    print("text")


def clear_console():
    """Used for clearing out the console. No errors."""
    os.system('cls' if os.name == 'nt' else "clear")


def continue_prompt(text):
    """Validates a 'y' or 'yes' string and returns a True value. No errors."""
    switcher = {
        "y": True,
        "yes": True
    }
    user_input = input(text).lower()
    return switcher.get(user_input, False)


def soda_selection(inventory):
    """Displays purchasable soda inventory and """
    validated_user_selection = (None, None)
    soda_options = get_unique_can_names(inventory)
    while validated_user_selection[0] is False:
        print("Please choose from the following options:")
        i = 1
        for can in soda_options:
            #  Bug: Missing f at the beginning of the quotation
            print(f"\n\tEnter -{i}- for {can} : ${can.price}")
            #  Had i++ instead of i += 1, probably confused languages
            i += 1
        user_selection = try_parse_int(input("Selection:"))
        validated_user_selection = validate_coin_choice(user_selection, soda_options)
    return validated_user_selection[1]


def validate_coin_choice(selection, unique_cans):
    """Translates user menu selection into the name of can that was chosen. No errors."""
    if 0 < selection <= len(unique_cans):
        return True, unique_cans[selection - 1].name
    else:
        print("Not a valid selection\n")
        return False, None


def try_parse_int(value):
    """Attempts to parse a string into an integer, returns 0 if unable to parse. No errors."""
    try:
        return int(value)
    except:
        #  Not a bug or error, just for added clarity
        print("Not a valid entry. Try again.")
        return 0


def get_unique_can_names(inventory):
    """Loops through inventory to create a list of all distinct types of sodas available. No errors."""
    unique_cans = []
    previous_names = []
    for can in inventory:
        if can.name in previous_names:
            continue
        else:
            unique_cans.append(can)
            previous_names.append(can.name)
    return unique_cans


def display_can_cost(selected_can):
    """Displays the name of a can and its price"""
    print(f'The price of a {selected_can.price} is ${selected_can.price}')


def display_payment_value(customer_payment):
    """Displays the value of selected coins as customer is choosing coins to deposit"""
    total_payment_value = 0
    for coin in customer_payment:
        total_payment_value += 1
    total_payment_value = round(total_payment_value, 2)
    print(f'You currently have ${total_payment_value} in hand')


def coin_selection():
    """Prompts user to choose which coins to deposit and passes their selection in validate_coin_selection"""
    validated_user_selection = (False, None)
    while validated_user_selection[0] is False:
        print("\n\tEnter -Q- for Quarter")
        print("\tEnter -D- for Dime")
        print("\tEnter -N- for Nickel")
        print("\tEnter -P- for Penny")
        print("\tEnter -5- for when finished to deposit payment into machine")
        user_input = try_parse_int(input())
        validated_user_selection = validate_coin_selection(user_input)
        if validated_user_selection[0] is False:
            print("Not a valid selection try again")
    return validated_user_selection[1]


def validate_coin_selection(selection):
    """Validation function that checks if 'selection' arugment is an int 1-5"""
    switcher = {
        1: (True, "Quarter"),
        2: (True, "Dime"),
        3: (True, "Nickel"),
        4: (True, "Penny"),
        5: (True, "Done")
    }
    return switcher.get(selection, (False, None))


def end_message(soda_name, change_amount):
    """Closing message displaying name of soda purchased and amount of change returned"""
    #  Invalid parameter: soda was used instead of soda_name inside of print statement.
    print(f'Enjoy your {soda_name}')
    if change_amount >= 0:
        print(f'Dispensing ${change_amount}')
