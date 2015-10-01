#calculate either the mass or moles of a compound given the other
from k_fun import *

def main(select):
    title = ["Mass", "Mole"]

    print("%s Calculator\n" % (title[select]))
    
    choice = ["moles", "mass [g]"]
    unit = [" g", " moles"]
    
    #continuous loop
    while True:
        #prompt compound input
        while True:
            spec = input("Enter species (Enter 0 to return to khem menu) >> ")
            if spec == "0":
                return
            try:
                spec = Species(spec)
                break
            except:
                print("\nInvalid input\n")
    
        #prompt mass/mole input
        while True:
            i = input("Enter %s of compound >> " % (choice[select]))
            try:
                i = float(i)
                if select == 0:
                    calc = i * spec.mw
                else:
                    calc = i / spec.mw
                print("\nThere are %.3f%s in %s%s of %s\n" % (calc, unit[select], i, unit[-select - 1], spec.form))
                break
            except:
                print("\nInvalid input\n")
