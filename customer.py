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

# Customer Class
class Customer:
    def __init__(self, name, phone, password, smart_coins=0.0):
        self.name = name
        self.phone = phone
        self.password = password
        self.smart_coins = smart_coins

        # Database connection and cursor initialization
        self.connection = sqlite3.connect(DB_NAME)  # Replace with your actual database name
        self.cursor = self.connection.cursor()
        

    # Register customer
    @staticmethod
    
    def login(phone, password):
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM customers WHERE phone = ? AND password = ?", (phone, password))
        customer_data = cursor.fetchone()

        # Decoration for the welcome message
        border = "=" * 50
        if customer_data:
            print(colored("\n" + border, "cyan"))
            print(colored(f"\n{'Welcome back, ' + customer_data[1] + '!':^50}", "yellow", attrs=["bold"]))
            print(colored(border, "cyan"))
            return Customer(customer_data[1], customer_data[2], customer_data[3], customer_data[4])
        else:
            print(colored("\n" + border, "red"))
            print(colored(f"\n{'Invalid login credentials. Please try again.':^50}", "red", attrs=["bold"]))
            print(colored(border, "red"))
            return None
# -----------------------------------------------------------------------------------------------------------------

    # Function to display products 

    def view_products(self):
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

    # View discount offers
    def view_discount_offers(self):
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        cursor.execute("SELECT product_name, discount_type, discount_description FROM product_discounts")
        offers = cursor.fetchall()
        

        if offers:
            print("\nAvailable Offers:")
            for offer in offers:
                print(f"Product: {offer[0]}, Discount Type: {offer[1]}, Description: {offer[2]}")
        else:
            print("No offers available.")
# -----------------------------------------------------------------------------------------------------------------

    # View smart coins balance
    def view_smart_coins(self):
        # Connect to the database
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()

        # Fetch the current smart coins balance from the database
        cursor.execute("""
            SELECT smart_coins
            FROM customers
            WHERE phone = ?
        """, (self.phone,))
        result = cursor.fetchone()

        if result:  # Check if a record is returned
            smart_coins_balance = result[0]
            print(f"Your current Smart Coins balance is: {smart_coins_balance}")

# -----------------------------------------------------------------------------------------------------------------

    # View Past bills acc to year,month,date filter
    def view_past_bills(self):
        print("\nView Your Past Bills:")

        # Step 1: Ask user for a filter option
        print("\nFilter Options:")
        print("1. View All Bills")
        print("2. Filter by Year")
        print("3. Filter by Month and Year")
        print("4. Filter by Specific Date")
        filter_choice = input("\nChoose a filter option (1-4): ").strip()

        # Step 2: Build the query based on the user's choice
        query = "SELECT id, bill_date, total_amount, discount, final_amount FROM bills WHERE customer_mobile = ?"
        params = [self.phone]  # Use phone for querying the bills table

        if filter_choice == "2":  # Filter by Year
            year = input("Enter the year (e.g., 2025): ").strip()
            query += " AND strftime('%Y', bill_date) = ?"
            params.append(year)
        elif filter_choice == "3":  # Filter by Month and Year
            month = input("Enter the month (1-12): ").zfill(2)
            year = input("Enter the year (e.g., 2025): ").strip()
            query += " AND strftime('%Y-%m', bill_date) = ?"
            params.append(f"{year}-{month}")
        elif filter_choice == "4":  # Filter by Specific Date
            date = input("Enter the date (YYYY-MM-DD): ").strip()
            query += " AND bill_date = ?"
            params.append(date)

        # Step 3: Fetch and display bills from the database
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        cursor.execute(query, tuple(params))
        bills = cursor.fetchall()
        

        # Step 4: Check if bills exist
        if not bills:
            print("\nNo bills found for the selected filter.")
            return

        # Step 5: Display bills in a tabular format
        headers = ["Bill ID", "Date", "Total", "Discount", "Final", "Smart Coins"]

        # Format the rows with colors
        formatted_bills = []
        for bill in bills:

            formatted_bills.append([
                colored(str(bill[0]), "cyan"),                # Bill ID
                colored(str(bill[1]), "yellow"),             # Date
                colored(f"{bill[2]:.2f}", "green"),          # Total
                colored(f"{bill[3]:.2f}", "red"),            # Discount
                colored(f"{bill[4]:.2f}", "blue"),           # Final
            ])

        # Use tabulate to display the table
        print("\nBills Summary:")
        print(tabulate(formatted_bills, headers=headers, tablefmt="fancy_grid"))

# -----------------------------------------------------------------------------------------------------------------

        
    # To view Coupons

    @staticmethod
    def view_coupons():
        """Displays all active discount coupons available in the store."""
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()

        # Fetch active coupons based on expiry date
        print("\nAvailable Discount Coupons at Our Store:")
        cursor.execute("""
            SELECT coupon_code, category, discount_percentage, expiry_date
            FROM discount_coupons
            WHERE expiry_date >= ?
        """, (datetime.now().strftime("%Y-%m-%d"),))
        coupons = cursor.fetchall()
        
        if not coupons:
            print("No active coupons available at the moment.")
        else:
        # Prepare the coupons for tabulation
            formatted_coupons = []
            for coupon in coupons:
                formatted_coupons.append((
                    colored(coupon[0], 'cyan'),
                    colored(coupon[1], 'yellow'),
                    colored(f"{coupon[2]:.2f}", 'green'),
                    colored(coupon[3], 'magenta')
                ))

            # Define the headers
            headers = ["Coupon Code", "Category", "Discount (%)", "Valid Till"]

            # Print the coupons in a fancy grid format with alignment
            print("\nActive Coupons:")
            print(tabulate(formatted_coupons, headers=headers, tablefmt="fancy_grid", numalign="center", stralign="center"))

# -----------------------------------------------------------------------------------------------------------------

    
    # For Return/Refund
    def request_refund_replacement(self):
        print("\n--- Request Refund or Replacement ---")
        

        # Step 1: Fetch Bill IDs from the last 30 days for the current user
        thirty_days_ago = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
        self.cursor.execute("SELECT id, bill_date FROM bills WHERE customer_mobile = ? AND bill_date >= ?", (self.phone, thirty_days_ago))
        recent_bills = self.cursor.fetchall()

        if not recent_bills:
            print("No Purchase Bills found in the last 30 days.")
            return

        # Step 2: Display Bill IDs to the user (showing only the current user's bills)
        print("\nYour Bills in the Last 30 Days:")
        for bill in recent_bills:
            print(f"Bill ID: {bill[0]} | Date: {bill[1]}")

        # Step 3: Ask for Bill ID (and ensure it's for the current user)
        bill_id = input("Enter the Bill ID for which you want to request a return or replacement: ")

        # Check if the entered Bill ID belongs to the current customer
        self.cursor.execute("SELECT * FROM bills WHERE id = ? AND customer_mobile = ?", (bill_id, self.phone))
        bill = self.cursor.fetchone()

        if not bill:
            print("Invalid Bill ID for your account. Please try again.")
            return

        # Step 4: Display products in the bill
        print(f"\nProducts in Bill ID {bill_id}:")
        self.cursor.execute("SELECT item_name, quantity, price FROM item_purchase_history WHERE bill_id = ?", (bill_id,))
        items = self.cursor.fetchall()

        if not items:
            print("No items found in the bill.")
            return

        for item in items:
            print(f"- {item[0]} (Quantity: {item[1]}, Price per item: ₹{item[2]})")

        # Step 3: Ask for Product Name
        product_name = input("\nEnter the product name for which you want to request a return or replacement: ")

        # Join item_purchase_history and products tables on item_name and fetch category
        self.cursor.execute(
            "SELECT iph.quantity, iph.price, p.category FROM item_purchase_history iph "
            "JOIN products p ON iph.item_name = p.name "
            "WHERE iph.bill_id = ? AND iph.item_name = ?",
            (bill_id, product_name)
        )
        product = self.cursor.fetchone()

        if not product:
            print(f"Product '{product_name}' not found in the bill. Please try again.")
            return

        quantity, price_per_item, category = product

        # List of restricted categories for return and replacement
        restricted_categories = [
            "Dairy", "Snacks", "Beverages", "Fruits", "Bakery", "Vegetables", 
        ]

        # Check if the product category is restricted
        if category in restricted_categories:
            print(f"Sorry, products in the '{category}' category cannot be returned or replaced because they are from Consumables Category.")
            return

        # Step 4: Choose between Return and Replacement
        print("\nWhat would you like to do?")
        print("1. Return")
        print("2. Replacement")
        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            # Return Process
            reasons_return = [
                "Defective Product",
                "Item Not as Described",
                "Expired Product",
                "Other"
            ]
            print("\nSelect a reason for return:")
            for i, reason in enumerate(reasons_return, 1):
                print(f"{i}. {reason}")
            reason_choice = int(input("Enter your choice: "))

            if reason_choice < 1 or reason_choice > len(reasons_return):
                print("Invalid reason choice. Please try again.")
                return

            reason = reasons_return[reason_choice - 1]

            # Ask for number of items to return
            num_items = int(input(f"Enter the number of '{product_name}' items to return (Max {quantity}): "))

            if num_items < 1 or num_items > quantity:
                print(f"Invalid quantity. Must be between 1 and {quantity}.")
                return

            refund_amount = num_items * price_per_item

            # Insert return record into returned_products table
            self.cursor.execute(
                "INSERT INTO returned_products (bill_id, product_name, reason, quantity) VALUES (?, ?, ?, ?)",
                (bill_id, product_name, reason, num_items)
            )
            self.cursor.connection.commit()

            # Update Smart points
            self.cursor.execute(
                "SELECT smart_coins FROM customers WHERE phone = ?",
                (bill[1],)
            )
            smart_coins = self.cursor.fetchone()[0]
            new_smart_coins= smart_coins + refund_amount
            self.cursor.execute(
                "UPDATE customers SET smart_coins = ? WHERE phone = ?",
                (new_smart_coins, bill[1])
            )
            self.connection.commit()

            print(f"\nRefund processed successfully! ₹{refund_amount} has been credited to your smart points.")

        elif choice == "2":
            # Replacement Process
            reasons_replacement = [
                "Defective Product",
                "Wrong Item Delivered",
                "Damaged During Transit",
                "Other"
            ]
            print("\nSelect a reason for replacement:")
            for i, reason in enumerate(reasons_replacement, 1):
                print(f"{i}. {reason}")
            reason_choice = int(input("Enter your choice: "))

            if reason_choice < 1 or reason_choice > len(reasons_replacement):
                print("Invalid reason choice. Please try again.")
                return

            reason = reasons_replacement[reason_choice - 1]

            # Ask for number of items to replace
            num_items = int(input(f"Enter the number of '{product_name}' items to replace (Max {quantity}): "))

            if num_items < 1 or num_items > quantity:
                print(f"Invalid quantity. Must be between 1 and {quantity}.")
                return

            # Insert replacement record into returned_products table
            self.cursor.execute(
                "INSERT INTO returned_products (bill_id, product_name, reason, quantity) VALUES (?, ?, ?, ?)",
                (bill_id, product_name, reason, num_items)
            )
            self.cursor.connection.commit()

            # Check stock availability
            self.cursor.execute(
                "SELECT stock FROM products WHERE name = ?", (product_name,)
            )
            stock = self.cursor.fetchone()

            if not stock or stock[0] < num_items:
                print(f"Sorry, insufficient stock to process replacement for {num_items} items.")
                return

            # Update original stock from products table after giving new item to customer
            new_stock = stock[0] - num_items
            self.cursor.execute(
                "UPDATE products SET stock = ? WHERE name = ?",
                (new_stock, product_name)
            )
            self.cursor.connection.commit()

            print(f"\nReplacement processed successfully! {num_items} new '{product_name}' items have been issued to you.")

        else:
            print("Invalid choice. Please try again.")
            return

        # Commit changes to the database
        self.connection.commit()
        print("\nRequest successfully processed. Thank you!")

# -----------------------------------------------------------------------------------------------------------------


# ***********************************
    # Generate and display the bill
    def generate_bill(self):
        items = []
        print("\nAdd Items To Your Bill. Type 'stop' when you're done.")

        while True:
            item_name = input("Enter the product name to add to the bill: ").strip()
            if item_name.lower() == 'stop':
                break

            # Connect to the database to retrieve product details
            connection = sqlite3.connect(DB_NAME)
            cursor = connection.cursor()

            # Case-insensitive product search
            cursor.execute("SELECT * FROM products WHERE LOWER(name) = LOWER(?)", (item_name,))
            product = cursor.fetchone()

            if product:
                product_name = product[1]  
                price = product[3]         
                stock = int(product[4])      

                if stock > 0:
                    quantity = int(input(f"Enter the quantity of {product_name} to add: "))

                    if quantity <= stock:
                        # Add product to the bill
                        items.append({'name': product_name, 'quantity': quantity, 'price': price})

                        # Update stock in the database
                        cursor.execute(
                            "UPDATE products SET stock = stock - ? WHERE LOWER(name) = LOWER(?)",
                            (quantity, item_name)
                        )
                        connection.commit()

                        print(f"'{product_name}' added to the bill. Quantity: {quantity}, Price per unit: {price}")
                    else:
                        print(f"Only {stock} units of '{product_name}' are available.")
                else:
                    print(f"'{product_name}' is out of stock.")
            else:
                print("Product not available.")

            

        # Display bill summary
        print("\nBill Summary:")
        total_amount = 0
        for item in items:
            item_total = item['price'] * item['quantity']
            total_amount += item_total
            print(f"Product: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}, Subtotal: {item_total}")

        print(f"\nTotal Amount before discounts: {total_amount}")


        # Apply Buy X Get X Free discounts (if any)
        for item in items:
            connection = sqlite3.connect(DB_NAME)
            cursor = connection.cursor()

            # Check for applicable discount in the product_discounts table
            cursor.execute(
                "SELECT discount_type FROM product_discounts WHERE LOWER(product_name) = LOWER(?)",
                (item['name'],)
            )
            discount_data = cursor.fetchone()

            if discount_data:
                discount_type = discount_data[0]
                # Parse discount details
                if "Buy" in discount_type and "Get" in discount_type:
                    # Example: "Buy 10 Get 1 Free"
                    parts = discount_type.split()
                    buy_quantity = int(parts[1])  # Extract '10' from "Buy 10"
                    free_quantity = int(parts[3])  # Extract '1' from "Get 1"

                    # Calculate free items based on the quantity purchased
                    free_items = (item['quantity'] // buy_quantity) * free_quantity

                    if free_items > 0:
                        print(f"Hurray! You got {free_items} free {item['name']}(s) worth {free_items * item['price']}!")

                        # Add free items to the bill
                        item['quantity'] += free_items  # Update quantity for this item

                        # Update stock in the database for the free items
                        cursor.execute(
                            "UPDATE products SET stock = stock - ? WHERE LOWER(name) = LOWER(?)",
                            (free_items, item['name'])
                        )
                        connection.commit()

                        print(f"{free_items} free {item['name']}(s) added to your bill, and stock updated.")

            connection.commit()

        # Ask user if they want to apply a coupon
        coupon_code = input("Enter Coupon Code (if any or press Enter to skip): ")
        if coupon_code:
            connection = sqlite3.connect(DB_NAME)
            cursor = connection.cursor()
            cursor.execute("SELECT discount_percentage FROM discount_coupons WHERE coupon_code = ? AND expiry_date >= ?", 
            (coupon_code, get_current_date()))
            coupon = cursor.fetchone()
            connection.commit()

            if coupon:
                discount += total_amount * (coupon[0] / 100)
                print(f"Hurray! You got {coupon[0]}% discount using coupon code {coupon_code}.")
            else:
                print("Invalid or expired coupon code.")

        discount = 0
        # Ask if user wants to redeem Smart Coins
        # Ask if the user wants to redeem Smart Coins
        if self.smart_coins > 0:
            self.view_smart_coins()
            redeem_coins = float(input("Enter how many Smart Coins you want to redeem: "))
            
            # Calculate the maximum coins that can be redeemed based on the bill amount
            max_redeemable_coins = min(self.smart_coins, total_amount)  # Ensure it does not exceed the bill amount
            
            if redeem_coins > max_redeemable_coins:
                print(f"You can only redeem up to {max_redeemable_coins} Smart Coins based on your bill amount of ₹{total_amount}.")
            else:
                # Deduct the redeemed smart coins from the user's balance
                self.smart_coins -= redeem_coins  # Update the local balance
                
                # Update the smart coins in the database based on the mobile number
                cursor.execute(
                    "UPDATE customers SET smart_coins = ? WHERE phone = ?",
                    (self.smart_coins, self.phone)  # Use the mobile number for identification
                )
                cursor.connection.commit()  # Commit the changes to the database
                
                # Apply the discount for the redeemed coins
                discount += redeem_coins
                print(f"Your {redeem_coins} Smart Coins have been redeemed. ₹{redeem_coins} has been deducted from your bill.")

        # Apply GST (Assuming 18% GST for this example)
        gst = total_amount * 0.18
        final_amount = total_amount - discount + gst
        new_smart_coins = final_amount * 0.05  # 5% of final amount

        print("\nFinal Bill Summary:")
        print("-" * 40)
        print("Product Name | Quantity | Price | Total")
        for item in items:
            print(f"{item['name']} | {item['quantity']} | {item['price']} | {item['price'] * item['quantity']}")
        print("-" * 40)
        print(f"Total Amount: {total_amount}")
        print(f"Discount Applied: {discount}")
        print(f"GST (18%): {gst}")
        print(f"Final Amount: {final_amount}")
        print(f"New Smart Coins Earned: {new_smart_coins}")
        print("-" * 40)

        # Ask if user wants to save the bill
        save_option = input("Do you want to save this bill? (yes/no): ").lower()
        if save_option == "yes":
            self.save_bill(total_amount, discount, gst, final_amount, new_smart_coins)

        # Update Smart Coins 
        self.smart_coins += new_smart_coins
        print(f"Your new Smart Coins balance: {self.smart_coins}")


        # Update the customer's smart coins in the database
        cursor.execute("""
            UPDATE customers 
            SET smart_coins = ? 
            WHERE phone = ?
        """, (self.smart_coins, self.phone))  # phone is unique to identify customer
        connection.commit()

        # Insert final bill details into the `bills` table
        customer_mob = self.phone  # Replace with actual method of fetching customer mobile number
        current_date = get_current_date()  # Assuming a function to get the current date

        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()

        # Insert into `bills` table
        cursor.execute("""
            INSERT INTO bills (customer_mobile, bill_date, total_amount, discount, final_amount)
            VALUES (?, ?, ?, ?, ?)
        """, (customer_mob, current_date, total_amount, discount, final_amount))
        connection.commit()

        bill_id = cursor.lastrowid

        # Update category_spending and monthly_spending tables
        self.update_spending_data(items,bill_id)

# -----------------------------------------------------------------------------------------------------------------


    # Save the bill to a text file
    def save_bill(self, total_amount, discount, gst, final_amount, smart_coins):
        # Set the file name to save in the current directory acc to users details_date-purchased
        file_name = f"{self.phone}_{get_current_date()}.txt"  

        with open(file_name, "a") as file:
            file.write(f"Date: {get_current_date()}\n")
            file.write(f"Total Amount: {total_amount}\n")
            file.write(f"Discount: {discount}\n")
            file.write(f"GST (18%): {gst}\n")
            file.write(f"Final Amount: {final_amount}\n")
            file.write(f"Smart Coins Earned: {smart_coins}\n")
            file.write("================================================")

        print(f"Bill saved to {file_name}")

# -----------------------------------------------------------------------------------------------------------------


    # Update spending data in database
    def update_spending_data(self, items, bill_id):
        customer_mob = self.phone  # Example: Replace this with your actual method of fetching customer mobile number
        current_month = get_current_month()  # Should return the current month in 'YYYY-MM' format

        # Connect to the database
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()

        for item in items:
            # Fetch the category for the item (assuming each item has a category in the products table)
            cursor.execute("SELECT category FROM products WHERE name = ?", (item['name'],))
            category_data = cursor.fetchone()

            if category_data:
                category_name = category_data[0]

                # Update category_spending table (if a record exists, update the total_spent and total_items)
                cursor.execute("""
                    INSERT INTO category_spending (customer_mobile, category, total_spent, total_items, bill_id)
                    VALUES (?, ?, ?, ?, ?)
                    ON CONFLICT(customer_mobile, category, bill_id) DO UPDATE SET 
                        total_spent = total_spent + ?, 
                        total_items = total_items + ?
                """, (customer_mob, category_name, item['price'] * item['quantity'], item['quantity'], bill_id,
                    item['price'] * item['quantity'], item['quantity']))
                connection.commit()  # Commit after insert

                # Update monthly_spending table (if a record exists, update total_spent, total_items for the given month and bill_id)
                cursor.execute("""
                    INSERT INTO monthly_spending (customer_mobile, category, total_spent, total_items, bill_date, bill_id)
                    VALUES (?, ?, ?, ?, ?, ?)
                    ON CONFLICT(customer_mobile, category, bill_date, bill_id) DO UPDATE SET 
                        total_spent = total_spent + ?, 
                        total_items = total_items + ?
                """, (customer_mob, category_name, item['price'] * item['quantity'], item['quantity'], current_month, bill_id,
                    item['price'] * item['quantity'], item['quantity']))
                connection.commit()  # Commit after insert

                # Update the item_purchase_history table to track purchased items

                # Update the item_purchase_history table to track purchased items
                cursor.execute("""
                    INSERT INTO item_purchase_history (customer_mobile, item_name, quantity, bill_id, price)
                    VALUES (?, ?, ?, ?, ?)
                    ON CONFLICT(customer_mobile, item_name, bill_id) DO UPDATE SET
                        quantity = quantity + excluded.quantity
                """, (customer_mob, item['name'], item['quantity'], bill_id, item['price']))

                # Commit the changes to item_purchase_history
                connection.commit()

                # Step 2: Calculate the top 5 purchased items based on cumulative quantity (from the start)
                cursor.execute("""
                    SELECT item_name, SUM(quantity) AS total_quantity
                    FROM item_purchase_history
                    WHERE customer_mobile = ?
                    GROUP BY item_name
                    ORDER BY total_quantity DESC
                    LIMIT 5
                """, (customer_mob,))

                # Fetch the top 5 items
                top_items = cursor.fetchall()

                # Step 3: Insert or update the top 5 items into the top_items table
                for item in top_items:
                    cursor.execute("""
                        INSERT INTO top_items (customer_mobile, item_name, total_quantity)
                        VALUES (?, ?, ?)
                        ON CONFLICT(customer_mobile, item_name) DO UPDATE SET
                            total_quantity = excluded.total_quantity
                    """, (customer_mob, item[0], item[1]))

                # Commit the changes to the top_items table
                connection.commit()

                # Now the top_items table will have the latest top 5 items for that customer

    

    
        # Commit the changes and close the connection
        connection.commit()
        cursor.close()  # Close the cursor
    
# -----------------------------------------------------------------------------------------------------------------

    # For Monthly Spendings Graph using Matplotlib

    def view_monthly_spendings(self):
        self.cursor.execute("""
            SELECT category, SUM(total_spent) AS total_spent
            FROM monthly_spending
            WHERE customer_mobile = ?
            GROUP BY category
            """, (self.phone,))
        results = self.cursor.fetchall()

        if not results:
            print("No monthly spending data found.")
            return

        categories = [row[0] for row in results]
        total_spent = [row[1] for row in results]

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.bar(categories, total_spent, color='skyblue')
        plt.title(f"Monthly Spending by Category ({datetime.now().strftime('%B %Y')})", fontsize=16)
        plt.xlabel("Category", fontsize=12)
        plt.ylabel("Total Spent (₹)", fontsize=12)
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
# -----------------------------------------------------------------------------------------------------------------

    # For Ctegory Wise Spending Graph using Matplotlib
    def view_category_spendings(self):
        self.cursor.execute("""
            SELECT category, SUM(total_spent) AS total_spent
            FROM category_spending
            WHERE customer_mobile = ?
            GROUP BY category
            """, (self.phone,))
        results = self.cursor.fetchall()

        if not results:
            print("No category-wise spending data found.")
            return

        categories = [row[0] for row in results]
        total_spent = [row[1] for row in results]

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.pie(total_spent, labels=categories, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
        plt.title("Category-Wise Spending Distribution", fontsize=16)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.tight_layout()
        plt.show()

# -----------------------------------------------------------------------------------------------------------------

    def view_top_purchased_items(self):
        # Query to fetch the top 5 purchased items from the top_items table
        self.cursor.execute("""
            SELECT item_name, total_quantity
            FROM top_items
            WHERE customer_mobile = ?
            ORDER BY total_quantity DESC
            LIMIT 5
        """, (self.phone,))
        results = self.cursor.fetchall()

        # Check if results exist
        if not results:
            print("No top purchased items found.")
            return

        # Extracting items and their quantities
        items = [row[0] for row in results]
        quantities = [row[1] for row in results]

        # Ensure X-axis scales properly and reflects the full range of data
        max_quantity = max(quantities) if quantities else 0
        min_quantity = min(quantities) if quantities else 0

        # Plotting the bar chart
        plt.figure(figsize=(10, 6))
        bars = plt.barh(items, quantities, color='limegreen', edgecolor='black')
        plt.title("Top 5 Purchased Items", fontsize=16, weight='bold')
        plt.xlabel("Total Quantity Purchased", fontsize=12)
        plt.ylabel("Items", fontsize=12)
        plt.gca().invert_yaxis()  # Invert y-axis for better readability
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.grid(axis='x', linestyle='--', alpha=0.7)

        # Annotate the bar chart with quantities
        for bar, quantity in zip(bars, quantities):
            plt.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height() / 2,
                    f"{quantity}", va='center', ha='left', fontsize=10)

        # Adjust X-axis range dynamically based on maximum quantity
        plt.xlim(0, max_quantity + (max_quantity * 0.2))  # Add 20% buffer

        # Explicitly force the graph to handle larger values if needed
        plt.tight_layout()
        plt.show()

# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
        

# Main Function

def main():
    # Assuming database is initialized and customers are registered
    while True:
        width = os.get_terminal_size().columns

        # The message you want to center
        message = "Welcome to Smart Billing System & Customer Services"

        # Print the message centered
        print("\n" + colored(message.center(width), "yellow", attrs=["bold"]))
        print(colored("\nPlease choose an option:", "green"))
        
        # Display the main menu options in a table
        main_menu = [
            ["1", "Register"],
            ["2", "Login"],
            ["3", "Exit"]
        ]
        
        # Tabulate main menu
        main_menu_table = tabulate(main_menu, tablefmt="fancy_grid", stralign="center")
        print(colored(main_menu_table, "cyan"))

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            phone = input("Enter your phone number: ")
            password = input("Enter your password: ")
            Customer.register(name, phone, password)

        elif choice == "2":
            phone = input("Enter your phone number: ")
            password = input("Enter your password: ")
            customer = Customer.login(phone, password)

            if customer:
                while True:
                    # Customer menu options in a table format
                    customer_menu = [
                        ["1", "View Profile"],
                        ["2", "View Products"],
                        ["3", "Generate Bill"],
                        ["4", "View Past Bills"],
                        ["5", "View Offers [Buy X get X Free !!]"],
                        ["6", "View Smart Coins"],
                        ["7", "View Discount Coupons"],
                        ["8", "Return/Replacement Product"],
                        ["9", "Visualize Your Spending Trends [SMART]"],
                        ["10", "Exit"]
                    ]
                    
                    # Tabulate customer menu
                    customer_menu_table = tabulate(customer_menu, headers=["#", "Option"], tablefmt="fancy_grid", stralign="center")
                    print(colored(customer_menu_table, "magenta"))

                    customer_choice = input("Enter your choice: ")

                    if customer_choice == "1":
                        print(f"Name: {customer.name}, Phone: {customer.phone}, Smart Coins: {customer.smart_coins}")
                    elif customer_choice == "2":
                        customer.view_products()
                    elif customer_choice == "3":
                        customer.generate_bill()
                    elif customer_choice == "4":
                        customer.view_past_bills()
                    elif customer_choice == "5":
                        customer.view_discount_offers()
                    elif customer_choice == "6":
                        customer.view_smart_coins()
                    elif customer_choice == "7":
                        customer.view_coupons()
                    elif customer_choice == "8":
                        customer.request_refund_replacement()
                    elif customer_choice == "9":
                        print("\n" + colored("Spending Trends - Select any that you want to view:", "yellow"))
                        
                        # Spending trend options in a table format
                        trend_menu = [
                            ["1", "View Your Monthly Spendings"],
                            ["2", "View Category-Wise Spendings"],
                            ["3", "View Top 5 Purchased Items"]
                        ]
                        
                        # Tabulate spending trend menu
                        trend_menu_table = tabulate(trend_menu, tablefmt="fancy_grid", stralign="center")
                        print(colored(trend_menu_table, "cyan"))

                        trend_choice = input("Enter your choice: ")

                        if trend_choice == "1":
                            customer.view_monthly_spendings()  # Call the method for monthly spendings
                        elif trend_choice == "2":
                            customer.view_category_spendings()  # Call the method for category-wise spendings
                        elif trend_choice == "3":
                            customer.view_top_purchased_items()  # Call the method for top 5 purchased items
                        else:
                            print("Invalid choice. Returning to the main menu.")
                    elif customer_choice == "10":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice. Please try again.")

        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

main()