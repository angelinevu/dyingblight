#Angeline Vu, CS302-001, 03/20/2024
#This file contains the survivor class which the 
#client will be playing as

#Global constants
PROTAGONIST = "Kyle Crane"   #Protagonist name
SURVIVOR_HP = 50             #Hit points
SURVIVOR_FP = 50             #Food points
HUNGER = 10                  #Hunger pangs

#Class survivor
class survivor():
    def __init__(self):                 #Default constructor
        self._name = PROTAGONIST        #Sets name
        self._hp = SURVIVOR_HP          #Sets hit points
        self._fp = SURVIVOR_FP          #Sets food points
        return

    def stats(self) -> int:                    #Display stats
        print(f"\nKyle Crane\n❤️  HP: {float(self._hp)}\n🥩 FP: {float(self._fp)}")
        return self._hp

    def damage(self, dmg):              #-HP
        if not isinstance(dmg, int) and not isinstance(dmg, float):    
            raise TypeError
        if dmg < 0:                     #Not in range
            raise ValueError

        self._hp -= dmg
        if self._hp <= 0:
            raise Death("the infected")
        return
    
    def hunger(self):                   #-FP
        self._fp -= HUNGER
        if self._fp <= 0:
            raise Death("starvation")
        return
    
    def heal(self, hp):                 #+HP
        if not isinstance(hp, int):     #Not an integer
            raise TypeError        
        if hp < 0:                      #Not in range
            raise ValueError

        self._hp += hp
        if self._hp > SURVIVOR_HP * 2:
            self._hp = SURVIVOR_HP * 2
        return
    
    def eat(self, pts):                 #+FP
        if not isinstance(pts, int):    #Not an integer
            raise TypeError
        if pts < 0:                     #Not in range
            raise ValueError            

        self._fp += pts
        if self._fp > SURVIVOR_FP * 2:
            self._fp = SURVIVOR_FP * 2
        return

    def __del__(self):                  #Destructor
        self._name = 0
        self._hp = 0
        self._fp = 0 
        return

class Death(Exception):                 #Death exception
    def __init__(self, cause):
        self.message = f"\nYou have died from {cause}.\nBetter luck next time."
        super().__init__(self.message)

 
