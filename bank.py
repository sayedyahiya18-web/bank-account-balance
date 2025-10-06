def update_balance():
    initial_balance = float(input("Enter initial balance: "))
    deposit = float(input("Enter deposit amount: "))

    updated_balance = initial_balance + deposit
    print(f"Updated balance: {updated_balance}")

update_balance()