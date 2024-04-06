import mob, items, pytest
from survivor import SURVIVOR_HP
from mob import BITER_D, BOMBER_D, VOLATILE_D

#Angeline Vu, CS302-001, 03/20/2024
#This file contains test functions for the mob
#classes

#Attack with gun or grenade
def test_unharmed_biter():    
    test = mob.biter()
    assert test._unharmed() == 0
    return

#Attack with knife 
def test_W1_biter():       
    test = mob.biter()
    assert test._W1() == SURVIVOR_HP/(BITER_D * 2)
    return

#No weapon
def test_unarmed_biter():     
    test = mob.biter()
    assert test._unarmed() == SURVIVOR_HP/BITER_D
    return

def test_attack_biter():               #Determines Attack
    test = mob.biter()

    with pytest.raises(TypeError, match = "String Value Expected"):    #Int -> String
        catching = test.attack(1)
    
    assert test.attack("") == SURVIVOR_HP/BITER_D               #Unarmed
    assert test.attack("Knife") == SURVIVOR_HP/(BITER_D * 2)      #Knife
    assert test.attack("Gun") == 0                                #Unharmed
    assert test.attack("Grenade") == 0                           
    return

#Derived bomber class
#Gun or grenade
def test_unharmed_bomber():    
    test = mob.bomber()
    assert test._unharmed() == 0
    return

def test_W1_bomber():
    test = mob.bomber()
    assert test._W1() == SURVIVOR_HP/BOMBER_D
    return

def test_unarmed_bomber():
    test = mob.bomber()
    assert test._unarmed() == SURVIVOR_HP
    return

def test_attack_bomber():
    test = mob.bomber()
    with pytest.raises(TypeError, match = "String Value Expected"):    #Int -> String
        catching = test.attack(1)
    
    assert test.attack("") == SURVIVOR_HP                  #Unarmed
    assert test.attack("Knife") == SURVIVOR_HP/BOMBER_D      #Knife
    assert test.attack("Gun") == 0                           #Unharmed
    assert test.attack("Grenade") == 0                           
    return

#Derived volatile class
def test_unarmed_volatile():     #No gun or grenade
    test = mob.volatile()
    assert test._unarmed() == SURVIVOR_HP * 3/2
    return

def test_W2_volatile():       #Gun
    test = mob.volatile()
    temp = int(test.attack("Gun"))
    assert temp == int(SURVIVOR_HP/(VOLATILE_D)) or temp == int((3 * SURVIVOR_HP)/(2 * VOLATILE_D))
    return

def test_W3_volatile():   #Grenade
    test = mob.volatile()
    assert test._W3() == 0
    return 
    
def test_attack_volatile():   #Attack 
    test = mob.volatile()
    with pytest.raises(TypeError, match = "String Value Expected"):    #Int -> String
        catching = test.attack(1)
    
    assert test.attack("") == SURVIVOR_HP * 3/2                 #Unarmed
    temp = int(test.attack("Gun"))
    assert temp == int(SURVIVOR_HP/(VOLATILE_D)) or temp == int((3 * SURVIVOR_HP)/(2 * VOLATILE_D))
    assert test.attack("Grenade") == 0                       #Unharmed
    return