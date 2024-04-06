import pytest
import items

#Angeline Vu, CS302-001, 03/20/2024
#this file holds test functions for the items
#file

#Constructor
def test__item__init__():             
    test = items.item("Knife", 1)       #Correct input
    assert test._name == "Knife"
    assert test._stat == 1

    with pytest.raises(TypeError, match = "String Value Expected"):    #Int -> String
        catching = items.item(1, 1)

    with pytest.raises(TypeError, match = "Number Value Expected"):     #String -> Int
        catching = items.item("Knife", "Knife")

    with pytest.raises(ValueError, match = "Positive Value Expected"):    #Int -> String
        catching = items.item("Knife", -1)
    return

def test_display_item(capsys):      #Display item info
    test = items.item("Knife", 1)
    test.display()
    output = capsys.readouterr()
    assert "Knife\t\tStat: 1" in output.out
    return

#Get name
def test_get_name(): 
    test = items.item("Knife", 1)       #Correct input
    assert test.get_name() == "Knife"
    return

def test__eq__():                   #== Overloader
    test = items.item("Knife", 1)       #Correct input

    with pytest.raises(TypeError, match = "String or Item Value Expected"):    #Int -> String
        catching = test == 1
    assert test == "Knife"
    assert not test == "A"
    return

def test__ne__():                   #!= Overloader
    test = items.item("Knife", 1)       #Correct input

    with pytest.raises(TypeError, match = "String or Item Value Expected"):    #Int -> String
        catching = test != 1
    assert test != "a"
    assert not test != "Knife"
    return

def test__gt__():                       #Overload >
    test = items.item("Knife", 1)       #Correct input
    with pytest.raises(TypeError, match = "String or Item Value Expected"):    #Int -> String
        catching = test > 1
    assert test > "A"
    assert not test > "Knife"
    return

def test__ge__():      #>= Overloader
    test = items.item("Knife", 1)
    with pytest.raises(TypeError, match = "String or Item Value Expected"):    #Int -> String
        catching = test >= 1
    assert test >= "A"
    assert test >= "Knife"
    assert not test >= "Z"
    return

def test__lt__():      #< Overloader
    test = items.item("Knife", 1)
    with pytest.raises(TypeError, match = "String or Item Value Expected"):    #Int -> String
        catching = test < 1
    assert test < "Z"
    assert not test < "A"
    return

def test__le__():       #<= Overloader
    test = items.item("Knife", 1)
    with pytest.raises(TypeError, match = "String or Item Value Expected"):    #Int -> String
        catching = test <= 1
    assert test <= "Z"
    assert test <= "Knife"
    assert not test <= "A"
    return

#Use item
def test_use():
    test = items.item("Knife", 1)       #Correct input
    assert test.use() == 0              
    return

#Derived Class Food
def test__food__init__():   
    test = items.food("Pita", 1, 1)       #Correct input
    assert test._name == "Pita"
    assert test._stat == 1
    assert test._fp == 1

    with pytest.raises(TypeError, match = "String Value Expected"):    #Int -> String
        catching = items.food(1, 1, 1)

    with pytest.raises(TypeError, match = "Number Value Expected"):     #String -> Int
        catching = items.food("Pita", "Pita", 1)

    with pytest.raises(ValueError, match = "Positive Value Expected"):     #String -> Int
        catching = items.food("Pita", -1, 1)

    with pytest.raises(TypeError, match = "Number Value Expected"):     #String -> Int
        catching = items.food("Pita", 1, "Pita")

    with pytest.raises(ValueError, match = "Positive Value Expected"):     #String -> Int
        catching = items.food("Pita", 1, -1)
    return

def test_display_food(capsys):
    test = items.food("Knife", 1, 2)
    test.display()
    output = capsys.readouterr()
    assert "Knife\t\tStat: 1\t\tFP+: 2" in output.out
    return

#Use item
def test_use():   
    test = items.food("Pita", 1, 1)       #Correct input
    assert test.use() == 0
    return 

#Get Food Points 
def test_fp():    
    test = items.food("Pita", 1, 1)       #Correct input
    assert test.fp() == 1
    return

#Derived Class Medication
def test__med__init__():                  #Constructor
    test = items.med("Pills", 1, 1)       #Correct input
    assert test._name == "Pills"
    assert test._stat == 1
    assert test._hp == 1

    with pytest.raises(TypeError, match = "String Value Expected"):    #Int -> String
        catching = items.med(1, 1, 1)

    with pytest.raises(TypeError, match = "Number Value Expected"):     #String -> Int
        catching = items.med("Pills", "Pills", 1)

    with pytest.raises(ValueError, match = "Positive Value Expected"):     #String -> Int
        catching = items.med("Pills", -1, 1)

    with pytest.raises(TypeError, match = "Number Value Expected"):     #String -> Int
        catching = items.med("Pills", 1, "Pills")

    with pytest.raises(ValueError, match = "Positive Value Expected"):     #String -> Int
        catching = items.med("Pills", 1, -1)
    return

#Display
def test_display_med(capsys):
    test = items.med("Knife", 1, 2)
    test.display()
    output = capsys.readouterr()
    assert "Knife\t\tStat: 1\t\tHP+: 2" in output.out
    return

#Use item
def test_use():   
    test = items.med("Pills", 1, 1)       #Correct input
    assert test.use() == 0
    return

#Get Med Points 
def test_hp():    
    test = items.med("Pita", 1, 1)       #Correct input
    assert test.hp() == 1
    return
