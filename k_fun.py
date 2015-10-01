"""
This file contains functions and classes that will be frequently used to run
calculations in other files. This file should be imported whenever creating a
new calculation file
"""
from e_props import elements

#return if string can be converted to int
def is_number(n):
    try:
        int(n)
        return True
    except:
        return False

#converts string num to appropriate int
def to_int(num):
    if num:
        return int(num)
    else:
        return 1

#chemical species class
class Species:
    def __init__(self, form, prefix = None, charge = None):
        #chemical formula
        self.form = form
        
        #number prefix
        if is_number(prefix):
            self.prefix = prefix
        else:
            self.prefix = 1
        
        #MW and mole balance
        self.mw, self.moles = self.find_mw()
    
    def __repr__(self):
        return self.form + " Prefix: " + str(self.prefix)
    
    def find_mw(self):
        #should not have number prefix
        if self.form and is_number(self.form[0]):
            raise ValueError("Number prefix unallowed")
        
        #initialize MW as 0
        mw = 0
        
        #initialize mole balance as empty dictionary
        moles = MoleBalance()
        
        #initialize element token
        e = ""
        
        #initialize subscript
        num = ""
        
        #initialize potential subsets
        parens = []
        s = []
        s_num = ""
        s_mw = 0
        s_mol = MoleBalance()
        
        #iterate through characters in compound
        i = 0
        length = len(self.form)
        while i < length:
            #check if parentheses
            if self.form[i] == "(":
                #calculate any stored element tokens and reset them
                if e:
                    num = to_int(num)
                    mw += elements[e].MW * num
                    moles += MoleBalance(e, num)
                    num = ""
                    e = ""
                    
                #store active parentheses
                parens.append(self.form[i])
                
                #add new subset to subset list
                s.append([])
                i += 1
                continue
                
            #while inside parentheses
            if parens:
                
                #termination of a subset
                if self.form[i] == ")":
                    parens.pop()
                    j = i + 1
                    
                    #check for subscript
                    while j < length and is_number(self.form[j]):
                        s_num += self.form[j]
                        j += 1
                    
                    #calculate MW of subset recursively
                    s_num = to_int(s_num)
                    s_spec = Species(s.pop())
                    if parens:
                        #add to current subset
                        s_mw = (s_spec.mw + s_mw) * s_num
                        s_mol = (s_spec.moles + s_mol) * s_num
                    else:
                        #add to overall MW
                        mw += (s_spec.mw + s_mw) * s_num
                        moles += (s_spec.moles + s_mol) * s_num
                        s_mw = 0
                        s_mol.clear()
                    
                    #return if compound fully parsed
                    if j == length:
                        #raise error if missing parentheses
                        if parens:
                            raise SyntaxError("Missing parentheses")
                        return mw, moles
                    else:
                        i = j
                        s_num = ""
                        
                #add characters to subset string
                else:
                    s[len(parens) - 1].append(self.form[i])
                    i += 1
                continue
            
            #add to current number token if number
            if is_number(self.form[i]):
                num += self.form[i]     
                
            #calculate and set new element token if capital letter
            elif self.form[i] == self.form[i].upper():
                if e:
                    num = to_int(num)
                    mw += elements[e].MW * num
                    moles += MoleBalance(e, num)
                    num = ""
                e = self.form[i]
            
            #otherwise add to existing element token
            else:
                e += self.form[i]    
            i += 1
        
            #calculate final piece
            if i == length:
                num = to_int(num)
                mw += elements[e].MW * to_int(num)
                moles += MoleBalance(e, num)
        
        return mw, moles

#mole balance object    
class MoleBalance:
    #balance can be initiated empty or with one species
    def __init__(self, species = None, count = None):
        if species:
            self.balance = {species: count}
        else:
            self.balance = {}
    
    #clear the current balance
    def clear(self):
        self.balance = {}
    
    #add one balance to another
    def __add__(self, other):
        for k, v in other.balance.items():
            if k in self.balance:
                self.balance[k] += v
            else:
                self.balance[k] = v
        return self
    
    #+= operation
    def __iadd__(self, other):
        self = self + other
        return self
    
    #multiply balance by a factor
    def __mul__(self, factor):
        for k, v in self.balance.items():
            self.balance[k] = v * factor
        return self
    
    #print mole balance
    def __repr__(self):
        string = ""
        for k, v in self.balance.items():
            string += "%s: %s\n" % (k, v)
        return string

#object to store reactants and products in lists
class SpecList:
    def __init__(self, name):
        self.name = name
        self.list = []
        self.moles = MoleBalance()
    
    def append(self, spec):
        self.list.append(spec)
        self.moles += spec.moles * spec.prefix

    def __repr__(self):
        print(self.name + "..")
        for spec in self.list:
            print(spec)
        return ""
