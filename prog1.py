accounts = {}

def create_account():
    acc = str(1001 + len(accounts))

    name = input("Enter name: ")
    age = int(input("Enter age: "))

    if age < 18:
        print("Age must be 18 or above.")
        return

    phone = input("Enter phone: ")
    address = input("Enter address: ")
    balance = float(input("Enter initial deposit: "))

    if balance < 0:
        print("Invalid amount.")
        return

    accounts[acc] = {
        "name": name,
        "age": age,
        "phone": phone,
        "address": address,
        "balance": balance,
        "transactions": [f"Initial deposit: ₹{balance:.2f}"]
    }

    print("Account created.")
    print("Account number:", acc)

def show_account():
    acc = input("Enter account number: ")

    if acc not in accounts:
        print("Account not found.")
        return

    a = accounts[acc]

    print("\nAccount Number:", acc)
    print("Name:", a["name"])
    print("Age:", a["age"])
    print("Phone:", a["phone"])
    print("Address:", a["address"])
    print("Balance: ₹", f"{a['balance']:.2f}")

def deposit():
    acc = input("Enter account number: ")

    if acc not in accounts:
        print("Account not found.")
        return

    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount.")
        return

    accounts[acc]["balance"] += amount
    accounts[acc]["transactions"].append(
        f"Deposited: ₹{amount:.2f}"
    )

    print("Deposit successful.")

def withdraw():
    acc = input("Enter account number: ")

    if acc not in accounts:
        print("Account not found.")
        return

    amount = float(input("Enter amount: "))

    if amount <= 0 or amount > accounts[acc]["balance"]:
        print("Invalid amount or insufficient balance.")
        return

    accounts[acc]["balance"] -= amount
    accounts[acc]["transactions"].append(
        f"Withdrawn: ₹{amount:.2f}"
    )

    print("Withdrawal successful.")

def transfer():
    sender = input("Sender account: ")
    receiver = input("Receiver account: ")

    if sender not in accounts or receiver not in accounts:
        print("Account not found.")
        return

    if sender == receiver:
        print("Accounts must be different.")
        return

    amount = float(input("Enter amount: "))

    if amount <= 0 or amount > accounts[sender]["balance"]:
        print("Invalid amount or insufficient balance.")
        return

    accounts[sender]["balance"] -= amount
    accounts[receiver]["balance"] += amount

    accounts[sender]["transactions"].append(
        f"Transferred ₹{amount:.2f} to {receiver}"
    )

    accounts[receiver]["transactions"].append(
        f"Received ₹{amount:.2f} from {sender}"
    )

    print("Transfer successful.")

def history():
    acc = input("Enter account number: ")

    if acc not in accounts:
        print("Account not found.")
        return

    print("\nTransaction History:")

    for i, transaction in enumerate(
        accounts[acc]["transactions"], 1
    ):
        print(i, transaction)

def delete_account():
    acc = input("Enter account number: ")

    if acc not in accounts:
        print("Account not found.")
        return

    if accounts[acc]["balance"] != 0:
        print("Withdraw all money before deleting.")
        return

    del accounts[acc]
    print("Account deleted.")

def main():
    while True:
        print("\n===== BANK MANAGEMENT =====")
        print("1. Create Account")
        print("2. Account Details")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer")
        print("6. Transaction History")
        print("7. Delete Account")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            show_account()
        elif choice == "3":
            deposit()
        elif choice == "4":
            withdraw()
        elif choice == "5":
            transfer()
        elif choice == "6":
            history()
        elif choice == "7":
            delete_account()
        elif choice == "8":
            print("Thank you!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()