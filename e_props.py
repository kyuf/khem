#properties of elements
class Element:
    def __init__(self, NAME, MW):
        self.NAME = NAME
        self.MW = MW

elements = {
    "H": Element("Hydrogen", 1.008),
    "He": Element("Helium", 4.003),
    "Li": Element("Lithium", 6.941),
    "Be": Element("Berylium", 9.012),
    "B": Element("Boron", 10.811),
    "C": Element("Carbon", 12.011),
    "N": Element("Nitrogen", 14.007),
    "O": Element("Oxygen", 15.999),
    "F": Element("Fluorine", 18.998),
    "Ne": Element("Neon", 20.180),
    "Na": Element("Sodium", 22.990),
    "Mg": Element("Magnesium", 24.305)
    }
