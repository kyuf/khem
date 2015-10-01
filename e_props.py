"""
This file contains information for the elements stored in the Element class.
The Element class currently holds the symbol, name, and MW of the element.
All Element objects are stored in the elements dictionary. Import this file
when you need to access elemental properties. Additional properties will be
added when necessary
"""
#properties of elements
class Element:
    def __init__(self, NAME, MW):
        self.NAME = NAME
        self.MW = MW

#raw data key
SYM = 0
NAME = 1
MW = 2

#raw values
raw = {
    ("H", "Hydrogen", 1.008),
    ("He", "Helium", 4.003),
    ("Li", "Lithium", 6.941),
    ("Be", "Berylium", 9.012),
    ("B", "Boron", 10.811),
    ("C", "Carbon", 12.011),
    ("N", "Nitrogen", 14.007),
    ("O", "Oxygen", 15.999),
    ("F", "Fluorine", 18.998),
    ("Ne", "Neon", 20.180),
    ("Na", "Sodium", 22.990),
    ("Mg", "Magnesium", 24.305),
    ("Al", "Aluminum", 26.982),
    ("Si", "Silicon", 28.086),
    ("P", "Phosphorus", 30.974),
    ("S", "Sulfur", 32.066),
    ("Cl", "Cholrine", 35.453),
    ("Ar", "Argon", 39.948),
    ("K", "Potassium", 39.098),
    ("Ca", "Calcium", 40.078),
    ("Sc", "Scandium", 44.956),
    ("Ti", "Titanium", 47.867),
    ("V", "Vanadium", 50.942),
    ("Cr", "Chromium", 51.996),
    ("Mn", "Manganese", 54.938),
    ("Fe", "Iron", 55.845),
    ("Co", "Cobalt", 58.845),
    ("Ni", "Nickel", 58.693),
    ("Cu", "Copper", 63.546),
    ("Zn", "Zinc", 65.38),
    ("Ga", "Gallium", 69.723),
    ("Ge", "Germanium", 72.631),
    ("As", "Arsenic", 74.922),
    ("Se", "Selenium", 78.971),
    ("Br", "Bromine", 79.904),
    ("Kr", "Krypton", 84.798),
    ("Rb", "Rubidium", 84.468),
    ("Sr", "Strontium", 87.62),
    ("Y", "Yttrium", 88.906),
    ("Zr", "Zirconium", 91.224),
    ("Nb", "Niobium", 92.906),
    ("Mo", "Molybdenum", 95.95),
    ("Tc", "Technetium", 98.907),
    ("Ru", "Ruthenium", 101.07),
    ("Rh", "Rhodium", 102.906),
    ("Pd", "Palladium", 106.42),
    ("Ag", "Silver", 107.868),
    ("Cd", "Cadmium", 112.411),
    ("In", "Indium", 114.818),
    ("Sn", "Tin", 118.711),
    ("Sb", "Antimony", 121.760),
    ("Te", "Tellurium", 127.6),
    ("I", "Iodine", 126.904),
    ("Xe", "Xenon", 131.294),
    ("Cs", "Cesium", 132.905),
    ("Ba", "Barium", 137.328),
    ("La", "Lanthanum", 138.905),
    ("Ce", "Cerium", 140.116),
    ("Pr", "Praseodymium", 140.908),
    ("Nd", "Neodymium", 144.243),
    ("Pm", "Promethium", 144.913),
    ("Sm", "Samarium", 150.36),
    ("Eu", "Europium", 151.964),
    ("Gd", "Gadolinium", 157.25),
    ("Tb", "Terbium", 158.925),
    ("Dy", "Dysprosium", 162.500),
    ("Ho", "Holmium", 164.930),
    ("Er", "Erbium", 167.259),
    ("Tm", "Thulium", 168.934),
    ("Yb", "Ytterbium", 173.055),
    ("Lu", "Lutetium", 174.967),
    ("Hf", "Hafnium", 178.49),
    ("Ta", "Tantalum", 180.948),
    ("W", "Tungsten", 183.84),
    ("Re", "Rhenium", 186.207),
    ("Os", "Osmium", 190.23),
    ("Ir", "Iridium", 192.217),
    ("Pt", "Platinum", 195.085),
    ("Au", "Gold", 196.967),
    ("Hg", "Mercury", 200.592),
    ("Tl", "Thallium", 204.383),
    ("Pb", "Lead", 207.2),
    ("Bi", "Bismuth", 208.980),
    ("Po", "Polonium", 208.982),
    ("At", "Astatine", 209.987),
    ("Rn", "Radon", 222.018),
    ("Fr", "Francium", 223.020),
    ("Ra", "Radium", 226.025),
    ("Ac", "Actinium", 227.028),
    ("Th", "Thorium", 232.038),
    ("Pa", "Protactinium", 231.036),
    ("U", "Uranium", 238.029),
    ("Np", "Neptunium", 237.048),
    ("Pu", "Plutonium", 244.064),
    ("Am", "Americium", 243.061),
    ("Cm", "Curium", 247.070),
    ("Bk", "Berkelium", 247.070),
    ("Cf", "Californium", 251.080),
    ("Es", "Einsteinium", 254),
    ("Fm", "Fermium", 257.095),
    ("Md", "Mendelevium", 258.1),
    ("No", "Nobelium", 258.1),
    ("Lr", "Lawrencium", 262),
    ("Rf", "Rutherfordium", 261),
    ("Db", "Dubnium", 262),
    ("Sg", "Seaborgium", 266),
    ("Bh", "Bohrium", 264),
    ("Hs", "Hassium", 269),
    ("Mt", "Meitnerium", 268),
    ("Ds", "Darmstadium", 269),
    ("Rg", "Roentgenium", 272),
    ("Cn", "Copernicium", 277),
    ("Uut", "Ununtrium", 286),
    ("Fl", "Flerovium", 289),
    ("Uup", "Ununpentium", 293),
    ("Lv", "Livermorium", 298),
    ("Uus", "Ununseptium", 294),
    ("Uuo", "Ununoctium", 294)
    }

#construct elements dictionary
elements = {e[SYM]: Element(e[NAME], e[MW]) for e in raw}
