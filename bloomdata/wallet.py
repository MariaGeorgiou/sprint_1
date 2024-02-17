#example of classes
#import pandas as pd

#Builds class of type DataFrame
#df holds a DataFrame 'object'
#'instantiated' an object =create new object and save to a variable
#df = pd.DataFrame({'a': [1,2,3], 'b': [4,5,6]})

#variables that form part of an object = attributes
# access using 'dot-notation'
#eg. df.shape / df.index / df.dtypes/ df.columns


#functions part of an object = methods
#eg df.head(), df.describe(), df.isnull().sum() = include parethesis to run code behind scenes

#a method associated with a pandas 'series' object aka column which lives inside of a dataframe
#df['a'].value_counts()

#whenever we make a class, always starts with that as a keyword

class Wallet:
    #first thing to run when we make a new class
    #outline required user provided input values
    def __init__(self, initial_amount =0):
        #can put initial amount = 0 to set default value
        #save as an attribute
        self.balance = initial_amount


    #inside cash METHOD
    def spend_cash(self, amount):
        if self.balance < amount: 
            return "not enough money"
        else:
            self.balance = self.balance - amount
            return f"remaining balance: {self.balance}"
        
    def add_cash(self, amount):
        self.balance = self.balance + amount
        return f"new balance of: {self.balance}"


    #repr method changes how object loojs when its printed out
        #presence of self keywprd allows access or modify class attributes within this function
    def __repr__(self):
        return f"Wallet with balance of: ${self.balance}"
    
if __name__ == '__main__':
    wallet1 = Wallet(100)
    wallet2 = Wallet(50)
    wallet3 = Wallet(3000)
    print(wallet1)
    print(wallet2)
    print(wallet3)
    #could also do print(wallet1.balance) for it to print out just amount

    print(wallet1.spend_cash(120))
    print(wallet1.add_cash(60))
    print(wallet1.spend_cash(120))
    print(wallet1.balance)


