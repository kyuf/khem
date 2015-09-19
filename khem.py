#main menu
def main():
    #clear screen
    import os
    os.system("clear")
    
    print("Welcome to khem")
    print("Select from options:\n")
    print("%4s" % ("1. Calculate MW of compound\n"))
    select = input("Enter choice (number):\n>> ")
    
    while True:
        try:
            select = int(select)
            break
        except:
            select = input("Please enter valid number for choice")
    
    #clear screen on successful selection
    os.system("clear")
    
    if select == 1:
        import find_mw
        find_mw.main()

while True:    
    main()