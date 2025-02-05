import sqlite3
import os
import matplotlib.pyplot as plt
from tabulate import tabulate  #for Table Formats
from termcolor import colored  #for Table Colored
from datetime import datetime, timedelta

# Initialize SQLite database
DB_NAME = "mall_inventory.db"


# Helper functions for date and time
def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")

# Helper functions for Fetching Current Month
def get_current_month():
    return datetime.now().strftime("%Y-%m")  # Returns the current month in 'YYYY-MM' format




class StoreManager:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    @staticmethod

    def login(usname, password):
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM manager WHERE username = ? AND password = ?", (usname, password))
        manager_data = cursor.fetchone()

        # Decoration for the welcome message
        border = "=" * 50
        if manager_data:
            return StoreManager(manager_data[1], manager_data[2]) 
        else:
            print(colored("\n" + border, "red"))
            print(colored(f"\n{'Invalid login credentials. Please try again.':^50}", "red", attrs=["bold"]))
            print(colored(border, "red"))
            return None
    
    def view_products_inventory(self):
        pass
    
    def view_sales_report(self):
        """View sales report with options for daily, monthly, and yearly sales."""
        print("1. View Daily Sales")
        print("2. View Monthly Sales")
        print("3. View Yearly Sales")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            self.daily_sales()
        elif choice == "2":
            self.monthly_sales()
        elif choice == "3":
            self.yearly_sales()
        else:
            print("Invalid choice.")
    
    def daily_sales(self):
        """View daily sales report."""
        pass
    
    def monthly_sales(self):
        """View monthly sales report."""
        pass
    
    def yearly_sales(self):
        """View yearly sales report."""
        pass
    
    def send_promotional_mail_to_customers(self):
        """Send promotional emails to customers."""
        pass
    
    def view_customer_data(self):
        """View customer information."""
        pass
    
    def view_returned_items(self):
        """View list of returned items."""
        pass
    
    def manage_discount_coupons(self):
        """Manage discount coupons (add, remove, update)."""
        pass

    

#---------------------------------Main Function------------------------------------------------------- 
def main():
    while True:
        width = os.get_terminal_size().columns

        # Centered title message
        message = "Welcome to Store Manager Panel"

        # Print centered message
        print("\n" + colored(message.center(width), "yellow", attrs=["bold"]))
        print(colored("\nPlease choose an option:", "green"))

        # Display the main menu options in a table
        main_menu = [
            ["1", "Login"],
            ["2", "Exit"]
        ]

        # Tabulate main menu
        main_menu_table = tabulate(main_menu, tablefmt="fancy_grid", stralign="center")
        print(colored(main_menu_table, "cyan"))

        choice = input("Enter your choice: ")

        if choice == "1":
            usname = input("Enter Manager User ID: ")
            password = input("Enter Password: ")
            manager = StoreManager.login(usname,password)

            if manager:
                while True:
                    # Store Manager menu options
                    manager_menu = [
                        ["1", "View Products Inventory"],
                        ["2", "View Sales Report"],
                        ["3", "Send Promotional Mail to Customers"],
                        ["4", "View Customers Data"],
                        ["5", "View Returned Items by Customers"],
                        ["6", "Manage Discount Coupons"],
                        ["7", "Exit"]
                    ]

                    # Tabulate manager menu
                    manager_menu_table = tabulate(manager_menu, headers=["#", "Option"], tablefmt="fancy_grid", stralign="center")
                    print(colored(manager_menu_table, "magenta"))

                    manager_choice = input("Enter your choice: ")

                    if manager_choice == "1":
                        manager.view_products_inventory()
                    elif manager_choice == "2":
                        manager.view_sales_report()
                    elif manager_choice == "3":
                        manager.send_promotional_mail_to_customers()
                    elif manager_choice == "4":
                        manager.view_customer_data()
                    elif manager_choice == "5":
                        manager.view_returned_items()
                    elif manager_choice == "6":
                        manager.manage_discount_coupons()
                    elif manager_choice == "7":
                        print(colored("Exiting Store Manager Panel...", "yellow"))
                        break
                    else:
                        print(colored("Invalid choice, please try again.", "red"))

        elif choice == "2":
            print(colored("Exiting Store Manager Panel...", "yellow"))
            break
        else:
            print(colored("Invalid choice, please try again.", "red"))
        
        
main()