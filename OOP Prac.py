



class Account:
    
    def __init__(self, owner):
        self.balance = 0
        self.owner = owner
     
    def withdrawal(self, amount):
        self.balance=self.balance + amount
        print(self.owner,':',self.balance)
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(self.owner,':',self.balance)

    


# In[99]:


class Business(Account):
    def __init__(self, owner, business_name):
        Account.__init__(self, owner)
        self.business_name = business_name
        


class Checking(Account):
    def __init__(self, owner):
        Account.__init__(self, owner)



class Saving(Account):
    def __init__(self, owner):
        Account.__init__(self, owner)
        self.interest = 0.02
        
    def collect_interest(self):
        Saving.deposit(self, self.balance*self.interest)






ledger = {}
countlist= [i for i in range(2000)]
def count_():
    return countlist.pop(0)
    

def fund(account, amount):
    
    account.deposit(amount)
    ledger[count_()] = [account.owner,'fund',amount]
    
    print(ledger)

def payment(sender, recipient, amount):
    if amount < sender.balance:
        sender.withdrawal(amount)
        recipient.deposit(amount) 
        ledger[count_()]=[sender.owner,recipient.owner,amount]
        print(ledger)

    else:
        print('insuficient funds')
    
    
    
    






