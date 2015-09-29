#import element properties
from e_props import elements
from k_fun import *

def main():
    #prompt user input
    print("MW Calculator\n")
    while True:
        choice = input("Enter species (Enter 0 to return to khem menu) >> ")
        if choice == "0":
            return
        try:
            spec = Species(choice)
            print("\nThe MW of %s is: %s\n" % (spec.form, spec.mw))
        except:
            print("\nInvalid input\n")
