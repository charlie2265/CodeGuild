''' Charlie lab 25 represent an ATM with a class containing a balance
'''

class ATM:

    def __init__(self, amount):
        '''
        initialize an amount method
        '''
        self.amount = amount
        
    def __repr__(self):
        pass

    def check_balance(self):
        '''returns account balance
        '''
        print(self.amount)

            
        
    
    def deposit(self,customer):
        '''deposits given amount. increases total in account'''
        self.amount += customer
        print(f'You deposited $ {customer}, Your new balance is $ {self.amount}')
        # elif customer not in ['y', 'yes']:
                    # self.withdraw(100)


        
        
            
    def check_withdraw(self, customer):
        '''  return True in withdraw function if it does not overdraw'''
        amount = customer
        if amount < self.amount:
            return True
        
    def withdraw(self,amount):
        '''withdraws amount and returns it'''
        self.amount -= amount
        print(f'You withdrew $ {amount}, Your new balance is $ {self.amount}')
        
         
            
    
def main():
    while True:
        atm = ATM(100)
        customer = input('would you like to check your balance? (y)es or (n)o?:').strip().lower()
        if customer in ['y', 'yes']:
            atm.check_balance()
            
        atm.customer = input('would you like to make a deposit? (y)es or (n)o?:').strip().lower()
        if customer in ['y', 'yes']:
            atm.customer = float(input('please enter amount to deposit: '))
            atm.deposit(atm.customer)

        atm.customer = input('would you like to make a withraw? (y)es or (n)o?: ').strip().lower()
        if customer in ['y','yes']:
            atm.customer = float(input('How much would you like to withdraw?: '))
            atm.withdraw(100) 


        print(atm.check_withdraw(100))
        atm.check_withdraw(atm.amount)
         
            

main()
             
        
            
        
            
            
