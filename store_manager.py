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

# -----------------------------------------------------------------------------------------------------------------


class StoreManager:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.connection = sqlite3.connect(DB_NAME)
        self.cursor = self.connection.cursor()

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
# -----------------------------------------------------------------------------------------------------------------    
    def view_products_inventory(self):
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        

        if products:
            headers = ["ID", "Name", "Category", "Price", "Stock"]
            
            # Print the products in an attractive table format with enhanced styling
            print("\nAvailable Products:")
            print(tabulate(products, headers=headers, tablefmt="fancy_grid", numalign="center", stralign="center"))
        else:
            print("No products available.")    
        
# -----------------------------------------------------------------------------------------------------------------    

    def view_sales_report(self):
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
        # Get today's date in DD-MM-YYYY format
        today = datetime.now().strftime("%d-%m-%Y")

        # Query to get total sales for each bill date (grouped by day)
        self.cursor.execute("""
            SELECT bill_date, SUM(total_spent) AS total_sales
            FROM monthly_spending
            WHERE bill_date = ?
            GROUP BY bill_date
        """, (today,))

        results = self.cursor.fetchall()

        if not results:
            print(f"No sales data found for {today}.")
            return

        dates = [row[0] for row in results]
        total_sales = [row[1] for row in results]

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.bar(dates, total_sales, color='skyblue')
        plt.title(f"Daily Sales Report ({today})", fontsize=16)
        plt.xlabel("Date", fontsize=12)
        plt.ylabel("Total Sales (₹)", fontsize=12)
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

    def monthly_sales(self):
        # Get current month and year
        current_month = datetime.now().strftime("%m")
        current_year = datetime.now().strftime("%Y")

        # Query to get total sales for each day in the current month
        self.cursor.execute("""
            SELECT SUBSTR(bill_date, 1, 2) AS day, SUM(total_spent) AS total_sales
            FROM monthly_spending
            WHERE SUBSTR(bill_date, 4, 2) = ?  -- Extract MM from DD-MM-YYYY
            AND SUBSTR(bill_date, 7, 4) = ?  -- Extract YYYY from DD-MM-YYYY
            GROUP BY day
        """, (current_month, current_year))

        results = self.cursor.fetchall()

        if not results:
            print(f"No sales data found for {datetime.now().strftime('%B %Y')}.")
            return

        days = [int(row[0]) for row in results]  # Convert day to integer for sorting
        total_sales = [row[1] for row in results]

        # Sorting to maintain correct order of dates
        days, total_sales = zip(*sorted(zip(days, total_sales)))

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.plot(days, total_sales, marker='o', linestyle='-', color='blue')
        plt.title(f"Monthly Sales Report ({datetime.now().strftime('%B %Y')})", fontsize=16)
        plt.xlabel("Day", fontsize=12)
        plt.ylabel("Total Sales (₹)", fontsize=12)
        plt.xticks(days)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

    def yearly_sales(self):
        """View yearly sales report."""
        # Get current year
        current_year = datetime.now().strftime("%Y")

        # Query to get total sales for each month in the current year
        self.cursor.execute("""
            SELECT SUBSTR(bill_date, 4, 2) AS month, SUM(total_spent) AS total_sales
            FROM monthly_spending
            WHERE SUBSTR(bill_date, 7, 4) = ?  -- Extract YYYY from DD-MM-YYYY
            GROUP BY month
        """, (current_year,))

        results = self.cursor.fetchall()

        if not results:
            print(f"No sales data found for {current_year}.")
            return

        months = [int(row[0]) for row in results]  # Convert month to integer for sorting
        total_sales = [row[1] for row in results]

        # Sorting to maintain correct order of months
        months, total_sales = zip(*sorted(zip(months, total_sales)))

        # Month labels
        month_labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        month_labels = [month_labels[m-1] for m in months]  # Convert numeric month to name

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.bar(month_labels, total_sales, color='green')
        plt.title(f"Yearly Sales Report ({current_year})", fontsize=16)
        plt.xlabel("Month", fontsize=12)
        plt.ylabel("Total Sales (₹)", fontsize=12)
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

# ----------------------------------------------------------------------------------------------------

    
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

    
# ----------------------------------------------------------------------------------------------------
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