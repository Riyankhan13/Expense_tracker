import csv
import os
from datetime import datetime
from collections import defaultdict

class ExpenseTracker:
    """A personal expense tracker that manages expenses with categories."""
    
    def __init__(self, filename='expenses.csv'):
        """Initialize the expense tracker with a CSV file."""
        self.filename = filename
        self.expenses = []
        self.categories = ['Food', 'Transport', 'Entertainment', 'Utilities', 
                          'Shopping', 'Health', 'Education', 'Other']
        self.load_expenses()
    
    def load_expenses(self):
        """Load expenses from CSV file if it exists."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', newline='') as file:
                    reader = csv.DictReader(file)
                    self.expenses = list(reader)
                print(f"✓ Loaded {len(self.expenses)} expenses from {self.filename}\n")
            except Exception as e:
                print(f"Error loading expenses: {e}\n")
        else:
            print(f"No existing file found. Starting fresh.\n")
    
    def save_expenses(self):
        """Save all expenses to CSV file."""
        if not self.expenses:
            print("No expenses to save.\n")
            return
        
        try:
            with open(self.filename, 'w', newline='') as file:
                fieldnames = ['Date', 'Category', 'Amount', 'Description']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.expenses)
            print(f"✓ Expenses saved to {self.filename}\n")
        except Exception as e:
            print(f"Error saving expenses: {e}\n")
    
    def display_categories(self):
        """Display available expense categories."""
        print("\n📋 Available Categories:")
        for i, category in enumerate(self.categories, 1):
            print(f"  {i}. {category}")
        print()
    
    def add_expense(self):
        """Add a new expense with category, amount, and description."""
        print("\n➕ ADD NEW EXPENSE")
        print("-" * 40)
        
        # Display categories
        self.display_categories()
        
        # Get category
        while True:
            try:
                choice = int(input("Select category (1-8): "))
                if 1 <= choice <= len(self.categories):
                    category = self.categories[choice - 1]
                    break
                else:
                    print("Invalid choice. Please select 1-8.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Get amount
        while True:
            try:
                amount = float(input("Enter amount (₹): "))
                if amount > 0:
                    break
                else:
                    print("Amount must be greater than 0.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Get description
        description = input("Enter description (optional): ").strip()
        if not description:
            description = "No description"
        
        # Get date
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Add to expenses list
        expense = {
            'Date': date,
            'Category': category,
            'Amount': amount,
            'Description': description
        }
        self.expenses.append(expense)
        print(f"✓ Expense added: {category} - ₹{amount}\n")
        
        # Auto-save
        self.save_expenses()
    
    def view_all_expenses(self):
        """Display all recorded expenses."""
        if not self.expenses:
            print("\n📭 No expenses recorded yet.\n")
            return
        
        print("\n📊 ALL EXPENSES")
        print("-" * 90)
        print(f"{'Date':<20} {'Category':<15} {'Amount':<12} {'Description':<30}")
        print("-" * 90)
        
        for expense in self.expenses:
            print(f"{expense['Date']:<20} {expense['Category']:<15} "
                  f"₹{float(expense['Amount']):<11.2f} {expense['Description']:<30}")
        print("-" * 90 + "\n")
    
    def calculate_total_spending(self):
        """Calculate and display total spending."""
        if not self.expenses:
            print("\n💰 No expenses to calculate.\n")
            return
        
        total = sum(float(expense['Amount']) for expense in self.expenses)
        print(f"\n💰 TOTAL SPENDING: ₹{total:.2f}\n")
    
    def calculate_category_wise_spending(self):
        """Calculate and display spending by category."""
        if not self.expenses:
            print("\n📈 No expenses to calculate.\n")
            return
        
        category_spending = defaultdict(float)
        
        for expense in self.expenses:
            category = expense['Category']
            amount = float(expense['Amount'])
            category_spending[category] += amount
        
        print("\n📈 SPENDING BY CATEGORY")
        print("-" * 40)
        
        total = sum(category_spending.values())
        for category in sorted(category_spending.keys()):
            amount = category_spending[category]
            percentage = (amount / total) * 100
            print(f"{category:<15} ₹{amount:<10.2f} ({percentage:.1f}%)")
        
        print("-" * 40)
        print(f"{'TOTAL':<15} ₹{total:.2f}\n")
    
    def display_menu(self):
        """Display the main menu."""
        print("\n" + "=" * 40)
        print("💳 PERSONAL EXPENSE TRACKER")
        print("=" * 40)
        print("1. ➕ Add Expense")
        print("2. 📋 View All Expenses")
        print("3. 💰 Total Spending")
        print("4. 📈 Category-wise Spending")
        print("5. 💾 Save Expenses")
        print("6. 🔄 Load Expenses")
        print("7. ❌ Exit")
        print("=" * 40)
    
    def run(self):
        """Run the expense tracker application."""
        print("\n" + "🎯 Welcome to Personal Expense Tracker! 🎯".center(40))
        
        while True:
            self.display_menu()
            choice = input("Select an option (1-7): ").strip()
            
            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.view_all_expenses()
            elif choice == '3':
                self.calculate_total_spending()
            elif choice == '4':
                self.calculate_category_wise_spending()
            elif choice == '5':
                self.save_expenses()
            elif choice == '6':
                self.load_expenses()
            elif choice == '7':
                print("\n👋 Thank you for using Expense Tracker. Goodbye!\n")
                break
            else:
                print("Invalid choice. Please select 1-7.\n")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()