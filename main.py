import os
import sys

while True:
    print("\nWelcome to the Store Management System")
    print("1) Store Manager")
    print("2) Customer")
    print("3) Exit")
    
    choice = input("Enter your choice (1/2/3): ").strip()
    
    if choice == '1':
        print("\nRedirecting to the Store Manager section...")
        os.system("python store_manager.py")  
    
    elif choice == '2':
        print("\nRedirecting to the Customer section...")
        os.system("python ./customer.py")    

    elif choice == '3':
        print("Exiting the system. Thank you!")
        sys.exit(0)
    
    else:
        print("Invalid choice. Please try again.")