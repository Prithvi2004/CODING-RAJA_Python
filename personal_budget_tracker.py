import json
import os

class Transaction:
    def __init__(self, amount, category, transaction_type):
        self.amount = amount
        self.category = category
        self.transaction_type = transaction_type

    def __repr__(self):
        return f"Type: {self.transaction_type}, Category: {self.category}, Amount: {self.amount}"

class BudgetTracker:
    def __init__(self, filename):
        self.filename = filename
        self.transactions = []
        self.load_transactions()

    def load_transactions(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                for trans_data in data:
                    transaction = Transaction(**trans_data)
                    self.transactions.append(transaction)

    def save_transactions(self):
        with open(self.filename, 'w') as f:
            data = [trans.__dict__ for trans in self.transactions]
            json.dump(data, f, indent=4)

    def add_transaction(self, amount, category, transaction_type):
        transaction = Transaction(amount, category, transaction_type)
        self.transactions.append(transaction)
        self.save_transactions()

    def calculate_budget(self):
        income = sum(trans.amount for trans in self.transactions if trans.transaction_type == 'income')
        expenses = sum(trans.amount for trans in self.transactions if trans.transaction_type == 'expense')
        remaining_budget = income - expenses
        return remaining_budget

    def analyze_expenses(self):
        expense_categories = {}
        for trans in self.transactions:
            if trans.transaction_type == 'expense':
                if trans.category in expense_categories:
                    expense_categories[trans.category] += trans.amount
                else:
                    expense_categories[trans.category] = trans.amount
        return expense_categories

    def display_transactions(self):
        print("------ TRANSACTION HISTORY ------")
        for trans in self.transactions:
            print(trans)
        print("---------------------------------")

def main():
    budget_tracker = BudgetTracker("transactions.json")

    while True:
        print("\n1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Remaining Budget")
        print("4. Analyze Expenses")
        print("5. View Transaction History")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            category = input("Enter income category: ")
            budget_tracker.add_transaction(amount, category, 'income')
        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            budget_tracker.add_transaction(amount, category, 'expense')
        elif choice == '3':
            remaining_budget = budget_tracker.calculate_budget()
            print(f"Remaining Budget: {remaining_budget}")
        elif choice == '4':
            expense_categories = budget_tracker.analyze_expenses()
            print("------ EXPENSE ANALYSIS ------")
            for category, amount in expense_categories.items():
                print(f"{category}: {amount}")
            print("---------------------------------")
        elif choice == '5':
            budget_tracker.display_transactions()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
