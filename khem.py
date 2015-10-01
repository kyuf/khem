#main menu
def main():
    #clear screen
    import os
    os.system("clear")
    
    #selection screen
    print("Welcome to khem")
    print("Select from options:\n")
    print("1. Calculate MW of compound")
    print("2. Find mass given moles")
    print("3. Find moles given mass")
    print("4. Limiting Reactant\n")
    
    select = input("Enter choice (number):\n>> ")
    
    #available options
    options = {1, 2, 3, 4}
    
    #loop until valid input
    while True:
        try:
            select = int(select)
            if select in options:
                break
            #need to implement proper error message
            else:
                select = "fail"
        except:
            select = input("Please enter valid number for choice:\n>> ")
    
    #clear screen on successful selection
    os.system("clear")
    
    #call selected function
    if select == 1:
        #mw calculator
        import find_mw
        find_mw.main()
    
    elif select == 2:
        #mass calculator
        import calc_mass_and_moles
        calc_mass_and_moles.main(0)
    
    elif select == 3:
        #mole calculator
        import calc_mass_and_moles
        calc_mass_and_moles.main(1)
        
    elif select == 4:
        #limiting reactant
        import limiting
        limiting.main()

while True:    
    main()
