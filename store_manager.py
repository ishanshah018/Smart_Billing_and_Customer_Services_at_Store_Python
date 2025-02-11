import sqlite3
import os
import matplotlib.pyplot as plt
from tabulate import tabulate  #for Table Formats
from termcolor import colored  #for Table Colored
from datetime import datetime
import requests # To send promotional message to customer here i used twilio library of python

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
        print("1. View Today's Sales")
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

        # Query to get total sales for today
        self.cursor.execute("""
            SELECT SUM(total_spent) AS total_sales
            FROM monthly_spending
            WHERE bill_date = ?
        """, (today,))

        result = self.cursor.fetchone()

        if not result or result[0] is None:
            print(f"\n🛒 Daily Sales Report ({today}) 🛒\n")
            print("No sales data found for today.\n")
            return

        total_sales = result[0]

        # Table data
        table_data = [[today, f"₹{total_sales:,.2f}"]]
        headers = ["Date", "Total Sales"]

        # Print tabulated sales report
        print("\n" + tabulate(table_data, headers=headers, tablefmt="double_grid", stralign="center") + "\n")

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

        print("\n🔹 Available Customer Phone Numbers 🔹\n")

        # Fetch all customer phone numbers
        self.cursor.execute("SELECT phone FROM customers")
        customers = self.cursor.fetchall()

        if not customers:
            print("❌ No customers found in the database!")
            return

        # Format and display customer phone numbers
        phone_numbers = [[idx + 1, row[0]] for idx, row in enumerate(customers)]
        print(tabulate(phone_numbers, headers=["Sr. No", "Phone Number"], tablefmt="grid"))

        # Ask for the phone number
        while True:
            try:
                selected_index = int(input("\nEnter the Sr. No of the customer to send SMS: ").strip()) - 1
                if selected_index < 0 or selected_index >= len(phone_numbers):
                    print("Invalid selection! Please enter a valid Sr. No.")
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter a numeric value.")

        selected_phone = phone_numbers[selected_index][1]

        # Get the promotional message
        message = input("\nEnter the promotional message: ").strip()
        if not message:
            print("Message cannot be empty!")
            return

        # Send SMS
        self.send_sms(selected_phone, message)

    def send_sms(self, to_number, message):
        
        # Twilio credentials (Replace with your actual details)
        TWILIO_SID = "AC0bf05489aa1d3b0c1f1f190f3d3d4452"
        TWILIO_AUTH_TOKEN = "9c8c360f3977b78acd30c99196439122"
        TWILIO_PHONE_NUMBER = "+16062122916"



        url = f"https://api.twilio.com/2010-04-01/Accounts/{TWILIO_SID}/Messages.json"

        data = {
            "To": to_number,      # The recipient's phone number
            "From": TWILIO_PHONE_NUMBER,  # Your Twilio phone number
            "Body": message       # The message to send
        }

        try:
            response = requests.post(url, data=data, auth=(TWILIO_SID, TWILIO_AUTH_TOKEN))
            
            if response.status_code == 201:
                print(f"\n✅ SMS successfully sent to {to_number}!")
            else:
                print(f"\nFailed to send SMS. Error: {response.text}")

        except requests.exceptions.RequestException as e:
            print(f"Network Error: {e}")

# ----------------------------------------------------------------------------------------------------


    def view_customer_data(self):
        # Fetch all customer data
        self.cursor.execute("SELECT id, name, phone, smart_coins FROM customers")
        results = self.cursor.fetchall()

        if not results:
            print("\nNo customer data available.\n")
            return

        # Table headers
        headers = ["ID", "Name", "Phone", "Smart Coins (₹)"]

        # Format data (round smart coins to 2 decimal places)
        table_data = [[row[0], row[1], row[2], f"₹{row[3]:,.2f}"] for row in results]

        # Print the table with solid borders
        print("\n" + tabulate(table_data, headers=headers, tablefmt="double_grid", colalign=("center", "left", "center", "right")) + "\n")

# ----------------------------------------------------------------------------------------------------


    def view_returned_items(self):
        
        # Fetch returned items from the database
        self.cursor.execute("SELECT id, bill_id, product_name, reason, quantity FROM returned_products")
        results = self.cursor.fetchall()

        if not results:
            print("\nNo returned items found.\n")
            return

        # Table headers
        headers = ["ID", "Bill ID", "Product Name", "Reason", "Quantity"]

        # Format data
        table_data = [[row[0], row[1], row[2], row[3], row[4]] for row in results]

        # Print the table with solid borders
        print("\n" + tabulate(table_data, headers=headers, tablefmt="double_grid", colalign=("center", "center", "left", "left", "center")) + "\n")

# ----------------------------------------------------------------------------------------------------




    def manage_discount_coupons(self):
        
        # Fetch unique categories from the products table
        self.cursor.execute("SELECT DISTINCT category FROM products")
        categories = self.cursor.fetchall()
        
        if categories:
            print("\n🔹 Available Product Categories 🔹")
            print(tabulate(categories, headers=["Category"], tablefmt="grid", numalign="center"))
        else:
            print("No categories found in the products table.")
            return  # Exit if no categories found
        
        print("\nEnter the details below to add a new discount coupon.\n")

        # Get coupon details from the admin
        coupon_code = input("Enter Coupon Code: ").strip().upper()
        
        # Get category from the available options
        while True:
            category = input("Enter Product Category (from above list): ").strip().title()
            # Check if the entered category exists in the available categories
            if any(c[0] == category for c in categories):
                break
            else:
                print(" Invalid category! Please enter a valid category from the list.")

        while True:
            try:
                discount_percentage = float(input("Enter Discount Percentage (%): ").strip())
                if discount_percentage <= 0 or discount_percentage > 100:
                    print("Invalid percentage! Must be between 0 and 100.")
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter a numeric value.")

        while True:
            expiry_date = input("Enter Expiry Date (YYYY-MM-DD): ").strip()
            try:
                # Validate date format
                expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d").date()
                if expiry_date <= datetime.today().date():
                    print("Expiry date must be in the future!")
                    continue
                expiry_date = expiry_date.strftime("%Y-%m-%d")  # Convert back to string for database
                break
            except ValueError:
                print("Invalid date format! Please enter in YYYY-MM-DD format.")

        # Insert data into the database
        try:
            self.cursor.execute("""
                INSERT INTO discount_coupons (coupon_code, category, discount_percentage, expiry_date) 
                VALUES (?, ?, ?, ?)
            """, (coupon_code, category, discount_percentage, expiry_date))
            
            self.connection.commit()  # Commit the transaction
            print(f"\n✅ Coupon '{coupon_code}' added successfully for category '{category}' with {discount_percentage}% discount! Expiry: {expiry_date}\n")

        except Exception as e:
            print(f"Error: {e}\n")       

    def close(self):
        self.connection.close()    

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
                        manager.close();    
                        break
                    else:
                        print(colored("Invalid choice, please try again.", "red"))

        elif choice == "2":
            print(colored("Exiting Store Manager Panel...", "yellow"))
            break
        else:
            print(colored("Invalid choice, please try again.", "red"))
        
        
main()