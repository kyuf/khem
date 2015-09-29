#import element properties
from e_props import elements
from k_fun import is_number, to_int

#parse a compound and return its MW
def find_mw(compound):
    #disallow number prefix
    if compound and is_number(compound[0]):
        raise ValueError("Number prefix unallowed")
    
    #initialize MW as 0
    mw = 0
    
    #initialize element token
    e = ""
    
    #initialize subscript
    num = ""
    
    #initialize potential subsets
    parens = []
    s = []
    s_num = ""
    s_mw = 0
    
    #iterate through characters in compound
    i = 0
    length = len(compound)
    while i < length:
        #check if parenthases
        if compound[i] == "(":
            #calculate any stored element tokens and reset them
            if e:
                mw += elements[e].MW * to_int(num)
                num = ""
                e = ""
                
            #store active parenthases
            parens.append(compound[i])
            
            #add new subset to subset list
            s.append([])
            i += 1
            continue
            
        #while inside parenthases
        if parens:
            
            #termination of a subset
            if compound[i] == ")":
                parens.pop()
                j = i + 1
                
                #check for subscript
                while j < length and is_number(compound[j]):
                    s_num += compound[j]
                    j += 1
                
                #calculate MW of subset recursively
                if parens:
                    #add to current subset
                    s_mw = (find_mw(s.pop()) + s_mw) * to_int(s_num)
                else:
                    #add to overall MW
                    mw += (find_mw(s.pop()) + s_mw) * to_int(s_num)
                    s_mw = 0
                
                #return if compound fully parsed
                if j == length:
                    #raise error if missing parenthases
                    if parens:
                        raise SyntaxError("Missing parenthases")
                    return mw
                else:
                    i = j
                    s_num = ""
                    
            #add characters to subset string
            else:
                s[len(parens) - 1].append(compound[i])
                i += 1
            continue
        
        #add to current number token if number
        if is_number(compound[i]):
            num += compound[i]     
            
        #calculate and set new element token if capital letter
        elif compound[i] == compound[i].upper():
            if e:
                mw += elements[e].MW * to_int(num)
                num = ""
            e = compound[i]
        
        #otherwise add to existing element token
        else:
            e += compound[i]    
        i += 1
    
        #calculate final piece
        if i == length:
            mw += elements[e].MW * to_int(num)
    
    return mw

def main():
    #prompt user input
    print("MW Calculator\n")
    while True:
        compound = input("Enter compound (Enter 0 to return to khem menu) >> ")
        if compound == "0":
            return
        try:
            print("\nThe MW of %s is: %s\n" % (compound, find_mw(compound)))
        except:
            print("\nInvalid input\n")
        
#testing
"""
#6
print(find_mw("((H)3)2"))
#25
print(find_mw("H2(H(H))2H(HH(H(H))2)3"))
"""
