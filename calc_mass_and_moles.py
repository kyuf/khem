#calculate either the mass or moles of a compound given the other
from find_mw import find_mw

def main():
    print("Mass/Mole Calculator")
    print("Select from options:\n")
    print("1. Find mass given moles")
    print("2. Find moles given mass\n")
    
    choice = ["moles", "mass [g]"]
    unit = ["g", " moles"]
    
    #prompt mass/mole selection
    while True:
        select = input("Enter selection:\n>> ")
        if select not in {"1", "2"}:
            print("Invalid selection\n")
        else:
            select = int(select)
            break
                
    #prompt compound input
    while True:
        compound = input("Enter compound:\n>> ")
        if compound == "0":
            break
        try:
            MW = find_mw(compound)
            break
        except:
            print("Invalid input\n")
    
    #prompt mass/mole input
    while True:
        i = input("Enter %s of compound:\n>> " % (choice[select]))
        try:
            i = float(i)
            if select == 1:
                calc = i * MW
            else:
                calc = i / MW
            print("There are %s%s in %s%s of %s" % (calc, unit[select - 1], i, unit[-select], compound))
            break
        except:
            print("Invalid input\n")

main()
