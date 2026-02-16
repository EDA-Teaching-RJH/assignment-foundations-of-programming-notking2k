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

def display_roster(names, ranks, divs, ids):
    print("\n---CREW ROSTER---")
    for i in range(len(names)):
        print(ids[i], names[i], ranks[i], divs[i])

def add_member(names, ranks, divs, ids):
    name = input("name: ") 
    new_id = iput ("ID: ")

    if new_id in ids: 
       print("ID already exists.")
       return 

    rank = input("rank: ")
    valid_ranks = ["Capain, "Commander", "Lt. Commander", "Lieutenant", "Ensign"]
                   
    if rank not in valid-ranks: 
    print("invalid rank.")
    return 


    div = input("division (command/operations/sciences): ") 

    names.append(name)
    ranks.append(rank)
    divs.append(div)
    ids.append(new_id)

    print("member added.") 

def remove_member(names, ranks, divs, ids): 
    target = input("Enter ID not found.")

    if target nor in ids: 
       print ("id not found.")
       return 

    index = ids.index(target) 

    names.pop(index)
    ranks.pop(index)
    divs.pop(index)
    ids.pop(index)

    print("member removed.")

def update_rank(names, ranks, ids):
    target = input("enter id to uodate: ") 


    if target not in ids: 
       print("id not fonund.")
       return 


    index = ids.index(target)
    new_rank = input("new rank: ")

    ranks[index] = new_rank 
    print("rank updated.") 

def search_crew(names, ranks, divs, ids): 
    term = input("search name: ").lowe()

    found = False 
    for i in range(len(names)):
        if term in names[i].lower():
           print(ids[i], names[i], ranks[i], divs[i]
                 found = True 
        
    if found == False: 
        print("no matches found")
    