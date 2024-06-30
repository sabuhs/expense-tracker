from expense import Expense

def main():
    print(f"Running Expense Tracker!")
    expense_file_path = "expenses.csv"
    # Get user input for expense.
    # expense = get_user_expense()
    
    # # Write their expense to a file.
    # save_expense_to_file(expense, expense_file_path)

    # # Read file and summarize expense.
    summarize_expense(expense_file_path)
    pass

def get_user_expense():
    print(f"<-- Getting User Expense -->")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    print(f"You've entered {expense_name}, {expense_amount}")
    expense_categories = [
        "🍔 Food", "🏨 Accommodation", "🚕 Transport", "👽 Misc"
    ]
    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f" {i + 1}. {category_name}")
        value_range = f"[1 - {len(expense_categories)}]"
        try:
            selected_index = int(input(f"Enter a category number: {value_range}")) - 1
            
            if selected_index in range(len(expense_categories)):
                print(f"Selected category: {expense_categories[selected_index]}")
                selected_category = expense_categories[selected_index]
                new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount )
                return new_expense
            else:
                print("Invalid Category. Please try again!")
        except Exception:
            print(f"Invalid input: {selected_index} is not a number")
        
def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"Saving Expense to a File: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

def summarize_expense(expense_file_path):
    print(f"Summarizing Expense: {expense_file_path}")
    expenses = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense(name=expense_name, amount=float(expense_amount), category=expense_category)
            print(line_expense)
            expenses.append(line_expense)
        print(expenses)
if __name__ == "__main__":
    main()