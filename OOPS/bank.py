
class Bank:

    accno :int
    bank_name:str
    balance:int
    ac_type:str

    def create_account(self,accno,ac_type):

        self.bank_name="SBI"
        self.balance=2000
        self.accno=accno
        self.ac_type=ac_type

    def deposit(self,amount):

        self.balance+=amount

        print(f"your{self.bank_name}Acc with {self.accno}has been credited with amount{amount} available balance{self.balance}")

    def withdraw(self,amount):

        if amount > self.balance:  #5000>2000
            
            print("transaction failed insufficient balance")
        
        else:

            self.balance-=amount

            print(f"your{self.bank_name}Acc with {self.accno}has been debited with amount{amount}  avilable balance{self.balance}")

    def get_balance(self):

        print(f"available balance{self.balance}")

user_account=Bank()

user_account.create_account(1000013,"savings")

user_account.withdraw(1000)

user_account.deposit(5000)