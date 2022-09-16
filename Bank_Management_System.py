'''
    Bank Management Project in Python
    With some basic and some important functionalities
    
    1) Creating Account
    2) 
'''

import os


class Account():

    __accounts = []

    @classmethod
    def validate(cls):
        try:
            print("Enter your Account Number ", end='')
            acno = GetNumber()
            print("Enter your Pin ", end='')
            pin = GetNumber()
            for account in cls.__accounts:
                if (account.__acno == acno and account.__pin == pin):
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
        self.__name = input("Enter Name ").strip().title()
        self.__acno = int(input("Enter Acno "))
        self.__pin = int(input("Enter Pin "))
        self.__security_question = self.securityQuestion()
        self.__security_question_answer = self.securityQuestionAnswer()
        self.__balance = 0
        Account.__accounts.append(self)
        print("Account Was Created Successfully")

    def showAccount(self):
        print("------------------------------------------------------------------")
        print("Name                     = ", self.__name)
        print("Account Number           = ", self.__acno)
        print("Pin                      = ", self.__pin)
        print("Security Question        = ", self.__security_question)
        print("Security Question Answer = ", self.__security_question_answer)
        print("Account Balance          = ", self.humanizeAmount())
        print("------------------------------------------------------------------")

    # Humanize the Account Balance with Commas (,)

    def humanizeAmount(self):
        num = ''
        stri = str(self.__balance)[::-1]
        for i in range(len(stri)):
            if i >= 3:
                if i % 2 != 0:
                    num += ','
            num += stri[i]
        return num[::-1]

    #  Function to Greet the Account Owner When he login

    def greet(self):
        print("Hello,", self.__name)

    def checkBalance(self):
        print("Your Available Balance is ", self.humanizeAmount())

    def deposit(self):
        print("Enter Amount to Deposit ")
        self.__balance += GetNumber()
        print("Amount Deposited SuccessFully")
        print("Current Balance =", self.humanizeAmount())

    def withdraw(self):
        print("Enter Amount to Withdraw ")
        d = GetNumber()
        if (d < self.__balance):
            self.__balance -= d
            print("withdrawal Successful")
            print("Current Balance =", self.humanizeAmount())
        else:
            print("Not Enough Money to Withdraw")

    def transferMoney(self):
        print("Enter Reciver Account Number ")
        rnum = GetNumber()
        for account in Account.__accounts:
            if account.__acno == rnum:
                print("Validation Successful")
                print(
                    "------------------------------------------------------------------")
                print("Enter the Transfer Amount ")
                samount = GetNumber()
                if self.__balance >= samount:
                    self.__balance -= samount
                    account.__balance += samount
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
            for account in Account.__accounts:
                if (account.__acno == acno):
                    print(account.__security_question)
                    ans = input()
                    if (ans == account.__security_question_answer):
                        print(
                            "------------------------------------------------------------------")
                        print("Validated")
                        print(
                            "------------------------------------------------------------------")
                        print("Enter your New PIN ", end='')
                        newPin = GetNumber()
                        if (account.__pin != newPin):
                            account.__pin = newPin
                            print("Pin Changed Successfully")
                        else:
                            print("Please Enter a Different Pin")
                    break
            else:
                print("Account not found")
        else:
            for account in Account.__accounts:
                if (account.__pin == acno and account.__pin == pin):
                    print("Enter your New PIN ", end='')
                    newPin = GetNumber()
                    if (account.__pin != newPin):
                        account.__pin = newPin
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
        print(self.__security_question)
        sa = input()
        print("------------------------------------------------------------------")
        return sa

    def __str__(self) -> str:
        return str(self.__acno)


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
    print("1) Create Account \n2) Make Transactions")
    print("------------------------------------------------------------------")
    print("Enter your choice ", end='')
    choice = GetNumber()
    match choice:
        case 1:
            print("------------------------------------------------------------------")
            a = Account()
            print("------------------------------------------------------------------")
        case 2:
            a=Account.validate()
            if a!=-1:
                choice2=''
                while choice2 != 0:
                    os.system('cls')
                    a.greet()
                    print("1) Deposit \n2) Withdraw \n3) View Balance\n4) Change pin\n5) Show Account \n6) Transfer Money \n0) For Exit")
                    print("------------------------------------------------------------------")
                    print("Enter your choice ", end='')
                    choice2 = GetNumber()
                    match choice2:
                        case 1:
                            print("------------------------------------------------------------------")
                            a.deposit()
                            print("------------------------------------------------------------------")
                        case 2:
                            print("------------------------------------------------------------------")
                            a.withdraw()
                            print("------------------------------------------------------------------")
                        case 3:
                            print("------------------------------------------------------------------")
                            a.checkBalance()
                            print("------------------------------------------------------------------")
                        case 4:
                            print("------------------------------------------------------------------")
                            a.changePin()
                            print("------------------------------------------------------------------")
                        case 5:
                            print("------------------------------------------------------------------")
                            a.showAccount()
                            print("------------------------------------------------------------------")
                        case 6:
                            print("------------------------------------------------------------------")
                            a.transferMoney()
                            print("------------------------------------------------------------------")
                        case 0:
                            print("------------------------------------------------------------------")
                            print("                  good bye !! Visit Again !!")
                            print("------------------------------------------------------------------")
                        case _:
                            print("Please Enter a Valid Choice")
                    if choice2!=0:
                        input("Please Enter to Continue")
        case _:
            print("Please Enter a Valid Choice")
    input("Please Enter to Continue")