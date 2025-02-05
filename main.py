import os
import sys
from tabulate import tabulate  # For table formatting
from termcolor import colored



# Function to print the menu in a centered and properly formatted table
def print_menu():
    width = os.get_terminal_size().columns

    # Menu options to display in the table
    menu_options = [
        ["1", "Store Manager"],
        ["2", "Customer"],
        ["3", "Exit"]
    ]

    # Table headers
    headers = ["Option", "Roles"]

    # Create a table using tabulate
    table = tabulate(menu_options, headers=headers, tablefmt="fancy_grid", numalign="center", stralign="center")

    # Print the table centered on the screen
    print(colored(table.center(width), "yellow"))

while True:
    # Print the centered header
    width = os.get_terminal_size().columns

    # The message you want to center
    message = "WELCOME TO DMART SMART SYSTEM"

    # Print the message centered
    print("\n" + colored(message.center(width), "green", attrs=["bold"]))
    
    # Print the menu in the centered and bordered table format
    print_menu()

    choice = input(colored("Enter your choice (1/2/3): ", "magenta")).strip()
    
    if choice == '1':
        print(colored("\nRedirecting to the Store Manager section...", "green"))
        os.system("python ./store_manager.py")  
    
    elif choice == '2':
        print(colored("\nRedirecting to the Customer section...", "green"))
        os.system("python ./customer.py")    

    elif choice == '3':
        print(colored("Exiting the system. Thank you!", "red"))
        sys.exit(0)
    
    else:
        print(colored("Invalid choice. Please try again.", "yellow"))