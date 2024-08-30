net_amount = 0

print("Enter transactions in the format 'D 100' for deposits or 'W 200' for withdrawals.")
print("Type 'done' to finish.")

while True:
    transaction = input("Enter transaction: ")
    
    if transaction.lower() == 'done':
        break
    
    parts = transaction.split()
    
    if len(parts) != 2:
        print("Invalid format. Please enter in the format 'D 100' or 'W 200'.")
        continue

    action, amount_str = parts
    
    try:
        amount = float(amount_str)
        if action == 'D':
            net_amount += amount
        elif action == 'W':
            net_amount -= amount
        else:
            print("Invalid action. Use 'D' for deposit and 'W' for withdrawal.")
    except ValueError:
        print("Invalid amount. Please enter a valid number.")

print(f"Net amount in the account: ${net_amount:.2f}")
