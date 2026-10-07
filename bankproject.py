import json
import random
import os

print(os.getcwd())
with open("accounts.json", "r") as file:
    data = json.load(file)

class Account:
    def CreateAccount(self):
        historyarray = []
        self.Name = input("enter your name : ")

        self.Age = int(input("enter your age : "))
        while self.Age < 18:
            print("not eligible write again")
            self.Age = int(input("enter your age : "))

        self.__cnic = input("enter valid cnic")
        found  = False
        while found == False:
            for a in data:
                if a["Cnic"] == self.__cnic:
                    found  = True
                    break
            if found:
                print("already exists")
                self.__cnic = input("enter again")
                found = False
            else:
                break
                
                
        self.PhoneNumber = int(input("enter valid number :"))

        self.__pin = input("enter 4 digit pin :")
        while len(self.__pin) < 4 or len(self.__pin) > 4 or not self.__pin.isdigit():
            print("pin should be of 4 numbers")
            self.__pin = input("enter 4 digit pin :")

        self.InitialDeposit = int(input("enter initial deposit :"))
        while self.InitialDeposit < 0:
            print("should be greater then 0")
            self.InitialDeposit = int(input("enter initial deposit :"))
        historyarray.append(f" first deposit : {self.InitialDeposit}")

        accnumber = random.randint(1000, 9999)
        flag = True

        while flag:
            flag = False
            for b in data:
                if b["accountnumber"] == accnumber:
                    flag = True
                    break
            if flag:
                accnumber = random.randint(1000, 9999)
        print(f"account number is {accnumber}")

        accountdata = {
            "Name" : self.Name,
            "accountnumber" : accnumber,
            "Age" : self.Age,
            "Pin" : self.__pin,
            "Phone" : self.PhoneNumber,
            "Cnic" : self.__cnic,
            "InitialDeposit" : self.InitialDeposit,
            "Balance" : self.InitialDeposit,
            "History" : historyarray
        }
        data.append(accountdata)
        with open("accounts.json", "w") as file:
            json.dump(data, file, indent=4)

    def loginaccount(self):
        accnum = int(input("enter your account number"))
        found = False
        ispin = False
        while found == False:
            for accounts in data:
                if accounts["accountnumber"] == accnum:
                    for i in range(3):
                        accpin = input("enter pin")
                        if accounts["Pin"] == accpin:
                            print("Login successfully")
                            username = accounts["Name"]
                            print(f"welcome {username}")
                            ispin = True
                            break
                        else:
                            print("wrong pin !")
                    else:
                        print("pin wrong only 3 attempts")
                    found = True
                    break
            if not found:
                print("wrong account number")
                break
        while ispin:
            print(f"welcome to account menu {username} !")
            print(" press : \n 1 for check balance \n 2 for deposit \n 3 for withdraw \n 4 for transaction history \n 5 for acc info \n 6 for transfer money \n 7 for pin change\n 8 for logout \n 9 for deleting the account")
            choice = int(input("enter your choice :"))
            if choice ==1:
                print(f"your current balance is {accounts['Balance']}")
            elif choice == 2:
                amount = int(input("enter amount to deposit"))
                while amount <=0:
                    print("wrong amount")
                    amount = int(input("enter again"))
                else:
                    accounts["Balance"] = accounts["Balance"] + amount
                    print("Amount deposited")
                    print(f"Your current balance is {accounts['Balance']}")
                    accounts["History"].append(f"deposit : {amount}")
                    with open("accounts.json", "w") as file:
                        json.dump(data, file, indent=4)
            elif choice == 3:
                withdrawamount = int(input("enter amount to withdraw"))
                while withdrawamount <=0 or withdrawamount > accounts["Balance"]:
                    print("Invalid amount")
                    withdrawamount = int(input("enter amount to withdraw again"))
                else:
                    accounts["Balance"] = accounts["Balance"] - withdrawamount
                    print(f"successfully withdrawn {withdrawamount} ")
                    print(f"your current balance is {accounts['Balance']}")
                    accounts["History"].append(f"withdraw : {withdrawamount}")
                    with open("accounts.json", "w") as file:
                        json.dump(data, file, indent=4) 
            elif choice == 4:
                for histories in accounts["History"]:
                    print(histories)
            elif choice ==5:
                print(f"your account info is : \n name : {accounts["Name"]} \n account number : {accounts["accountnumber"]} \n age : {accounts["Age"]}  \n phone :  {accounts["Phone"]} \n cnic : {accounts["Cnic"]}  \n current balance is : {accounts["Balance"]}" )
            elif choice == 6:
                num = int(input("enter reciepent accout number"))
                found = False
                for account in data:
                    if account["accountnumber"] == num and account["accountnumber"] != accounts["accountnumber"]:
                        money = int(input("how much u want to transfer"))
                        if money <= 0 :
                            print("wrong input")
                        elif money > accounts["Balance"]:
                            print("insuffient amount to transfer")
                        else:
                            # accounts is dictationary of sender
                            accounts["Balance"] = accounts["Balance"] - money
                            account["Balance"] = account["Balance"] + money
                            accounts["History"].append(f"send : {money}")
                            account["History"].append(f"recieved : {money}")
                            print(f"your current balance is {accounts["Balance"]}")
                            found = True
                            with open("accounts.json", "w") as file:
                                json.dump(data, file, indent=4)
                            break
                if not found:
                    print("wrong account number")
            elif choice == 7 :
                currentpin = input("enter your current pin")
                if currentpin == accounts["Pin"]:
                    newpin = input("enter new pin")
                    while len(newpin) != 4 or not newpin.isdigit():
                        print("pin should be of 4 numbers")
                        newpin = input("enter pin again")
                    newpin2 = input("enter pin again to confirm")
                    if newpin2 != newpin:
                        print("both pin doesnt match ")
                    else:
                        accounts["Pin"] = newpin
                        print("pin updated successfully")
                        with open("accounts.json", "w") as file:
                            json.dump(data, file, indent=4)
                else:
                    print("wrong pin")
            elif choice == 8:
                print("logged out")
                ispin = False
            elif choice == 9 :
                repin = input("enter your pin again to delete account")
                if repin == accounts["Pin"]:
                    deletechoice = input("Are you sure you want to delete your account? (yes/no")
                    if deletechoice.lower() == "yes":
                        data.remove(accounts)
                        with open("accounts.json", "w") as file:
                            json.dump(data, file, indent=4)
                        print("account removed successfully")
                        ispin = False
                else:
                    print("wrong pin")
            else:
                print("wrong choice")


while True:
    print(":: BANK MANAGEMENT SYSTEM ::")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choices = int(input("Enter choice: "))
    if choices == 1:
        user = Account()
        user.CreateAccount()
    elif choices == 2:
        user = Account()
        user.loginaccount()
    elif choices == 3 :
        print('logged out')
        break
    else:
        print("wrong choice")


