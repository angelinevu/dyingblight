from mob import biter, bomber, volatile
import game, pytest
import survivor as s
import inventory as i
from survivor import Death
from items import item, food, med

#Angeline Vu, CS302-001, 03/20/2024
#This file contains test functions for the game file

def test__init__():         #Constructor
    test = game.game()
    assert test._time == 1
    assert test._inventory._root == None
    assert test._survivor._hp == s.SURVIVOR_HP
    assert test._survivor._fp == s.SURVIVOR_FP
    return

def test_safe_menu(monkeypatch):   #Safe zone menu
    test = game.game()
    monkeypatch.setattr("builtins.input", lambda _: "1")
    result = test.safe_menu()
    assert result == '1'

    monkeypatch.setattr("builtins.input", lambda _: "2")
    result = test.safe_menu()
    assert result == '2'

    monkeypatch.setattr("builtins.input", lambda _: "3")
    result = test.safe_menu()
    assert result == '3'
    return

def test_inventory_menu(monkeypatch):   #Safe inventory menu
    test = game.game()
    assert test.inventory_menu() is None        #Empty inventory
    test._inventory.insert(item("1", 1))

    monkeypatch.setattr("builtins.input", lambda _: "1")    #Select 1
    result = test.inventory_menu()
    assert result == '1'

    monkeypatch.setattr("builtins.input", lambda _: "2")    #Select 2
    result = test.inventory_menu()
    assert result == '2'
    return

def test_consume_item(monkeypatch):     #Eat food or use med or drop weapon
    #WEAPON
    test = game.game()     #Drop weapon
    test._inventory.insert(item("Knife", 1))
    monkeypatch.setattr("builtins.input", lambda _: "Knife")    #Select 1
    test.consume_item()
    assert test._inventory._root == None
                            
    test._inventory.insert(item("Knife", 2)) #Drop weapon regardless of stat
    monkeypatch.setattr("builtins.input", lambda _: "Knife")    #Select 1
    test.consume_item()
    assert test._inventory._root == None

    test._inventory.insert(food("Knife", 2, 1)) #Eat 2 stat food (not empty)
    monkeypatch.setattr("builtins.input", lambda _: "Knife")    #Select 1
    test.consume_item()
    assert test._inventory._root.get_item() == food("Knife", 1, 1)
    assert test._survivor._fp == 51

    #Use 1 stat food (empty)
    monkeypatch.setattr("builtins.input", lambda _: "Knife")    #Select 1
    test.consume_item()
    assert test._inventory._root == None
    assert test._survivor._fp == 52

    test._inventory.insert(med("Knife", 2, 1)) #Use 2 stat med (not empty)
    monkeypatch.setattr("builtins.input", lambda _: "Knife")    #Select 1
    test.consume_item()
    assert test._inventory._root.get_item() == med("Knife", 1, 1)
    assert test._survivor._hp == 51

    #Use 1 stat med (empty)
    monkeypatch.setattr("builtins.input", lambda _: "Knife")    #Select 1
    test.consume_item()
    assert test._inventory._root == None
    assert test._survivor._hp == 52
    return
    
def test_mob_menu():    #Mob menu
    test = game.game()
    with pytest.raises(TypeError, match = "Mob Class Expected"):    #Int -> Str
        catching = test.mob_menu(1, "")
    with pytest.raises(TypeError, match = "String Value Expected"):    #Int -> Str
        catching = test.mob_menu(biter, 1)

    #BITER
    test.mob_menu(biter(), "")
    assert test._survivor._hp == 40
    test.mob_menu(biter(), "Knife")
    assert test._survivor._hp == 35
    test.mob_menu(biter(), "Gun")
    test.mob_menu(biter(), "Grenade")
    assert test._survivor._hp == 35

    #Bomber
    test = game.game()
    with pytest.raises(Death, match = "\nYou have died from the infected.\nBetter luck next time."): 
        catching = test.mob_menu(bomber(), "")
    test = game.game()
    test.mob_menu(bomber(), "Knife")
    assert test._survivor._hp == 25
    test.mob_menu(bomber(), "Gun")
    test.mob_menu(bomber(), "Grenade")
    assert test._survivor._hp == 25

    #Volatile
    test = game.game()
    with pytest.raises(Death, match = "\nYou have died from the infected.\nBetter luck next time."): 
        catching = test.mob_menu(volatile(), "")
    test = game.game()
    with pytest.raises(Death, match = "\nYou have died from the infected.\nBetter luck next time."): 
        catching = test.mob_menu(volatile(), "Knife")
    test = game.game()
    test.mob_menu(volatile(), "Gun")
    assert test._survivor._hp == 12.5 or test._survivor._hp == 25
    test.mob_menu(volatile(), "Grenade")
    assert test._survivor._hp == 12.5 or test._survivor._hp == 25
    return

def test_weapon_menu(monkeypatch):  #Pick weapon
    test = game.game()
    monkeypatch.setattr("builtins.input", lambda _: "1")    #Select 1
    result = test.weapon_menu()
    assert result == ""

    monkeypatch.setattr("builtins.input", lambda _: "2")    #Select 2, no items
    result = test.weapon_menu()
    assert result == ""

    monkeypatch.setattr("builtins.input", lambda _: "3")    #Select 2, no items
    result = test.weapon_menu()
    assert result == ""

    monkeypatch.setattr("builtins.input", lambda _: "4")    #Select 2, no items
    result = test.weapon_menu()
    assert result == ""

    test._inventory.insert(item("Knife", 1))
    test._inventory.insert(item("Gun", 1))
    test._inventory.insert(item("Grenade", 1))

    monkeypatch.setattr("builtins.input", lambda _: "2")    #Select 2, has items
    result = test.weapon_menu()
    assert result == "Knife"

    monkeypatch.setattr("builtins.input", lambda _: "3")    #Select 3, has items
    result = test.weapon_menu()
    assert result == "Gun"

    monkeypatch.setattr("builtins.input", lambda _: "4")    #Select 4, has item
    result = test.weapon_menu()
    assert result == "Grenade"

def test_spawn_loot():
    test = game.game()
    with pytest.raises(TypeError, match = "Integer Value Expected"):    #Int -> String
        catching = test.spawn_loot('a')
    with pytest.raises(ValueError, match = "Integer Out of Range"):    #Int -> String
        catching = test.spawn_loot(-1)
    with pytest.raises(ValueError, match = "Integer Out of Range"):    #Int -> String
        catching = test.spawn_loot(101)
    #HERE    

def test_spawn_mob():
    test = game.game()
    with pytest.raises(TypeError, match = "Integer Value Expected"):    #Int -> String
        catching = test.spawn_mob('a')
    with pytest.raises(ValueError, match = "Integer Out of Range"):    #Int -> String
        catching = test.spawn_mob(-1)
    with pytest.raises(ValueError, match = "Integer Out of Range"):    #Int -> String
        catching = test.spawn_mob(101)

    assert test.spawn_mob(0) == None
    assert test.spawn_mob(40) == None
    assert isinstance(test.spawn_mob(41), biter)
    assert isinstance(test.spawn_mob(80), biter)
    assert isinstance(test.spawn_mob(81), bomber)
    assert isinstance(test.spawn_mob(90), bomber)
    assert isinstance(test.spawn_mob(91), volatile)
    assert isinstance(test.spawn_mob(100), volatile)
    return

def test_sleep(capsys):     #Sleep function
    test = game.game()
    test.sleep()
    assert test._time == 2
    assert test._survivor._fp == 40
    output = capsys.readouterr()
    assert f"\nDay {test._time} survived." and "\nGood night." in output.out

    test.sleep()
    assert test._time == 3
    assert test._survivor._fp == 30
    output = capsys.readouterr()
    assert f"\nDay {test._time} survived." and "\nGood night." in output.out

def test_game_over(capsys):
    test = game.game()
    test.game_over()
    output = capsys.readouterr()
    assert f"\nGame Over. You survived {test._time - 1} days.\n" in output.out