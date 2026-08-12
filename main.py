import interaction
import json
import bank

#OKEY SO STORING ALL THIS VARIABLE DATA IN VARIABLES OR ARRAY IS PRETTY TROUBLESOME 
#THAT'S WHY I USED JSON BEACUSE IT'S PRETTY MUCH EASY TO USE 

    
option=interaction.menu()
entry1=True
while entry1:
    with open ("data.json","r") as file:
        customers= json.load(file)
    
    customer_idss=0
    open_account=None
    bank_bal=0
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
                
                open_account["bank_bal"]=bank_bal
                open_account["acc_num"]=acc_num
                
                customers.append(open_account)
                with open("data.json","w") as file:
                    json.dump(customers,file)
                break
        entry1=False
        
#SO HERE I USED THE OPEN ACCOUNT VARIABLE TO STORE THE ACC_NUM OF PEOPLES IN A SINGLE DICTIONARY
#AND APPENDED IT ON THE VARIABLE WE CREATED FOR THE JSON FILE UNDER THE FIRST COMMENT 
        
        
            
#HERE I'M INITIALIZING THE BANK MENU FUNCTION FROM THE BANK.PY MODULE
#AND DEPENDING ON THE OPTION CHOOSEN WILL DITERMINE THE NEXT COURSE OF ACTION

            
        
    elif option ==2:
        
#I AGAIN INVOKED THE JSON FILE FOR THE LOGIN PART 
        
        with open ("data.json","r") as file:
            customers= json.load(file)
            
        loged_in=True        
        while loged_in:
            print("\nSO , YOU ALREADY HAVE AN ACCOUNT OPENED HERE . LET'S LOG INTO THAT 👉")
            
            login=interaction.login()
            found=False
            
            for customer in customers:
                
#HERE WHAT I DID IS SEARCHED THROUGH EVERY DICTIONARY OF DATA OF PERSON THAT HAS AN ACCOUNT HERE 
#AND LOOKED FOR THE PARTICULAR DATA TO MATCH FOR FURTHER BANKING TRANSACTION           
  
                    if customer["phn_num"]==login[0] and customer["mapin"]==login[1]:
                        
                        print(f"HEY IT'S GOOD TO SEE YOU > {customer['name']} <🙏 WHAT DO YOU WANNA DO NEXT .")
                        bank_bal=customer["bank_bal"]
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
                            
#AND HERE WHEN THE DEED IS DONE I UPDATED THE PERSON'S BANK BALANCE DATA WITH THE NEW TRANSACTIONS    
                         
                        customer["bank_bal"]=bank_bal
                        with open("data.json","w") as file:
                            json.dump(customers,file)
                            
                        found=True
                        loged_in=False 
                        
                        break
                            
            if not found :
                print("IT SEEMS LIKE THERE ISN'T ANY ACCOUNT OPENED HERE WITH THAT CREDENTIAL .. PLEASE TRY AGAIN ")
                    
                        
        entry1=False
    elif option==3:
        print('''🏦 WELCOME TO TRUSTWAVE DIGITAL BANK 🏦

                Thank you for choosing TrustWave Digital Bank.

                TrustWave Digital Bank is a simple and secure banking system designed to help customers manage their money conveniently. Our goal is to provide a fast, reliable, and user-friendly banking experience.

                🌟 OUR SERVICES

                • Create a new bank account
                • Secure login using your registered phone number and MPIN
                • Deposit money into your account
                • Withdraw money safely
                • Check your current account balance
                • Store customer information securely

                🔒 SECURITY FIRST

                Your account is protected using:
                • Registered phone number verification
                • Personal MPIN authentication
                • Secure storage of customer records

                🎯 OUR MISSION

                To make digital banking simple, accessible, and secure for everyone while helping users learn and experience modern banking systems.

                💡 ABOUT THIS PROJECT

                This banking system has been developed as a programming project using Python and JSON data storage. It demonstrates important software development concepts such as:

                • Functions and modular programming
                • Data validation
                • JSON file handling
                • User authentication
                • Banking operations (Deposit, Withdraw, Balance Inquiry)

                🙏 Thank you for banking with us.

                "Your Trust, Our Responsibility." ''')
        entry1=False
    else:
        print("SO YOU WANNA EXIT , GOODBYE THEN 🙏")
        entry1=False
