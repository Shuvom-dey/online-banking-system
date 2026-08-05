def menu():
    print("1. CREATE ACOOUNT .",
          "\n2. LOG-IN .",
          "\n3. KNOW ABOUT OUR BANK ."
          "\nCHOOSE AN OPTION .")
    
    #THIS IS JUST THE MENU PART SHOWING SOME OPTIONS 
    #AND VALIDATING IF THE USER HAS CHOOSEN A CORRECT OPTION OR NOT 
    #AND RETURNING THE OPTION VARIABLE AT THE END TO USE IT LATER OUTSIDE THE FUNCTION 
    
    while True:
        option=input("ENTER YOUR CHOICE OF OPTION HERE >>")
        if not option.isdigit():
            print("PLEASE ENTER A VALID DIGIT 🔢")
            continue 
        option=int(option)
        if option not in [1,2,3]:
            print("YOU HAVE CHOOSEN A WRONG OPTION PLEASE CHOOSE ANOTHER !!")
        else:
            return option
        
        
        
def create_account():
    
    #INPUTING ALL THE VALUES IN THE VARIABLES >>
    
    name=str(input("ENTER YOUR NAME HERE >>"))
    age=int(input("ENTER YOUR AGE HERE >>"))
    phn_no=int(input("ENTER YOUR PHONE NUMEBER HERE >>"))
    address=str(input("ENTER YOUR ADDRESS HERE >>"))
    pin=int(input("ENTER A NEW MPIN HERE >>"))
    
    #ORGANIZING ALL THE VARIABLE VALUES IN A DICTIONARY 
    #FOR EASYNESS OF RETURNING AND USING ANY PERTICULAR VALUE OUTSIDE THE FUNCTION
    
    account={"name":name,
             "age":age,
             "phn_num":"+91"+str(phn_no),
             "address":address,
             "mapin":pin}
    
    #OR THIS A WAY TO DO THE SAME THING BUT A BIT MORE WORK 
    # name,age,phn_no,address,acc_no=create_account()
    # ^^[this line will be outside the function so that the return value can be accessed ]
    
    return account


def bank_accnum(customer_id):
    
    #THIS FUNCTION IS FOR CREATING JUST THE BANK ACCOUNT NUMBER AS A STRING 
     
    bankcode="033"
    acc_num=bankcode+f"{customer_id:09}"
    
    return acc_num

def login():
    
    #WHAT I WANNA DO HERE IS JUST GET THE INPUT AND 
    #AND COMPARE IT WITH THE CREATE_ACCOUNT'S PHN_NUM & MPIN 
    #IF IT MATCHES THEN IT CAN DISPLAY THE REST OF THE DETAILS FROM THE CREATE_ACCOUNT FUNCTION
    
    phn_num=int(input("ENTER YOUR REGISTERED PHONE NUMBER HERE >>"))
    mpin=int(input("ENTER YOUR MPIN HERE >>"))
     
    return phn_num , mpin
