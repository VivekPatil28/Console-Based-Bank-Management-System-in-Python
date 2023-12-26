import os
import pickle
import tempfile
import shutil
from datetime import datetime
file_path = r"E:\Python Programs\Console Based Bank Management System in Python\BMS_DATA.BMS"
while True:
    try:
        class Transaction():
            def __init__(self,data,time):
                self.data = data
                self.time = time

        class Account():
            __accounts = []
            @classmethod
            def returnAccounts(cls):
                return cls.__accounts
            
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
                print("Enter the Account Number ", end='')
                self.__acno = GetNumber()
                print("Enter Pin ", end='')
                self.__pin = GetNumber()
                self.__security_question = self.securityQuestion()
                self.__security_question_answer = self.securityQuestionAnswer()
                self.__balance = 0
                self.__transactions = []
                Account.__accounts.append(self)
                print("Account Was Created Successfully")

            def showAccount(self):
                print(
                    "------------------------------------------------------------------")
                print("Name                     = ", self.__name)
                print("Account Number           = ", self.__acno)
                print("Pin                      = ", self.__pin)
                print("Security Question        = ", self.__security_question)
                print("Security Question Answer = ",
                      self.__security_question_answer)
                print("Account Balance          = ", Account.humanizeAmount(self.__balance))
                print("------------------------------------------------------------------")

            # Humanize the Account Balance with Commas (,)
            @classmethod
            def humanizeAmount(cls,val):
                num = ''
                stri = str(val)[::-1]
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
                print("Your Available Balance is ", Account.humanizeAmount(self.__balance))

            def addTransaction(self,data):
                self.__transactions.append(Transaction(data,datetime.today()))

            def deposit(self):
                print("Enter Amount to Deposit ")
                s = GetNumber()
                self.__balance += s
                self.addTransaction(f"Rs{Account.humanizeAmount(s)} Deposited | Current Balance Rs{Account.humanizeAmount(self.__balance)}")
                print("Amount Deposited SuccessFully")
                print("Current Balance =", Account.humanizeAmount(self.__balance))

            def withdraw(self):
                print("Enter Amount to Withdraw ")
                d = GetNumber()
                if (d < self.__balance):
                    self.__balance -= d
                    self.addTransaction(f"Rs{Account.humanizeAmount(d)} Withdrawed | Current Balance Rs{Account.humanizeAmount(self.__balance)}")
                    print("withdrawal Successful")
                    print("Current Balance =", Account.humanizeAmount(self.__balance))
                else:
                    print("Not Enough Money to Withdraw")

            def showTransactions(self):
                for i in self.__transactions:
                    print(i.data,i.time,sep=" | ")


            def transferMoney(self):
                print("Enter Reciver Account Number ")
                rnum = GetNumber()
                receiver_account = next((account for account in Account.__accounts if account.__acno == rnum ), None)

                if receiver_account is None:
                    print("Receiver Account Not Found")
                    return

                # Check for self-transfer
                if receiver_account.__acno == self.__acno:
                    print("Cannot Transfer to Self Account")
                    return

                print("Validation Successful")
                print("------------------------------------------------------------------")

                # Enter the Transfer Amount
                transfer_amount = GetNumber()

                # Check if the sender has enough balance
                if self.__balance < transfer_amount:
                    print("Not enough Balance to Transfer")
                    print("------------------------------------------------------------------")
                    return

                # Perform the transfer
                self.__balance -= transfer_amount
                receiver_account.__balance += transfer_amount

                # Update transaction details
                self.addTransaction(f"Rs{Account.humanizeAmount(transfer_amount)} Transferred to Account No {receiver_account.__acno} | Current Balance Rs{Account.humanizeAmount(self.__balance)}")
                receiver_account.addTransaction(f"Rs{Account.humanizeAmount(transfer_amount)} Received from Account No {self.__acno} | Current Balance Rs{Account.humanizeAmount(receiver_account.__balance)}")

                print("Transaction Successful !!! ")
                print("------------------------------------------------------------------")

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
                print(
                    "------------------------------------------------------------------")
                print("1) What is the name of one of your teacher ?\n2) What is the name of your favourite Resturant ?\n3) In what city did you meet your first partner ?\n4) What is your childhood nickname ?\n5)Add your Custom Question")
                print(
                    "------------------------------------------------------------------")
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
                print(
                    "------------------------------------------------------------------")
                print(self.__security_question)
                sa = input()
                print(
                    "------------------------------------------------------------------")
                return sa

            def __str__(self) -> str:
                return f"{self.__name} {self.__acno} {self.__pin} {self.__balance}"

        
        # Get Number Function to Get a Valid Number
        def FetchAccounts():
            with open(file_path,"rb") as f:
                data = f.read()
                if data:
                    s = pickle.loads(data)
                    Account.returnAccounts().extend(s)
                    for i in s:
                        print(i)

        def SaveAccounts():
            temp_file_path = None
            try:
                with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                    temp_file_path =  temp_file.name
                    with open(temp_file_path,"wb") as f:
                        f.write(pickle.dumps(Account.returnAccounts()))
                
                shutil.move(temp_file_path,file_path)
            except Exception as e:
                print("Error Occoured During Data Updation",e)
            finally:
                if temp_file_path  and os.path.exists(temp_file_path):
                    os.remove(temp_file_path)

        def GetNumber():
            while True:
                try:
                    x = int(input())
                    return x
                except ValueError:
                    print("Oops! That was not a valid number Try again...")
        if __name__ == '__main__':
            # Loads the Recent Bank Accounts
            FetchAccounts()
            # Driver Code
            choice = ""
            while(choice != 0):
                # os.system('cls')    # To Clear the Console
                print("------------------------- Welcome to MGB -------------------------")
                # Options to select
                print("1) Create Account \n2) Make Transactions")
                print("------------------------------------------------------------------")
                print("Enter your choice ", end='')
                choice = GetNumber()
                match choice:
                    case 1:
                        print(
                            "------------------------------------------------------------------")
                        a = Account()
                        print(
                            "------------------------------------------------------------------")
                    case 2:
                        a = Account.validate()
                        if a != -1:
                            choice2 = ''
                            while choice2 != 0:
                                os.system('cls')
                                a.greet()
                                print(
                                    "1) Deposit \n2) Withdraw \n3) View Balance\n4) View Transactions\n5) Change pin\n6) Show Account \n7) Transfer Money \n0) For Exit")
                                print("------------------------------------------------------------------")
                                print("Enter your choice ", end='')
                                choice2 = GetNumber()
                                match choice2:
                                    case 1:
                                        print(
                                            "------------------------------------------------------------------")
                                        a.deposit()
                                        print(
                                            "------------------------------------------------------------------")
                                    case 2:
                                        print(
                                            "------------------------------------------------------------------")
                                        a.withdraw()
                                        print(
                                            "------------------------------------------------------------------")
                                    case 3:
                                        print(
                                            "------------------------------------------------------------------")
                                        a.checkBalance()
                                        print(
                                            "------------------------------------------------------------------")
                                    case 4:
                                        print(
                                            "------------------------------------------------------------------")
                                        a.showTransactions()
                                        print(
                                            "------------------------------------------------------------------")
                                    case 5:
                                        print(
                                            "------------------------------------------------------------------")
                                        a.changePin()
                                        print(
                                            "------------------------------------------------------------------")
                                    case 6:
                                        print(
                                            "------------------------------------------------------------------")
                                        a.showAccount()
                                        print(
                                            "------------------------------------------------------------------")
                                    case 7:
                                        print(
                                            "------------------------------------------------------------------")
                                        a.transferMoney()
                                        print(
                                            "------------------------------------------------------------------")
                                    case 0:
                                        print(
                                            "------------------------------------------------------------------")
                                        print(
                                            "                  good bye !! Visit Again !!")
                                        print(
                                            "------------------------------------------------------------------")
                                    case _:
                                        print("Please Enter a Valid Choice")
                                if choice2 != 0:
                                    input("Please Enter to Continue")
                    case _:
                        print("Please Enter a Valid Choice")
                input("Please Enter to Continue")
    except Exception as e:
        print("Application Crashed")
        print("Error : ", e)
        input("Please Enter to Restart")
    finally:
        SaveAccounts()