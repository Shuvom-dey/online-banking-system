import interaction
import json
import bank

#OKEY SO STORING ALL THIS VARIABLE DATA IN VARIABLES OR ARRAY IS PRETTY TROUBLESOME 
#THAT'S WHY I USED JSON BEACUSE IT'S PRETTY MUCH EASY TO USE 

with open ("data.json","r") as file:
    customers= json.load(file)
    
option=interaction.menu()

while True:
    customer_idss=0
    open_account=None #check at last whether it's really needed or not ....
      
    if option ==1:
        print("\nOKEY , YOU HAVE CHOOSEN TO CREATE AN ACCOUNT AT OUR BANK . WELLCOME ABROAD 😊")
        customer_idss+=1
        open_account=interaction.create_account()
        acc_num=interaction.bank_accnum(customer_id=customer_idss)
        
        while True:        
                                opt=bank.bank_menu()
                                    
                                if opt==1:
                                    bank_bal=bank.deposit(bank_bal)
                                    continue
                                elif opt==2:
                                    bank_bal=bank.withdraw(bank_bal)
                                    continue
                                elif opt==3:
                                    bank_bal=bank.show_bal(bank_bal)
                                    print(f"HERE THE AMOUNT OF MONEY U HAVE IN YOUR ACCOUNT{bank_bal}$ .")
                                    continue
                                else :
                                    print("OK YOU CHOOSE TO EXIT , HAVE A GOOD DAY 🙏")
                                break
        
#SO HERE I USED THE OPEN ACCOUNT VARIABLE TO STORE THE ACC_NUM OF PEOPLES IN A SINGLE DICTIONARY
#AND APPENDED IT ON THE VARIABLE WE CREATED FOR THE JSON FILE UNDER THE FIRST COMMENT 
        
        open_account["acc_num","bank_bal"]=acc_num,bank_bal
        customers.append(open_account)
        with open("data.json","w") as file:
            json.dump(customers,file)
            
#HERE I'M INITIALIZING THE BANK MENU FUNCTION FROM THE BANK.PY MODULE
#AND DEPENDING ON THE OPTION CHOOSEN WILL DITERMINE THE NEXT COURSE OF ACTION

            
        
    elif option ==2:
        while True:
            print("\nSO , YOU ALREADY HAVE AN ACCOUNT OPENED HERE . LET'S LOG INTO THAT 👉")
            login=interaction.login()
            for customer in customers:
                    if customer["phn_num"]==login[0] and customer["mapin"]==login[1]:
                        print(f"HEY IT'S GOOD TO SEE YOU > {customer['name']}<🙏WHAT DO YOU WANNA DO NEXT .")
                        while True:        
                                opt=bank.bank_menu()
                                    
                                if opt==1:
                                    bank_bal=bank.deposit(bank_bal)
                                    continue
                                elif opt==2:
                                    bank_bal=bank.withdraw(bank_bal)
                                    continue
                                elif opt==3:
                                    bank_bal=bank.show_bal(bank_bal)
                                    print(f"HERE THE AMOUNT OF MONEY U HAVE IN YOUR ACCOUNT{bank_bal}$ .")
                                    continue
                                else :
                                    print("OK YOU CHOOSE TO EXIT , HAVE A GOOD DAY 🙏")
                                break
                                
                    break
                    
            else :
                print("IT SEEMS LIKE THERE ISN'T ANY ACCOUNT OPENED HERE WITH THAT CREDENTIAL .. PLEASE TRY AGAIN ")
                continue
    break