from k_fun import *

#rxn parser
def parse(rxn):
    #store parsed species using SpecList
    reactants = SpecList("Reactants")
    products = SpecList("Products")
    prefix = ""
    form = ""
    
    #variable to show which side of the equation we are on
    left = True
    
    #special characters
    special = {"+", ">", " "}
    
    #parse through rxn string
    i = 0
    while i < len(rxn):
        if rxn[i] in special:
            #space will not trigger any action
            if rxn[i] != " ":
                #error if + or > with empty form
                if not form:
                    raise SyntaxError("Improper syntax")
                elif rxn[i] == "+":
                    #add to reactants/products depending on side
                    prefix = to_int(prefix)
                    if left:
                        reactants.append(Species(form, prefix))
                    else:
                        products.append(Species(form, prefix))
                elif rxn[i] == ">":
                    #add to reactants if on left side
                    if left:
                        left = False
                        reactants.append(Species(form, to_int(prefix)))
                    #error if on right side
                    else:
                        raise SyntaxError("> in wrong location")
                
                #reset form and prefix
                form = ""
                prefix = ""
            i += 1
        
        #append numbers to prefix
        elif is_number(rxn[i]):
            #error if prefix before form reset
            if form:
                raise SyntaxError("Misplaced prefix")
            prefix += rxn[i]
            i += 1
        
        #capital letter means new form
        elif rxn[i] == rxn[i].upper():
            #error if form before form reset
            if form:
                raise SyntaxError("Extra spaces")
            #continue adding to form until hitting special character
            while i < len(rxn) and rxn[i] not in special:
                form += rxn[i]
                i += 1
        
        #invalid input
        else:
            raise SyntaxError("Invalid input")
    
    #add last form to products, error if form empty
    if form == "":
        raise SyntaxError("Missing product")
    else:
        products.append(Species(form, to_int(prefix)))
    
    #error if empty reactants
    if not reactants:
        raise SyntaxError("Missing reactants")
    
    #check for mole balance
    if reactants.moles.balance != products.moles.balance:
        raise SyntaxError("Moles unbalanced")
    
    return reactants, products
    
"""
r, p = parse("2H2 + O2 > 2H2O")
print(r)
print(p)
"""
