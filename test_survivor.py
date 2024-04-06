#Angeline Vu

#This file holds test functions for the class
#survivor

import survivor as s, pytest
from survivor import PROTAGONIST, SURVIVOR_FP, SURVIVOR_HP, HUNGER

#Constructor
def test__init__():                 
    test = s.survivor()
    assert test._name == PROTAGONIST    
    assert test._hp == SURVIVOR_HP       
    assert test._fp == SURVIVOR_FP       
    return

#Display stats
def test_stats(capsys):   
    test = s.survivor()
    assert test.stats() == SURVIVOR_HP
    output = capsys.readouterr()
    assert "\n❤️  HP: 50.0\n🥩 FP: 50.0\n" in output.out
    return

#-HP
def test_damage():   
    test = s.survivor()
    test.damage(5)
    assert test._hp == SURVIVOR_HP - 5
    return

#-FP
def test_hunger():    
    test = s.survivor()
    test.hunger()
    assert test._fp == SURVIVOR_FP - HUNGER
    return

#+HP
def test_heal():
    test = s.survivor()
    test.heal(SURVIVOR_HP)
    assert test._hp == SURVIVOR_HP * 2
    return

#+FP
def test_eat():
    test = s.survivor()
    test.eat(SURVIVOR_FP)
    assert test._fp == SURVIVOR_FP * 2
    return