#ATM APPLICATION
Total_Amount=100000
card="c"
pwd=1234
user=input("Insert the card:")
password=int(input("Enter the Password:"))
if user==card and pwd==password:
    print("Welcome Jagadeesh")
    while True:
        print("Select Options:\n1.Balance Enquiry\n2.Withdraw")
        option = int(input("Select an option: "))
        if option == 1:
            print("Available Balance:", Total_Amount)

        elif option == 2:
            withdraw_amount = int(input("Enter withdraw amount: "))

            if withdraw_amount <= Total_Amount:
                Total_Amount -= withdraw_amount
                print("Please collect your cash.")
                print("Remaining Account Balance:", Total_Amount)
            else:
                print("Insufficient Balance!")
        else:
            print("Invalid Option. Please try again.")

elif user == card and pwd != password:
    print("Invalid PIN")

elif user != card and pwd == password:
    print("Invalid User")

else:
    print("Invalid User and Invalid PIN")

        

