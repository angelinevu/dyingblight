import image
import items
import numpy

from mob import biter, bomber, volatile
from survivor import survivor
from time import sleep
from inventory import BST
from random import randint

#Angeline Vu, CS302-001, 03/20/2024
#This file contains functions that carry out gameplay

#Events (loot and mob)
SLEEP = 0.3
EVENTS = 3
SLEEP_HP = 5

#Drop rates: Food for food, M for meds, W for weapon
NONE = 25   #25% chance of nothing... etc.
F1 = NONE + 10
F2 = F1 + 10
F3 = F2 + 5
M1 = F3 + 10
M2 = M1 + 10
M3 = M2 + 5
W1 = M3 + 15
W2 = W1 + 5
W3 = W2 + 5

#Encounter rates for infected:
NONE2 = 40
BITER = NONE2 + 40
BOMBER = BITER + 10
VOLATILE = BOMBER + 10

#% of 100
assert VOLATILE == 100
assert W3 == 100

#Class with application functions
class game():
    def __init__(self):             #Constructor
        self._time = 1              #Days survived
        self._inventory = BST()     #BST inventory
        self._survivor = survivor() #Characters

    def safe_menu(self) -> str:     #Menu at safe zone
        image.line()
        self._survivor.stats()
        selection = ''
        while selection < '1' or selection > '3':
            selection = input("\nSafe Zone\
                                    \n1. Exit Safe Zone\n2. Open Inventory\n3. Sleep to Next Day\n\nSelection: ")
        return selection
        
    def inventory_menu(self):    #Inventory menu
        print("\nOpening inventory...")
        sleep(SLEEP/2)
        image.line()
        print("\nInventory")

        if self._inventory.display() == 0:
            print("Empty Inventory")
            return

        selection = ''
        while selection < '1' or selection > '2':
                selection = input("\n1. Consume/Drop Item\n2. Exit Inventory\n\nSelection: ")
        return selection

    def consume_item(self):
        match = input("Item: ")                          #User input
        hold = self._inventory.retrieve(match)      #Exists? Get data for consumption?
        if hold is None:                                #No match
            print("\nNot Available")
            return
        item = hold.get_item()                          #Real item
        if isinstance(item, items.food):                #Food
            self._survivor.eat(item.fp())               #Survivor gains FP
            print(f"\n1 {match} eaten.")
            if hold.get_item().use() > 0:               #Stats?
                return
        elif isinstance(item, items.med):               #Medication
            self._survivor.heal(item.hp())              #Survivor gains HP
            print(f"\n1 {match} used.")
            if hold.get_item().use() > 0:               #Stats?
                return
        else:                                           #Weapon
            print(f"\n1 {match} dropped.")

        self._inventory.remove_item(match)              #Remove from inventory

        return

    def mob_menu(self, zombie, weapon):
        if not isinstance(weapon, str):
            raise TypeError("String Value Expected")

        if isinstance(zombie, biter):      #Attack biter with selected weapon
            self._survivor.damage(zombie.attack(weapon))
        elif isinstance(zombie, bomber):   #Attack bomber with selected weapon
            self._survivor.damage(zombie.attack(weapon))
        elif isinstance(zombie, volatile):   #Attack volatile with selected weapon
            self._survivor.damage(zombie.attack(weapon))
        else:
            raise TypeError("Mob Class Expected")   #ERROR
        return

    def weapon_menu(self):      #Choose weapon
        selection = ''
        while selection < '1' or selection > '4':
            selection = input(f"\nChoose Weapon\n1. No weapon\n2. {items.W1_NAME} \
                                    \n3. {items.W2_NAME}\n4. {items.W3_NAME}\n\nSelection: ")

        if selection == '1':   
            weapon = ""
        elif selection == '2':
            weapon = items.W1_NAME
        elif selection == '3':
            weapon = items.W2_NAME
        else:
            weapon = items.W3_NAME

        if weapon != "":
            hold = self._inventory.retrieve(weapon)
            if hold is None:
                print(f"\nNo {weapon} in inventory.\nYou have nothing equipped.")
                weapon = ""
            elif hold.get_item().use() == 0 and weapon != "":
                self._inventory.remove_item(weapon)
        return weapon

    def spawn_loot(self, rand): #Spawns loot, takes random number argument
        if not isinstance(rand, int):                       #Error checking
            raise TypeError("Integer Value Expected")
        if rand > 100 or rand < 0:
            raise ValueError("Integer Out of Range")

        #if rand <= NONE:        #No drop
        if rand <= NONE:        #No drop
            print("\nYou searched and found... nothing.")

        #Food drop
        #elif rand <= NONE + F1:                 #Food 1
        elif rand <= F1:                 #Food 1
            print(f"\nYou found 1 {items.F1_NAME} in a cabinet.")
            if self._inventory.insert(items.food(items.F1_NAME, items.F1_STAT, items.F1_FP)) == 0:
                sleep(SLEEP)
                print("Your inventory is full.")
            else:
                print(f"+1 {items.F1_NAME}")

        #elif rand <= NONE + F1 + F2:            #Food 2
        elif rand <= F2:          
            print(f"\nYou found 1 {items.F2_NAME} in a drawer.")
            if self._inventory.insert(items.food(items.F2_NAME, items.F2_STAT, items.F2_FP)) == 0:
                sleep(SLEEP)
                print("Your inventory is full.")
            else:
                print(f"+1 {items.F2_NAME}")

        #elif rand <= NONE + F1 + F2 + F3:       #Food 3
        elif rand <= F3:          
            print(f"\nYou found 1 uncommon {items.F3_NAME} food in a basket.")
            if self._inventory.insert(items.food(items.F3_NAME, items.F3_STAT, items.F3_FP)) == 0:
                sleep(SLEEP)
                print("Your inventory is full.")
            else:
                print(f"+1 {items.F3_NAME}")

        #Medication Drop
        #elif rand <= NONE + F1 + F2 + F3 + M1:          #Med 1
        elif rand <= M1:          
            print(f"\nYou found 1 {items.M1_NAME} in a cabinet.")
            if self._inventory.insert(items.med(items.M1_NAME, items.M1_STAT, items.M1_HP)) == 0:
                sleep(SLEEP)
                print("Your inventory is full.")
            else:
                print(f"+1 {items.M1_NAME}")

        #elif rand <= NONE + F1 + F2 + F3 + M1 + M2:     #Med 2
        elif rand <= M2:
            print(f"\nYou found 1 {items.M2_NAME} on a shelf.")
            if self._inventory.insert(items.med(items.M2_NAME, items.M2_STAT, items.M2_HP)) == 0:
                sleep(SLEEP)
                print("Your inventory is full.")
            else:
                print(f"+1 {items.M2_NAME}")

        #elif rand <= NONE + F1 + F2 + F3 + M1 + M2 + M3:#Med 3
        elif rand <= M3:
            print(f"\nYou found 1 {items.M3_NAME} in a closet.")
            if self._inventory.insert(items.med(items.M3_NAME, items.M3_STAT, items.M3_HP)) == 0:
                sleep(SLEEP)
                print("Your inventory is full.\n")
            else:
                print(f"+1 {items.M3_NAME}")

        #Weapon 3
        #elif rand <= NONE + F1 + F2 + F3 + M1 + M2 + M3 + W1:           #Weapon 1
        elif rand <= W1:
            print(f"\nYou found 1 {items.W1_NAME} in a kitchen.")
            if self._inventory.insert(items.item(items.W1_NAME, items.W1_STAT)) == 0:
                sleep(SLEEP)
                print("Your inventory is full.")
            else:
                print(f"+1 {items.W1_NAME}")

        #elif rand <= NONE + F1 + F2 + F3 + M1 + M2 + M3 + W1 + W2:      #Weapon 2
        elif rand <= W2:
            print(f"\nYou found 1 {items.W2_NAME} in a safe. One bullet remains.")
            if self._inventory.insert(items.item(items.W2_NAME, items.W2_STAT)) == 0:
                sleep(SLEEP)
                print("Your inventory is full.")
            else:
                print(f"+1 {items.W2_NAME}")

        else:                                                           #Weapon 3   
            print(f"\nYou found 1 {items.W3_NAME} in a military bunker.")
            if self._inventory.insert(items.item(items.W3_NAME, items.W3_STAT)) == 0:
                sleep(SLEEP)
                print("Your inventory is full.")
            else:
                print(f"+1 {items.W3_NAME}")
        return            

    def spawn_mob(self, rand):                #Mob encounter
        if not isinstance(rand, int):                       #Error checking
            raise TypeError("Integer Value Expected")
        if rand > 100 or rand < 0:
            raise ValueError("Integer Out of Range")

        #if rand <= NONE2:                     #No infected
        if rand <= NONE2:
            return None
        #if rand <= NONE2 + BITER:             #Biter encounter
        if rand <= BITER:
            print("\nBiter encountered.")
            self._survivor.stats()
            return biter()
        #if rand <= NONE2 + BITER + BOMBER:    #Bomber encounter
        if rand <= BOMBER:
            print("\nBomber encountered.")
            self._survivor.stats()
            return bomber()
        print("\nVolatile encountered.")      #Volatile encounter (else clause)
        self._survivor.stats()
        return volatile()

    def sleep(self):                 #Sleep to next day  
        print(f"\nDay {self._time} survived.")
        sleep(SLEEP)
        print("\nGood night.")
        sleep(SLEEP)
        self._time += 1
        self._survivor.heal(SLEEP_HP)
        self._survivor.hunger()     #Adjust hunger
        return

    def game_over(self):
        print(f"\nGame Over. You survived {self._time - 1} days.\n")
        return
