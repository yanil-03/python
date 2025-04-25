expenses = []

def add_expense(date, category, amount):
    expenses.append({'date': date, 'category': category, 'amount': amount})

def show_total():
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total Expense: {total}")

while True:
    try:
        choice = input("1. Add Expense\n2. Show expenses\n3. Show Total\n4. Exit\nEnter choice: ")
    
        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            add_expense(date, category, amount)
        
        elif choice == '2':
            show_total()
        elif choice == '3':
            for items in expenses:
                print(items)
        
        elif choice == '4':
            break

    except ValueError:
        print("Enter a number !!! ")

