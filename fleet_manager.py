def init_database():
    names = ["Picard" "Riker","Data","Worf","Crusher"]
    ranks = ["Captain","Commander,"Lt.Commander","lieutenant","ensign"]
    divs = ["command","operations","operations","sciences"]
    ids = ["001","002","003","004","005"]
    return names, ranks, divs, ids 

def display_menu(user):
    if user ==""
        user = (input("Enter your full name: ")
                
    print ("\n---MENU---")
    print ("Logged in as:", user)
    print ("1. view roster")
    print ("2. add member") 
    print ("3. remove member") 
    print ("4. update rank")
    print ("5. seatch crew")
    print ("6. filter by division")
    print ("7. calculate payroll") 
    print ("8. count officers")
    print ("9. reset database")
    print ("0. exit") 

    choice = input(select option: ")
    return choice, user 