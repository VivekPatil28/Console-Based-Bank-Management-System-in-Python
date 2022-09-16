'''
    Bank Management Project in Python
    With some basic and some important functionalities
    
    1) Creating Account
    2) 
'''

import os


class Account():

    accounts = []

    @classmethod
    def validate(cls):
        try:
            print("Enter your Account Number ", end='')
            acno = GetNumber()
            print("Enter your Pin ", end='')
            pin = GetNumber()
            for account in cls.accounts:
                if (account.acno == acno and account.pin == pin):
                    print("Validation Successful")
                    print(
                        "------------------------------------------------------------------")
                    return account
            else:
                print("Account Not Found")
                return -1
        except NameError:
            print(NameError)

    def __init__(self) -> None:
        self.name = input("Enter Name ").strip().title()
        self.acno = int(input("Enter Acno "))
        self.pin = int(input("Enter Pin "))
        self.security_question = self.securityQuestion()
        self.security_question_answer = self.securityQuestionAnswer()
        self.balance = 0
        Account.accounts.append(self)
        print("Account Was Created Successfully")

    def showAccount(self):
        print("------------------------------------------------------------------")
        print("Name                     = ", self.name)
        print("Account Number           = ", self.acno)
        print("Pin                      = ", self.pin)
        print("Security Question        = ", self.security_question)
        print("Security Question Answer = ", self.security_question_answer)
        print("Account Balance          = ", self.humanizeAmount())
        print("------------------------------------------------------------------")

    # Humanize the Account Balance with Commas (,)

    def humanizeAmount(self):
        num = ''
        stri = str(self.balance)[::-1]
        for i in range(len(stri)):
            if i >= 3:
                if i % 2 != 0:
                    num += ','
            num += stri[i]
        return num[::-1]

    #  Function to Greet the Account Owner When he login

    def greet(self):
        print("Hello", self.name)

    def checkBalance(self):
        self.greet()
        print("Your Available Balance is ", self.humanizeAmount())

    def deposit(self):
        self.greet()
        print("Enter Amount to Deposit ")
        self.balance += GetNumber()
        print("Amount Deposited SuccessFully")
        print("Current Balance =", self.humanizeAmount())

    def withdraw(self):
        self.greet()
        print("Enter Amount to Withdraw ")
        d = GetNumber()
        if (d < self.balance):
            self.balance -= d
            print("withdrawal Successful")
            print("Current Balance =", self.humanizeAmount())
        else:
            print("Not Enough Money to Withdraw")

    def transferMoney(self):
        print("Enter Reciver Account Number ")
        rnum = GetNumber()
        for account in Account.accounts:
            if account.acno == rnum:
                print("Validation Successful")
                print(
                    "------------------------------------------------------------------")
                print("Enter the Transfer Amount ")
                samount = GetNumber()
                if self.balance >= samount:
                    self.balance -= samount
                    account.balance += samount
                else:
                    print("Not enough Balance to Transfer")
                print("Transfer Successful !!! ")
                print(
                    "------------------------------------------------------------------")
                break
        else:
            print("Account Not Found")

    def changePin(self):
        print("Enter your Account Number ", end='')
        acno = GetNumber()
        print("Enter -0000 if you forget your pin")
        print("Enter your Pin ")
        pin = GetNumber()
        if (pin == -0000):
            for account in Account.accounts:
                if (account.acno == acno):
                    print(account.security_question)
                    ans = input()
                    if (ans == account.security_question_answer):
                        print(
                            "------------------------------------------------------------------")
                        print("Validated")
                        print(
                            "------------------------------------------------------------------")
                        print("Enter your New PIN ", end='')
                        newPin = GetNumber()
                        if (account.pin != newPin):
                            account.pin = newPin
                            print("Pin Changed Successfully")
                        else:
                            print("Please Enter a Different Pin")
                    break
            else:
                print("Account not found")
        else:
            for account in Account.accounts:
                if (account.pin == acno and account.pin == pin):
                    print("Enter your New PIN ", end='')
                    newPin = GetNumber()
                    if (account.pin != newPin):
                        account.pin = newPin
                        print("Pin Changed Successfully")
                    else:
                        print("Please Enter a Different Password")
                    break
            else:
                print("Account not Found")

    def securityQuestion(self):
        print("------------------------------------------------------------------")
        print("1) What is the name of one of your teacher ?\n2) What is the name of your favourite Resturant ?\n3) In what city did you meet your first partner ?\n4) What is your childhood nickname ?\n5)Add your Custom Question")
        print("------------------------------------------------------------------")
        print("Enter your choice ", end='')
        choice = GetNumber()
        match choice:
            case 1:
                return "What is the name of one of your teacher ?"
            case 2:
                return "What is the name of your favourite Resturant ?"
            case 3:
                return "In what city did you meet your first partner ?"
            case 4:
                return "What is your childhood nickname ?"
            case 5:
                return input("Enter your custom question \n")

    def securityQuestionAnswer(self):
        print("------------------------------------------------------------------")
        print(self.security_question)
        sa = input()
        print("------------------------------------------------------------------")
        return sa

    def __str__(self) -> str:
        return str(self.acno)


# Get Number Function to Get a Valid Number
def GetNumber():
    while True:
        try:
            x = int(input())
            return x
        except ValueError:
            print("Oops! That was not a valid number Try again...")


# Driver Code
choice = ""

while(choice != 0):
    os.system('cls')    # To Clear the Console

    print("------------------------- Welcome to MGB -------------------------")
    # Options to select
    print("1) Create Account \n2) Deposit \n3) Withdraw \n4) View Balance\n5) Change pin\n6) Show Account \n7) Transfer Money \n0) For Exit")
    print("------------------------------------------------------------------")
    print("Enter your choice ", end='')
    choice = GetNumber()
    match choice:
        case 1:
            print("------------------------------------------------------------------")
            a = Account()
            print("------------------------------------------------------------------")
        case 2:
            print("------------------------------------------------------------------")
            a = Account.validate()
            if (a != -1):
                a.deposit()
            print("------------------------------------------------------------------")
        case 3:
            print("------------------------------------------------------------------")
            a = Account.validate()
            if (a != -1):
                a.withdraw()
            print("------------------------------------------------------------------")
        case 4:
            print("------------------------------------------------------------------")
            a = Account.validate()
            if (a != -1):
                a.checkBalance()
            print("------------------------------------------------------------------")
        case 5:
            print("------------------------------------------------------------------")
            a.changePin()
            print("------------------------------------------------------------------")
        case 6:
            print("------------------------------------------------------------------")
            a = Account.validate()
            if (a != -1):
                a.showAccount()
            print("------------------------------------------------------------------")
        case 7:
            print("------------------------------------------------------------------")
            a = Account.validate()
            if (a != -1):
                a.transferMoney()
            print("------------------------------------------------------------------")

        case 0:
            print("------------------------------------------------------------------")
            print("                  good bye !! Visit Again !!")
            print("------------------------------------------------------------------")
        case _:
            print("Please Enter a Valid Choice")
    input("Please Enter to Continue")
