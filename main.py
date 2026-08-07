import interaction
import json

#OKEY SO STORING ALL THIS VARIABLE DATA IN VARIABLES OR ARRAY IS PRETTY TROUBLESOME 
#THAT'S WHY I USED JSON BEACUSE IT'S PRETTY MUCH EASY TO USE 

with open ("data.json","r") as file:
    customers= json.load(file)
    
option=interaction.menu()

while True:
    customer_idss=0
    open_account=None
    
    if option ==1:
        print("\nOKEY , YOU HAVE CHOOSEN TO CREATE AN ACCOUNT AT OUR BANK . WELLCOME ABROAD 😊")
        customer_idss+=1
        open_account=interaction.create_account()
        acc_num=interaction.bank_accnum(customer_id=customer_idss)
        
        #SO HERE I USED THE OPEN ACCOUNT VARIABLE TO STORE THE ACC_NUM OF PEOPLES IN A SINGLE DICTIONARY
        #AND APPENDED IT ON THE VARIABLE WE CREATED FOR THE JSON FILE UNDER THE FIRST COMMENT 
        
        open_account["acc_num"]=acc_num
        customers.append(open_account)
        with open("data.json","w") as file:
            json.dump(customers,file)
        
    elif option ==2:
        print("\nSO , YOU ALREADY HAVE AN ACCOUNT OPENED HERE . LET'S LOG INTO THAT 👉")
        login=interaction.login()
        while True:
            
            if not login == open_account["phn_num","mapin"]:
                print("THERE ISN'T ANY ACOOUNT WITH THIS CREDENTIALS ON OUR DATABASE .",
                    "\nPLEASE TRY AGAIN .🙏")
                continue
    else :
        print("working")