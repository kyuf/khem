#calculate either the mass or moles of a compound given the other
from find_mw import find_mw

def main(select):
    title = ["Mass", "Mole"]

    print("%s Calculator\n" % (title[select]))
    
    choice = ["moles", "mass [g]"]
    unit = ["g", " moles"]
    
    #continuous loop
    while True:
        #prompt compound input
        while True:
            compound = input("Enter compound (Enter 0 to return to khem menu) >> ")
            if compound == "0":
                return
            try:
                MW = find_mw(compound)
                break
            except:
                print("\nInvalid input\n")
    
        #prompt mass/mole input
        while True:
            i = input("Enter %s of compound >> " % (choice[select]))
            try:
                i = float(i)
                if select == 0:
                    calc = i * MW
                else:
                    calc = i / MW
                print("\nThere are %s%s in %s%s of %s\n" % (calc, unit[select], i, unit[-select - 1], compound))
                break
            except:
                print("\nInvalid input\n")
