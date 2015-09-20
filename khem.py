#main menu
def main():
    #clear screen
    import os
    os.system("clear")
    
    print("Welcome to khem")
    print("Select from options:\n")
    print("1. Calculate MW of compound")
    print("2. Find mass given moles")
    print("3. Find moles given mass\n")
    
    select = input("Enter choice (number):\n>> ")
    
    #available options
    options = {1, 2, 3}
    
    while True:
        try:
            select = int(select)
            if select in options:
                break
            else:
                select = "fail"
        except:
            select = input("Please enter valid number for choice:\n>> ")
    
    #clear screen on successful selection
    os.system("clear")
    
    if select == 1:
        import find_mw
        find_mw.main()
    
    elif select == 2:
        import calc_mass_and_moles
        calc_mass_and_moles.main(0)
    
    elif select == 3:
        import calc_mass_and_moles
        calc_mass_and_moles.main(1)

while True:    
    main()
