def bank_menu():
    
    
    print("HELLO SIR WHAT DO YOU WANNA DO TODAY 🏦💵",
          "\n1. DEPOSIT 💰",
          "\n2. WITHDRAW 💸",
          "\n3. SHOW BALANCE 🧾",
          "\n4. EXIT 🚪")
    
    #THIS IS JUST THE MENU PART SHOWING SOME OPTIONS 
    #AND VALIDATING IF THE USER HAS CHOOSEN A CORRECT OPTION OR NOT 
    #AND RETURNING THE OPTION VARIABLE AT THE END TO USE IT LATER OUTSIDE THE FUNCTION 
        
    
    while True :
        
        option=input("HERE INPUT YOUR CHOICE OF OPTION >>")
        if not option.isdigit():
            print("YOU HAVE GIVEN WRONG INPUT , PLEASE TRY AGAIN !!")
            continue
        option=int(option)
        if option not in [1,2,3,4]:
           print("YOU HAVEN'T CHOOSEN A OPTION FROM THE MENU PLEASE CHOOSE ONE !!")
        else:
            return option



def deposit(bank_bal):
    
    while True :
        amount=input("ENTER THE AMOUNT OF MONEY YOU WANNA DEPOSIT >>")
        if not amount.isdigit():
            print("PLEASE ENTER A VALID AMOUNT !!")
            continue 
        amount=int(amount)
        bank_bal+=amount
        return bank_bal
        
        
def withdraw(bank_bal):
    
    while True :
            amount=input("ENTER THE AMOUNT OF MONEY YOU WANNA WITHDRAW >>")
            if not amount.isdigit():
                print("PLEASE ENTER A VALID AMOUNT !!")
                continue 
            amount=int(amount)
            if amount>bank_bal:
                print("YOU DON'T HAVE ENOUGH MONEY IN YOUR ACCOUNT !!😥")
                continue
            else :
                bank_bal-=amount
                return bank_bal


def show_bal(bank_bal):
    return bank_bal

    
