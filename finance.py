import csv


while True:
    entry = input("Income or Expense? ")
    if entry.lower() == "Income":
        entry = "Income"
        category.lower() = input("Salary, Giftings, Savings, Investments? ")
        if category in ["Salary", "Giftings", "Savings", "Investments"]:
            amount = int(input("Amount: "))
            if amount > 0:
                pass
            else:
                print("Invalid Amount")
        else:
            print("Invalid Category")
        try:
            with open("finance.csv", "a") as f:
                header = ["Type", "Category", "Amount"]
                file = csv.DictWriter(f, fieldnames=header)
                file.writerow({"Type": entry, "Category": category, "Amount": amount})

        except FileNotFoundError:
            with open("finance.csv", "w") as f:
                header = ["Type", "Category", "Amount"]
                file = csv.DictWriter(f, fieldnames=header)
                file.writeheader()
                file.writerow({"Type": entry, "Category": category, "Amount": amount})
    

        

    elif entry.lower() == "Expense":
        entry = "Expense"
        category.lower() = input("Food, Rent, Fees, Miscellanous ")
        if category in ["Food", "Rent", "Fees", "Miscellanous"]:
            category = category
        else:
            print("Invalid Category")
        amount = int(input("Amount: "))   
        if amount > 0:
            pass
        else:
            print("Invalid Amount")

        try:
            with open("finance.csv", "a") as f:
                header = ["Type", "Category", "Amount"]
                file = csv.DictWriter(f, fieldnames=header)
                file.writerow({"Type": entry, "Category": category, "Amount": amount})

        except FileNotFoundError:
            with open("finance.csv", "w") as f:
                header = ["Type", "Category", "Amount"]
                file = csv.DictWriter(f, fieldnames=header)
                file.writeheader()
                file.writerow({"Type": entry, "Category": category, "Amount": amount})

        
    elif entry.lower() == "quit": 
        print("Goodbye!")
        break
    
    else:
        print("Invalid — type Income, Expense or Quit")


inc = []
exp = []

try :

    with open("finance.csv") as f:
        for file in csv.DictReader(f):
            if file["Type"] == "Income":
                inc.append(int(file["Amount"]))
            else:
                exp.append(int(file["Amount"]))
    income_total = sum(inc)
    expenses_total = sum(exp)
    Net = income_total - expenses_total
    print(Net)
    # #  Spendings by category
    row = []
    with open("finance.csv") as f:
        for file in csv.DictReader(f):
            if file["Type"] == "Expense":
                # print(file["Category"])
                row.append(file)
    # for sor in row:
    #     if (sor["Type"]) == "Expense":
    #         print(f'{sor["Category"]} : {sor["Amount"]}')

    # Top 5 biggest spending
    expenses = []
    for expense in row:
        if expense["Type"] == "Expense":
            expenses.append(expense)    
    biggest = sorted(expenses, key=lambda x: int(x["Amount"]), reverse=True)
    biggest = biggest[:5]
    print("Top 5 biggest spendings:")
    for item in biggest:
        print(f"{item['Category']}: ${item['Amount']}")
    spend_cate= {}
    for spend in row:
        if spend["Type"] == "Expense":
            if spend["Category"] in spend_cate:
                spend_cate[spend["Category"]] += int(spend["Amount"])
            else:
                spend_cate[spend["Category"]] = int(spend["Amount"])
    for cater, total in spend_cate.items():
        print(f'{cater} : ${total}')
except FileNotFoundError:
    print("No entries found.")

# Spending by category






