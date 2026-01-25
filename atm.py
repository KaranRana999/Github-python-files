<<<<<<< HEAD
print('--Welcome to SBI--')
name = str(input("Enter your name: "))
balance= 5000
pin = 1234
tries = 3
while tries >0:
    entered_pin = int(input("Enter your pin:"))
    if entered_pin== pin:
        print(f"\nHello {name} , Logged in succcessfully")
        break

    else:
        print("Wrong pin entered, Enter correct pin")
        tries-=1 

if tries ==0:
    print("Tooo many unsuccessful attempt, Card blocked. Contact bank for more information")
else:
            

                

            def check_balance():
                global balance
                print(f" Your balance is {balance}")


            def withdraw():
                global balance
                withdrawal = int(input("Enter the amount: "))
                
                
                if withdrawal  <=0:
                    print("Enter valid amount") 
                elif withdrawal > balance:
                    print("Insufficient Funds")
                else:
                    balance -=withdrawal
                    print(f"Your Balance = {balance}")

            def deposit():
                global balance
                deposit = int(input("Enter the amount: "))
                if deposit<=0:
                    print("Enter valid Amount")
                else:
                    balance += deposit
                print(f"Your balance = {balance}")
            def exit_atm():
                    print("Thank You for using SBI ATM")

                    
                
            while True:
                print(" \nHow may we help you?")
                print("1. Check Balance")
                print("2. Withdraw money")
                print("3. Deposit money")
                print("4. Exit")
                
                choice = int(input())
                

                if choice == 1:
                    check_balance()
                elif choice == 2:
                    withdraw()
                elif choice == 3:
                    deposit()
                elif choice == 4:
                    exit_atm()
                    break
                
                else: 
                    print("Invalid Operation Entered")




=======
print('--Welcome to SBI--')
name = str(input("Enter your name: "))
balance= 5000
pin = 1234
tries = 3
while tries >0:
    entered_pin = int(input("Enter your pin:"))
    if entered_pin== pin:
        print(f"\nHello {name} , Logged in succcessfully")
        break

    else:
        print("Wrong pin entered, Enter correct pin")
        tries-=1 

if tries ==0:
    print("Tooo many unsuccessful attempt, Card blocked. Contact bank for more information")
else:
            

                

            def check_balance():
                global balance
                print(f" Your balance is {balance}")


            def withdraw():
                global balance
                withdrawal = int(input("Enter the amount: "))
                
                
                if withdrawal  <=0:
                    print("Enter valid amount") 
                elif withdrawal > balance:
                    print("Insufficient Funds")
                else:
                    balance -=withdrawal
                    print(f"Your Balance = {balance}")

            def deposit():
                global balance
                deposit = int(input("Enter the amount: "))
                if deposit<=0:
                    print("Enter valid Amount")
                else:
                    balance += deposit
                print(f"Your balance = {balance}")
            def exit_atm():
                    print("Thank You for using SBI ATM")

                    
                
            while True:
                print(" \nHow may we help you?")
                print("1. Check Balance")
                print("2. Withdraw money")
                print("3. Deposit money")
                print("4. Exit")
                
                choice = int(input())
                

                if choice == 1:
                    check_balance()
                elif choice == 2:
                    withdraw()
                elif choice == 3:
                    deposit()
                elif choice == 4:
                    exit_atm()
                    break
                
                else: 
                    print("Invalid Operation Entered")




>>>>>>> d4ead5f17bbbf74dfb44aa4be1b6b78fc25ff521
