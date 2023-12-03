from expense import Expense       # To import the expense class from another file
import calendar                   # library to import calender
from datetime import datetime     # library to import date and time in the code
from colorama import Fore, Back, Style,init  # library to color the output in the terminal

init(autoreset=True)        # To stop the color from leaking.Like to color the next line of output

def main():
    print(f"Rnning expense tracker")
    expense_file_path = "expenses.csv"
    budget = 5000

    
    expense = get_user_expense()      #Get user to input for expense.

    save_expense_to_file(expense, expense_file_path)      #write it inti a file.    
    
    summarize_expenses(expense_file_path,budget)        #read file and summarize expanses.


def get_user_expense():
    print("Getting user expense")
    expense_name=input("Enter expense name: ")
    expense_amount=float(input("Enter expense amount: "))    

    expense_categories= [
        "FOOD",
        "HOME",
        "TICKET",
        "TRAVEL"
        "FUN",
        "MISCELLANEOUS",
    ]
    while True:
        print("Select a category: ")
        for i,category_name in enumerate(expense_categories):
            print(f"{i + 1}. {category_name}")                                        # 1 was added because peple will see the categories starting from 1
        
        value_range =f"[1-{len(expense_categories)}]"                                 # To store the lenth of category list which we will use as range latter.
        
        selected_index = int(input(f"Enter a category {value_range}: ")) - 1          # To store the selected index and because previously we added 1 for user so we have to substract it from here so that our compiler does not assume the index was starting from 1.... 
        
        if selected_index in range(len(expense_categories)):                          # To stop user from giving invalid input.and to declear our range from then length of the category list.
            selected_category = expense_categories[selected_index] 
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return (new_expense)
        else:
            print("Invalid category. Please try again")


def save_expense_to_file(expense, expense_file_path):
    print(f"savivng user expense: {expense} to {expense_file_path}")
    with open(expense_file_path,"a") as f:
        f.write(f"{expense.name}, {expense.amount}, {expense.category}\n")



def summarize_expenses(expense_file_path, budget):
    # print("summarize user expense")
    expenses: list[Expense] = []
    with open(expense_file_path,"r") as f:
        lines = f.readlines()
        for line in lines:
            # striped_line = line.strip()
            expense_name,expense_amount,expense_category = line.strip().split(",")    # Here we used "line.strip().split(",")" in one line..instead of two lines which are "striped_line = line.strip()" and "striped_line.split(",")".
            line_expense = Expense(name=expense_name,amount=float(expense_amount),category=expense_category)

            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] +=expense.amount
        else:
            amount_by_category[key] = expense.amount
    
    print("Expenses By Category :")
    for key, amount in amount_by_category.items():
        print(f"{Fore.BLUE}{key}: ₹{amount:.2f}")                                   # Printing the expenses

    total_spent = sum([x.amount for x in expenses])                                 # Total spending in current month
    print(f"You have spent ₹{total_spent:.2f} this month! ")

    remaining_budget = budget - total_spent                                         # Remaining budget. like how much money is left
    print(f"{Fore.MAGENTA}Budget remaining ₹{remaining_budget:.2f}")
    
    
    
    current_date = datetime.now()                                                        # Get the current date
    days_in_month = calendar.monthrange(current_date.year, current_date.month)[1]        # Get the number of days in the current month
    remaining_days = days_in_month - current_date.day                                    # Calculate the remaining days in the month
    print(f'{Fore.YELLOW}There are {remaining_days} days remaining in the current month.')

    daily_budget = remaining_budget / remaining_days
    print(f"{Fore.CYAN}Budget for the day: ₹{daily_budget:.2f}{Style.RESET_ALL}")



if __name__ == "__main__":
    main()

# In the colorama library in Python, the Fore class provides color constants for foreground text colors, and the Back class provides constants for background colors. Here are some of the color codes:
# Foreground Colors:

# Fore.BLACK
# Fore.RED
# Fore.GREEN
# Fore.YELLOW
# Fore.BLUE
# Fore.MAGENTA
# Fore.CYAN
# Fore.WHITE
# Fore.RESET
# Background Colors:

# Back.BLACK
# Back.RED
# Back.GREEN
# Back.YELLOW
# Back.BLUE
# Back.MAGENTA
# Back.CYAN
# Back.WHITE
# Back.RESET