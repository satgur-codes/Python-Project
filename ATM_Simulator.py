#ATM_Simulator
correct_pin = "1234"
balance = 10000
attempts = 3
is_authenticated = False

while attempts > 0:
  pin = input("Enter PIN: ")
  if pin == correct_pin:
    is_authenticated = True
    break
  else:
    attempts -= 1
    if attempts > 0:
      print("You Entered Wrong PIN. Attempts left:", attempts)
    else:
      print("Card blocked.")

if is_authenticated:
  history = []

  while True:
    print("\n1. Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Select an option: ")

    if choice == "1":
      print("Balance:", balance)

    elif choice == "2":
      amount = int(input("Enter amount to deposit: "))
      if amount > 0:
        balance += amount
        print("New balance:", balance)
        history.append(f"Deposit -> {amount}")
      else:
        print("Amount must be above 0")

    elif choice == "3":
      amount = int(input("Enter amount to withdraw: "))
      if amount <= balance:
        balance -= amount
        print("New balance:", balance)
        history.append(f"Withdraw -> {amount}")
      else:
        print("Insufficient balance")

    elif choice == "4":
      print("Thank you! for using our program")
      for transaction in history:
        print(transaction)
      break
    else:
      print("Invalid choice, Please try again...")
