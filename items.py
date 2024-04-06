#Angeline Vu, CS302-001, 03/20/2024
#This file contains the item class and the types of items. 
#The file contains global constants for the stats of items.

#Global constants for item types: W for weapon, F for food, M for meds
#Weapon types
W1_NAME = "Knife"
W1_STAT = 3              
W2_NAME = "Gun"
W2_STAT = 1
W3_NAME = "Grenade"
W3_STAT = 1

#Food types
F1_NAME = "Energy Bar"
F1_FP = 10                 
F1_STAT = 1

F2_NAME = "Dried Fruit" 
F2_FP = 10               
F2_STAT = 2

F3_NAME = "Pita"
F3_FP = 20
F3_STAT = 2

#Medication types
M1_NAME = "Pills"
M1_HP = 5      
M1_STAT = 3

M2_NAME = "Bandages"
M2_HP = 10 
M2_STAT = 2

M3_NAME = "Medkit"
M3_HP = 50   
M3_STAT = 1

#Base Class Item
class item():               #Class Item, Weapons will be of this type
    def __init__(self, name: str, stat: int):   #Constructor
        if not isinstance(name, str) or name == "":
            raise TypeError("String Value Expected")
        if not isinstance(stat, int):           #type(stat) = int
            raise TypeError("Number Value Expected")
        if stat < 0:                            #Negative durability
            raise ValueError("Positive Value Expected")

        self._name = name
        self._stat = stat
        return
    
    def display(self):      #Display item info
        if len(self._name) > 7:
            print(f"{self._name}\tStat: {self._stat}", end= "")
        else:
            print(f"{self._name}\t\tStat: {self._stat}", end= "")
        return
    
    def use(self) -> int:   #--Durability
        self._stat -= 1
        return self._stat

    def get_name(self) -> str:  #Get name
        return self._name

    def __eq__(self, match) -> bool:    #== Overload for string && items
        if isinstance(match, str):      #String instance
            return self._name == match
        elif isinstance(match, item):   #Item instance
            return self._name == match.get_name()
        raise TypeError("String or Item Value Expected")

    def __ne__(self, match) -> bool:    #!= Overload
        if isinstance(match, str):      #String instance
            return self._name != match
        elif isinstance(match, item):   #Item instance
            return self._name != match.get_name()
        raise TypeError("String or Item Value Expected")

    def __gt__(self, match) -> bool:    #> Overload
        if isinstance(match, str):      #String instance
            return self._name > match
        elif isinstance(match, item):   #Item instance
            return self._name > match.get_name()
        raise TypeError("String or Item Value Expected")

    def __ge__(self, match) -> bool:    #>= Overload
        if isinstance(match, str):      #String instance
            return self._name >= match
        elif isinstance(match, item):   #Item instance
            return self._name >= match.get_name()
        raise TypeError("String or Item Value Expected")

    def __lt__(self, match) -> bool:    #< Overload
        if isinstance(match, str):      #String instance
            return self._name < match
        elif isinstance(match, item):   #Item instance
            return self._name < match.get_name()
        raise TypeError("String or Item Value Expected")

    def __le__(self, match) -> bool:    #<= Overload
        if isinstance(match, str):      #String instance
            return self._name <= match
        elif isinstance(match, item):   #Item instance
            return self._name <= match.get_name()
        raise TypeError("String or Item Value Expected")

    def __del__(self):      #Destructor
        self._name = ""     #Name of Item
        self._stat = 0      #Durability
        return 

#Derived Class Food
class food(item):           #Food Class
    def __init__(self, name: str, stat: int, fp: int):   #Constructor
        super().__init__(name, stat)
        if not isinstance(fp, int):                      #type(fp) = int
            raise TypeError("Number Value Expected")
        if fp < 0:                                       #fp > 0
            raise ValueError("Positive Value Expected")

        self._fp = fp
        return

    def display(self):
        super().display()
        print(f"\t\tFP+: {self._fp}", end="")
        return
    
    def fp(self) -> int:    #Return FP
        return self._fp

    def __del__(self):      #Destructor: set data items to 0 equivalent
        super().__del__()   
        self._fp = 0        
        return

#Derived Class Medication
class med(item):
    def __init__(self, name: str, stat: int, hp: int):   #Constructor
        super().__init__(name, stat)
        if not isinstance(hp, int):                      #type(fp) = int
            raise TypeError("Number Value Expected")
        if hp < 0:                                       #fp > 0
            raise ValueError("Positive Value Expected")

        self._hp = hp
        return

    def display(self):
        super().display()
        print(f"\t\tHP+: {self._hp}", end="")
        return
        
    def hp(self) -> int:   #Return HP
        return self._hp

    def __del__(self):      #Destructor: set data items to 0 equivalent
        super().__del__()   
        self._hp = 0         
        return