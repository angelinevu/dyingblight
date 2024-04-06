#Angeline Vu, CS302-001, 03/20/2024
#This file contains the infected class interfaces
#Mob damage is based off survivor health. Global constants
#of the divisors to base damage are included

import random as rand
from time import sleep
from survivor import SURVIVOR_HP
from items import W1_NAME, W2_NAME, W3_NAME

#Sleep time
SLEEP = 0.5

#Global constants divisors
BITER_D = 5
BOMBER_D = 2
VOLATILE_D = 2

#Zombie classes
#Biter class
class biter():
    def __init__(self):     #No members
        pass

    def _unharmed(self):    #Attack with W2 or W3
        sleep(SLEEP)
        print("\nYou successfully killed the biter.\nNo damage taken.")
        return 0

    def _W1(self):       #Attack with W1 
        sleep(SLEEP)
        print(f"\nThe biter scratched you as you fought.\n🖤 {SURVIVOR_HP/(BITER_D * 2)} damage taken. You killed the biter.")
        return int(SURVIVOR_HP/(BITER_D * 2))
    
    def _unarmed(self):     #No weapon
        sleep(SLEEP)
        print(f"\nThe biter bit you, tearing at your skin.\n🖤 {SURVIVOR_HP/BITER_D} damage taken. You fled from the biter.")
        return int(SURVIVOR_HP/BITER_D)

    def attack(self, weapon):               #Determines Attack
        if not isinstance(weapon, str):     #Type Error
            raise TypeError("String Value Expected")

        if weapon == W1_NAME:
            return self._W1()
        
        #W2 or W3 instance
        if weapon == W2_NAME or weapon == W3_NAME:
            return self._unharmed()
        
        return self._unarmed()   #No weapon

    def __del__(self):
        pass

#Derived bomber class
class bomber():
    def __init__(self):     #No members
        pass
    
    def _unharmed(self):     #W2 or W3
        sleep(SLEEP)
        print("\nKeeping your distance, you manage to explode\nthe bomber far from you. No damage taken.")
        return 0

    def _W1(self):
        print("\nYou face the bomber, knife in hand.\n")
        sleep(SLEEP)
        print(f"The bomber exploded near you. You have\nsustained moderate injuries.\n🖤 {SURVIVOR_HP/BOMBER_D} damage taken.")
        return int(SURVIVOR_HP/BOMBER_D)

    def _unarmed(self):
        print("\nYou face the bomber unarmed.")
        sleep(SLEEP)
        print(f"\nA bomber exploded in your face. You have\nsustained lethal injuries.\n🖤 {SURVIVOR_HP} damage taken.")
        return SURVIVOR_HP

    def attack(self, weapon):
        if not isinstance(weapon, str):     #Type Error
            raise TypeError("String Value Expected")

        if weapon == W1_NAME:
            return self._W1()
        
        #W2 or W3 instance
        elif weapon == W2_NAME or weapon == W3_NAME:
            return self._unharmed()
        
        return self._unarmed()   #No weapon

    def __del__(self):
        pass

#Derived volatile class
class volatile():
    def __init__(self):     #No members
        pass
    
    def _unarmed(self):     #No W2 or W3
        print("\nYou attempt to catch the volatile off guard.\nHowever, no damage was dealt to the\nspecial infected.")
        sleep(SLEEP)
        print(f"\nThe volatile lunged and preyed on you. You\nsustained lethal injuries.\n🖤 {SURVIVOR_HP * 3/2} damage taken.")
        return SURVIVOR_HP * 3/2

    def _W2(self):       #W2
        print(f"\nYou shot the volatile. The volatile\nscratched you as you fled.")
        sleep(SLEEP)
        damage = SURVIVOR_HP/(VOLATILE_D)
        if rand.randint(0, 1) == 1:
            print("\nThe volatile spat at you.")
            sleep(SLEEP)
            damage += SURVIVOR_HP/(VOLATILE_D * 2)
        print(f"\nYou successfully escaped the volatile.\n🖤 {damage} damage taken.")
        return damage

    def _W3(self):   #W3
        print("\nYou creep your way closer to the\nvolatile.")
        sleep(SLEEP)
        print(f"\nYou throw a grenade at the volatile\nand flee as it is disoriented.\n")
        sleep(SLEEP)
        print("You successfully escaped the volatile.\nNo damage taken.")
        return 0

    def attack(self, weapon):   #Attack 
        sleep(SLEEP)
        if not isinstance(weapon, str):   #Type Error
            raise TypeError("String Value Expected")

        if weapon == W2_NAME:       #W2 attack
            return self._W2()
        
        #W2 or W3 instance
        elif weapon == W3_NAME:     #W3 attack
            return self._W3()
        
        return self._unarmed()   #No weapon

    def __del__(self):
        pass
