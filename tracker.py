import csv
from expense import Expense
class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_expenses()
    def add_expense(self,expense):
        self.expenses.append(expense)
        self.save_expense(expense)
    ## New feature for showing Expenses
    def view_expenses(self):
        for expense in self.expenses:
            print("   ")
            print("-" * 30)
            print(expense.amount)
            print(expense.category)
            print(expense.description)
            print(expense.date)
            print("-" * 30)


    def save_expense(self, expense):

        with open("expenses.csv", "a" , newline = "") as file:
            writer = csv.writer(file)
            writer.writerow(
                        [expense.amount,
                        expense.category,
                        expense.description,
                        expense.date]
            )

    def load_expenses(self):
        with open("expenses.csv","r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if not row:
                    continue
                
                expense = Expense(
                    row[0],
                    row[1],
                    row[2],
                    row[3]
                )
                self.expenses.append(expense)