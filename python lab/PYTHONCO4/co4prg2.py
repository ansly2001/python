class Bankaccount:
    def __init__(self):
        self.account_number=input("enter the account number:")
        self.name=input("enter the name:")
        self.account_type=input("enter the account type:")
        self.balance=0
        
    def deposit(self):
        amount=int(input("enter the amount to be deposited:"))
        self.balance+=amount
    
    def withdraw(self):
        amount=int(input("enter the amount to be withdraw:"))
        if self.balance>amount:
            self.balance-=amount
            print("balance=",self.balance)
        else:
            print("withdraw not possible")
            
    def display(self):
        print("net available balance:",self.balance)
        
a=Bankaccount()
while(True):
    print("\n 1.Deposit Money \n2.Withdraw Money \n3.Exit")
    ch=int(input("enter the choice:"))
    if(ch==1):
        a.deposit()
        a.display()
    elif(ch==2):
        a.withdraw()
        a.display()
    else:
        exit(0)

        
        


        
        
        
    

        