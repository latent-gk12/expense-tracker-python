from expense import Expense
from tracker import ExpenseTracker
tracker = ExpenseTracker() ## made a object . 

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter Choice: ")


    if choice=="3":
        print("Thank You")
        break
    elif choice == "2":
        tracker.view_expenses()
    elif choice == "1":
        amount = input("Enter Amount: ")
        category = input("Enter Category: ")
        description = input("Enter Description: ")
        date = input("Enter Date (YYYY-MM-DD): ")

        ## create the object
        expense = Expense(
            amount,
            category,
            description,
            date
        )
        ## add it to the tracker
        tracker.add_expense(expense)

        print("Expense Added Successfully")
