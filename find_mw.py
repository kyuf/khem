from k_fun import *

#MW calculator
def main():
    #prompt user input
    print("MW Calculator\n")
    
    #loop until valid input
    while True:
        choice = input("Enter species (Enter 0 to return to khem menu) >> ")
        if choice == "0":
            return
        try:
            spec = Species(choice)
            print("\nThe MW of %s is: %.3f\n" % (spec.form, spec.mw))
        except:
            print("\nInvalid input\n")
