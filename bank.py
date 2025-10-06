def update_balance():
    initial_balance = float(input("Enter initial balance: "))
    deposit = float(input("Enter deposit amount: "))
    updated_balance = initial_balance + deposit
    print(f"Balance after deposit: {updated_balance}")

    withdrawal = float(input("Enter withdrawal amount: "))
    if withdrawal > updated_balance:
        print("Insufficient funds! Withdrawal denied.")
    else:
        updated_balance -= withdrawal
        print(f"Balance after withdrawal: {updated_balance}")

update_balance()
