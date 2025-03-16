import db
from business import Transaction
from datetime import datetime

transactions = []

# Function to display separator
def display_separator():
    print("*******************************************************************")

# Function to display title
def display_title():
    print("                       Personal Finance Tracker")
    print()

# Function to display menu
def display_menu():
    print("MENU OPTIONS")
    print("1 - View all transactions")
    print("2 - View transactions by type")
    print("3 - Add a transaction")
    print("4 - Edit a transaction")
    print("5 - Delete a transaction")
    print("6 - Exit program")
    print()

# Function to view all transactions
def view_all_transactions(transactions):
    # Refresh transactions in memory
    transactions[:] = db.view_all_transactions()
    
    if len(transactions) == 0:
        print("No transactions to view.\n")
    else:
        total = 0
        print(f"{'ID'}\t{'Date'}\t\t{'Type'}\t\t{'Description'}\t\t{'Amount'}")

        for num, transaction in enumerate(transactions, start=1):
              transaction_id = transaction.transaction_id
              date = datetime.strptime(transaction.date,'%Y-%m-%d').strftime('%m-%d-%Y')
              type_ = transaction.type_
              description = transaction.description
              amount = transaction.amount

              total += amount

              print(f"{transaction_id}\t{date}\t{type_}\t\t{description}\t\t${amount:,.2f}")
              
        print(f"\t\t\t\t\t\t\tTotal:\t${total:,.2f}\n")
        print()

# Function to view by type
def view_by_type(transactions):
    while True:
        type_ = input("Enter the transaction type (Income/Expense): ").capitalize()
        if type_ in ['Income', 'Expense']:
            break
        else:
            print("Invalid input. Please enter 'Income' or 'Expense'.")

    
    filtered_transactions = db.get_by_transaction_type(type_)

    total = 0

    print(f"{'ID'}\t{'Date'}\t\t{'Type'}\t\t{'Description'}\t\t{'Amount'}")

    for transaction in filtered_transactions:
        transaction_id = transaction[0]
        date = transaction[1]
        type_ = transaction[2]
        description = transaction[3]
        amount = transaction[4]

        total += amount

        print(f"{transaction_id}\t{date}\t{type_}\t\t{description}\t\t${amount:,.2f}")
    
    print(f"\t\t\t\t\t\t\tTotal:\t${total:,.2f}\n")
    print()
    
# Function to add a transaction
def add_transaction_ui():
    global transactions
    
    # Validate date input
    while True:
        date_input = input("Enter the transaction date (MM-DD-YYYY): ")
        try:
            date=datetime.strptime(date_input, '%m-%d-%Y').date()
            break
        except ValueError:
            print("Invalid date format. Please enter the date in MM-DD-YYYY format.")

    # Validate type input        
    while True:
        type_ = input("Enter the transaction type (Income/Expense): ").capitalize()
        if type_ in ['Income', 'Expense']:
            break
        else:
            print("Invalid type. Please enter 'Income' or 'Expense'.")
            
    description = input("Enter a description of the transaction: ")

    # Validate amount input
    while True:
        try:
            amount = float(input("Enter the transaction amount: $"))
            if type_ == "Expense":
                amount = -abs(amount)
            break
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    # Add transaction to the database
    transaction_id = db.add_transaction(date, type_, description, amount)
    
    # Create the transaction object
    transaction = Transaction(transaction_id, date, type_, description, amount)

    # Print confirmation message  
    print(f"Transaction #{transaction_id} in the amount of ${amount} has been added.")
    print()

    # Refresh transactions in memory
    transactions[:] = db.view_all_transactions()

# Function to edit transaction
def edit_transaction_ui(transactions):
    transaction_id = int(input("Enter the transaction ID to edit: "))

    # Find transaction by id
    transaction_to_edit = None
    for transaction in transactions:
        if transaction.transaction_id == transaction_id:
            transaction_to_edit = transaction
            break

    # Check if the transaction exists
    if transaction_to_edit is None:
        print(f"Transaction with ID {transaction_id} not found.")
        return

    # Convert string to date format
    transaction_date = datetime.strptime(transaction_to_edit.date, '%Y-%m-%d').date()

    # Format date
    formatted_date = transaction_date.strftime('%m-%d-%Y')

    # Validate date input
    while True:
        date_input = input(f"Enter new date (current: {formatted_date}): ")
        try:
            date=datetime.strptime(date_input, '%m-%d-%Y').date()
            break
        except ValueError:
            print("Invalid date format. Please enter the date in MM-DD-YYYY format.")

    # Validate type input        
    while True:
        type_ = input(f"Enter new type (current: {transaction_to_edit.type_}): ").capitalize()
        if type_ in ['Income', 'Expense']:
            break
        else:
            print("Invalid type. Please enter 'Income' or 'Expense'.")
            
    description = input(f"Enter new description (current: {transaction_to_edit.description}):")

    # Validate amount input
    while True:
        try:
            amount = float(input(f"Enter new amount (current: ${transaction_to_edit.amount}): $"))
            if type_ == "Expense":
                amount = -abs(amount)
            break
        except ValueError:
                print("Invalid amount. Please enter a valid number.")

    # Update the transaction in the database
    db.edit_transaction(transaction_id, date, type_, description, amount)

    # Refresh transactions in memory
    transactions[:] = db.view_all_transactions()

    # Print confirmation message
    print(f"Transaction #{transaction_id} has been updated.")
    print()
    
# Function to delete a transaction
def delete_transaction_ui(transactions):
    transaction_id = int(input("Enter the transaction ID to delete: "))

    # Find transaction by id
    transaction_to_delete = None
    for transaction in transactions:
        if transaction.transaction_id == transaction_id:
            transaction_to_delete = transaction
            break

    # Check if the transaction exists
    if transaction_to_delete is None:
        print(f"Transaction with ID {transaction_id} not found.")
        return

    # Delete transaction
    db.delete_transaction(transaction_id)

    # Refresh transactions in memory
    transactions[:] = db.view_all_transactions()

    # Print confirmation message
    print(f"Transaction #{transaction_id} has been deleted.")
    print()

# Main function
def main():
    db.connect_db()
    display_separator()
    display_title()
    display_separator()

    # Refresh transactions in memory
    transactions = db.view_all_transactions()

    # Display options menu
    while True:
        display_menu()
        
        option = input("Please enter a menu option: ")
        if option == "1":
            view_all_transactions(transactions)
        elif option == "2":
            view_by_type(transactions)
        elif option == "3":
            add_transaction_ui()
        elif option == "4":
            edit_transaction_ui(transactions)
        elif option == "5":
            delete_transaction_ui(transactions)
        elif option == "6":
            print("Exiting program. Goodbye!")
            db.close()
            break
        else:
            print("Invalid option. Please try again.")
            display_menu()

if __name__ == "__main__":
    main()  # Start the program


