#determine limiting reactant
import rxn

def main():
    print("Limiting Reactant\n")
    while True:
        #prompt equation input
        while True:
            print("Enter reaction equation (ie. 2H2 + O2 > 2H2O)")
            print("(Enter 0 to return to khem menu)")
            print("Note: Prefixes must be integers")
            equation = input(">> ")
            if equation == "0":
                return
            try:
                #parse equation in reactant and product lists
                reactants, products = rxn.parse(equation)
                break
            except Exception as msg:
                print("\nError: %s\n" % (msg.args[0]))
        
        #formatting
        print("")
        
        #prompt mass input
        lim_mole = None
        lim_r = None
        for spec in reactants.list:
            #loop until valid input
            while True:
                r_mass = input("Enter mass of %s in g >> " % (spec.form))
                
                #test if input is valid number
                try:
                    r_mass = float(r_mass)
                    #mass must be greater than 0
                    if r_mass <= 0:
                        print("\nMass cannot be negative or 0")
                        continue
                    else:
                        break
                except:
                    print("\nInvalid input\n")    

            #calculate moles from mass using MW
            r_mole = (r_mass/spec.mw) / spec.prefix
            
            #limiting reactant will have least moles
            if lim_mole == None or r_mole < lim_mole:
                lim_mole = r_mole
                lim_r = spec
                
        
        print("\nThe limiting reactant is the %.3f moles of %s\n" % (lim_mole * lim_r.prefix, lim_r.form))
