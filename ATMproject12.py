#Code designed by Jonathan Abramson
#This is for project 12
#This is an example ATM machine in the command line 
#I tried to figure out how to make a UI as well, but clearly was unsuccesful

class BankAccount: 

    def __init__(self, ID,PIN,checking,savings):
        self.ID = ID
        self.PIN = PIN
        self.checking = checking
        self.savings = savings

#Account information getters
    def getID(self):
        return self.ID
    def getPIN(self):
        return self.PIN 
    def getSavings(self):
        return self.savings
    def getChecking(self):
        return self.checking
    def withdraw(self,amount,type):
#Does not let the user withdraw more than they have
        if(type==1):
          if(self.savings<amount):
              return False
          else: 
              self.savings -= amount
        elif(type==2):
            if(self.checking<amount):
                return False
            else:
                self.checking -= amount
        return True
#Dictates which account the deposit is going into
    def deposit(self,amount,type):
        if(type==1):
            self.savings += amount
        elif(type==2):
            self.checking += amount

def main():
    account = []
    n=0

#Example file with different # amounts
    with open("CustomerExample.txt") as file: 
        for line in file: 
            li = line.split(' ') 
            account.append(BankAccount(li[0],li[1],float(li[2]),float(li[3].replace('\n',''))))
            n += 1 

    userid = input("Enter ID #- ")
    userpin = input("Enter PIN #- ")
    i=0

    while i<n:
        if(account[i].getID()==userid):
            if(account[i].getPIN()==userpin):
            
#Prompt the user to decide what they would like to do after inputing their ID and pin
                option = int(input('Enter: [1] to withdraw cash from your Savings or Checkings. [2] to transfer cash from your Savings or Checkings[3] check balance of your Savings or Checkings: '))
                if(option==1):
                    type = int(input('Type: [1] Savings [2] Checkings: '))
                    amount = float(input("Enter #: "))
                    if(account[i].withdraw(amount,type)):
#Lets the code know which account is being withdrawn from                    
                        if(type==1):
                            print(amount,'withdrawn from your account. Balance: ',account[i].getSavings())
                        else:
                            print(amount,'withdrwan from your account.  Balance: ',account[i].getChecking())
                    else:
                        print('Not enough funds in account!')
                elif(option==2):
                    option = int(input('Which account: [1] Internal Account Transfer [2] New Account Transfer: '))
                    if(option==1): 
                        fromto = int(input('Transfer: [1] Savings Account to Checking Account [2] Checking Account to Savings Account: '))
                        amount = float(input('Enter amount: '))
#Will print the transfer amount from the internal transfer                       
                        if(fromto==1):
                            account[i].withdraw(amount,1)
                            account[i].deposit(amount,2)
                            print('Savings Account to Checking Account transfer complete.')
                        else:
                            account[i].withdraw(amount,2)
                            account[i].deposit(amount,1)
                            print('Checking Account to Savings account transfer complete.')
#Prompts user to enter their ID in order to transfer funds                           
                    else: 
                        AccountID = input('Enter ACCOUNT ID to transfer funds- ')
                        j=0
                        while j<n:
                            if(account[j].getID()==AccountID):
                                break
                            j += 1
                        if(j<n):
                            type = int(input('Type: [1] Savings [2] checking: '))
                            amount = float(input("Enter amount to transfer: "))
                            account[i].withdraw(amount,type)
                            account[j].deposit(amount,type)
                            print('Transfer successful to account ID #: ',account[j].getID())
                            if(type==1):
                                print(amount,'transferred. The new savings balance is: ',account[i].getSavings())
                            else:
                                print(amount,'transferred. The new checkings balance is: ',account[i].getChecking())
                        else:
                            print('Incorrect ID #. The current process has ended.')
                else:
                    type = int(input('Type: [1] Savings [2] Checkings: '))
                    if(type==1):
                        print('The current savings balance is:',account[i].getSavings())
                    else:
                        print('The current checking balance is:',account[i].getChecking())
                break
        i += 1

    if(i==n): 
        print('Invalid login attempt.')
    else: 
        file = open('CustomerExample.txt','w')
        j=0
        while j<n:
            file.write(account[j].getID()+' '+account[j].getPIN()+' '+str(account[j].getChecking())+' '+str(account[j].getSavings())+' ')
            j += 1
    file.close() 
	
    print('Goodbye, Thank you.')       

main()