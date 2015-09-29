from k_fun import is_number, to_int

#rxn parser
def parse(rxn):
    #dicionaries store compound as key and prefix as value
    reactants = {}
    products = {}
    prefix = ""
    compound = ""
    
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
                #error if + or > with empty compound
                if not compound:
                    raise SyntaxError("Improper syntax")
                elif rxn[i] == "+":
                    #add to reactants/products depending on side
                    if left:
                        reactants[compound] = to_int(prefix)
                    else:
                        products[compound] = to_int(prefix)
                elif rxn[i] == ">":
                    #add to reactants if on left side
                    if left:
                        left = False
                        reactants[compound] = to_int(prefix)
                    #error if on right side
                    else:
                        raise SyntaxError("> in wrong location")
                
                #reset compound and prefix
                compound = ""
                prefix = ""
            i += 1
        
        #append numbers to prefix
        elif is_number(rxn[i]):
            #error if prefix before compound reset
            if compound:
                raise SyntaxError("Misplaced prefix")
            prefix += rxn[i]
            i += 1
        
        #capital letter means new compound
        elif rxn[i] == rxn[i].upper():
            #error if compound before compound reset
            if compound:
                raise SyntaxError("Extra spaces")
            #continue adding to compound until hitting special character
            while i < len(rxn) and rxn[i] not in special:
                compound += rxn[i]
                i += 1
    
    #add last compound to products, error if compound empty
    if compound == "":
        raise SyntaxError("Missing product")
    else:
        products[compound] = to_int(prefix)
    
    #error if empty reactants
    if not reactants:
        raise SyntaxError("Missing reactants")
    
    return reactants, products

print(parse("2H2 + O2 > 2H2O"))
print(parse("2H2 + O2 > 2H2O"))

