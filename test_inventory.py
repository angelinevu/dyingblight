from inventory import LLL_node, LLL, BST_node, BST
from items import item, food, med
import pytest

#LLL_Node
def test__init__LLL_node():
    with pytest.raises(TypeError, match = "Item Value Expected"):    #Str -> int
        catching = LLL_node(1)
    
    with pytest.raises(TypeError, match = "String Value Expected"):  #...other cases tested in in test_item
        catching = LLL_node(item(1, 1))

    test = LLL_node(item("Knife", 1))   #Insert weapon
    test._data._name == "Knife"
    test._data._stat == 1
    test._next == None

    test = LLL_node(food("Knife", 1, 1))    #Insert food
    test._data._name == "Knife"
    test._data._stat == 1
    test._data._fp == 1
    test._next == None

    test = LLL_node(med("Knife", 1, 1))     #Insert med
    test._data._name == "Knife"
    test._data._stat == 1
    test._data._hp == 1
    test._next == None
    return

def test_get_data_LLL_node():        #Test Getter
    test = LLL_node(item("Knife", 1))   #Insert weapon
    assert test.get_data() == item("Knife", 1)

    test = LLL_node(food("Knife", 1, 1))   #Insert weapon
    assert test.get_data() == food("Knife", 1, 1)

    test = LLL_node(med("Knife", 1, 1))   #Insert weapon
    assert test.get_data() == med("Knife", 1, 1)
    return

def test_display_LLL_node(capsys):          #Display contents
    test = LLL_node(item("Knife", 1))   #Insert weapon
    test.display()
    output = capsys.readouterr()
    assert f"Knife\t\tStat: 1" in  output.out

    test = LLL_node(food("Knife", 1, 1))   #Insert weapon
    test.display()
    output = capsys.readouterr()
    assert f"Knife\t\tStat: 1\t\tFP+: 1" in  output.out

    test = LLL_node(med("Knife", 1, 1))   #Insert weapon
    test.display()
    output = capsys.readouterr()
    assert f"Knife\t\tStat: 1\t\tHP+: 1" in  output.out
    return

def test_get_next_LLL_node():         #Get next
    test = LLL_node(item("Knife", 1))   #Insert weapon
    assert test._next == None
    return

def test_set_next_LLL_node():   #Set next
    test = LLL_node(item("Knife", 1))   #Insert weapon
    with pytest.raises(TypeError, match = "LLL Node Value Expected"): 
        catching = test.set_next(1)

    test2 = LLL_node(item("Knife", 1))   #Insert weapon
    test.set_next(test2)
    test._next == test2
    test.set_next(None)
    test._next is None
    return

#LLL
def test__init__LLL():   #Constructor with argument
    with pytest.raises(TypeError, match = "Item Value Expected"):    #Str -> int
        catching = LLL(1)
    with pytest.raises(TypeError, match = "String Value Expected"):  #...other cases tested in in test_item
        catching = LLL(item(1, 1))
    
    test = LLL(item("Knife", 1))        #Weapon
    assert test._head.get_data() == item("Knife", 1)
    assert test._count == 1

    test = LLL(food("Knife", 1, 1))     #Food
    assert test._head.get_data() == food("Knife", 1, 1)
    assert test._count == 1

    test = LLL(med("Knife", 1, 1))      #Med
    assert test._head.get_data() == med("Knife", 1, 1)
    assert test._count == 1
    return

def test_get_data_LLL():     #Get data
    test = LLL(item("Knife", 1))        #Weapon
    assert test.get_data() == item("Knife", 1)

    test = LLL(med("Knife", 1, 1))      #Med
    assert test.get_data() == med("Knife", 1, 1)

    test = LLL(food("Knife", 1, 1))     #Food
    assert test.get_data() == food("Knife", 1, 1)
    return

def test_display_LLL(capsys):  #Displays item
    test = LLL(item("Knife", 1))    #One item
    test.display()
    output = capsys.readouterr()
    assert "Knife\t\tStat: 1\n" in output.out

    #Unsure of how to test multiple outputs...
    test.insert(item("Knife", 1))   #Multiple items
    test.display()
    assert "Knife\t\tStat: 1\n" in output.out
    return

def test_insert_LLL():  #Add a new item to LLL
    test = LLL(item("Knife", 1))
    with pytest.raises(TypeError, match = "Item Value Expected"):    #Str -> int
        catching = test.insert(1)
    test.insert(item("Knife", 1))  #Add and check
    assert test._head._data == item("Knife", 1) \
        and test._head.get_next()._data == item("Knife", 1)

def test_delete_LLL():  #Deletes an item from the LLL
    test = LLL(item("Knife", 1))
    test.delete()
    assert test._head is None
    with pytest.raises(TypeError, match = "Empty List"):    #Empty del
        catching = test.delete()

    test = LLL(item("Knife", 1))
    test.insert(item("Knife", 1))  #Add and check
    test.delete()
    assert test._head._data == item("Knife", 1) \
        and test._head.get_next() is None
    test.delete() 
    assert test._head == None
    return

#BST_Node
def test__init__BST_node():     #Constructor for BST_Node
    with pytest.raises(TypeError, match = "Item Value Expected"):    #Wrong data
        catching = BST_node(1)

    test = BST_node(item("Knife", 1))
    assert test._head._head.get_data() == item("Knife", 1)
    assert test._left == None
    assert test._right == None

    test = BST_node(food("Knife", 1, 1))
    assert test._head._head.get_data() == food("Knife", 1, 1)
    assert test._left == None
    assert test._right == None

    test = BST_node(med("Knife", 1, 1))
    assert test._head._head.get_data() == med("Knife", 1, 1)
    assert test._left == None
    assert test._right == None
    return

def test_get_LLL():     #Get LLL
    test = BST_node(item("Knife", 1))
    LLL = test.get_LLL()
    assert LLL._head._data == item("Knife", 1)
    assert LLL._head._next is None
    return

def test_get_item():     #Get item
    test = BST_node(item("Knife", 1))
    assert test.get_item() == item("Knife", 1)
    return
    
def test_get_left():     #Get left node
    test1 = BST_node(item("Knife", 1))
    test2 = BST_node(item("Knife", 1))
    test1._left = test2
    assert test1.get_left() == test2
    test1._left = None
    assert test1.get_left() == None
    return

def test_get_right():     #Get right node
    test1 = BST_node(item("Knife", 1))
    test2 = BST_node(item("Knife", 1))
    test1._right = test2
    assert test1.get_right() == test2
    test1._right = None
    assert test1.get_right() == None
    return

def test_set_left():    #Set left ptr
    test1 = BST_node(item("Knife", 1))
    test2 = BST_node(item("Knife", 1))
    
    with pytest.raises(TypeError, match = "BST_Node Value Expected"):    #Wrong data
        catching = test1.set_left(1)

    test1.set_left(test2)
    assert test1._left == test2
    return

def test_set_left():    #Set right ptr
    test1 = BST_node(item("Knife", 1))
    test2 = BST_node(item("Knife", 1))
    
    with pytest.raises(TypeError, match = "BST_Node Value Expected"):    #Wrong data
        catching = test1.set_right(1)

    test1.set_right(test2)
    assert test1._right == test2
    return

def test__init__BST():  #Constructor
    test = BST()
    assert test._root == None
    return

def test_insert_BST():  #Insert BST
    test = BST()        #One item 
    test.insert(item("B", 1))
    assert test._root.get_item() == item("B", 1)

    test = BST()        #One food
    test.insert(food("B", 1, 1))
    assert test._root.get_item() == food("B", 1, 1)

    del test
    test = BST()        #One med
    test.insert(med("B", 1, 1))
    assert test._root.get_item() == med("B", 1, 1)

    test.insert(item("A", 1))   #Add left
    assert test._root.get_left().get_item() == item("A", 1)

    test.insert(item("C", 1))   #Add right
    assert test._root.get_right().get_item() == item("C", 1)

    test.insert(item("C", 1))   #Add right
    #Duplicate
    assert test._root.get_right().get_item() == item("C", 1) \
        and test._root._right._head._head._next.get_data() == item("C", 1)
    
    assert test.insert(item("C", 1)) == None  #Full
    return

def test_display_BST(capsys):   #Display BST
    test = BST()
    assert test.display() == 0
    test.insert(item("A", 1))
    test.display()
    output = capsys.readouterr()
    assert "A\t\tStat: 1\n" in output.out
    #Not sure how to test multiple outputs...

def test_retrieve_BST():    #Retrieve BST node with match
    test = BST()
    test.insert(item("B", 1))   #Populate lists
    test.insert(item("A", 1))
    test.insert(item("C", 1))

    with pytest.raises(TypeError, match = "Item Value Expected"): 
        catching = test.retrieve(1)
    
    #Allow string & item type; validate...
    assert test.retrieve("B") == test.retrieve(item("B", 1))   
    assert test.retrieve("B").get_item() == item("B", 1)

    assert test.retrieve("A") == test.retrieve(item("A", 1))
    assert test.retrieve("A").get_item() == item("A", 1)

    assert test.retrieve("C") == test.retrieve(item("C", 1))
    assert test.retrieve("C").get_item() == item("C", 1)

    assert test.retrieve("D") is None            #No match
    assert test.retrieve(item("D", 1)) is None   #No match
    return

def test_remove_item_BST(): #Remove items from tree
    test = BST()
    assert test.remove_item("") == 0    #Empty list

    test.insert(item("B", 1))   #Root, no children
    test.remove_item("B")
    assert test._root == None

    test.insert(item("B", 1))   #Root, duplicates
    test.insert(item("B", 1))  
    test.remove_item("B")
    assert test._root.get_item() == "B"

    test = BST()
    test.insert(item("B", 1))   #Root, L child
    test.insert(item("A", 1)) 
    test.remove_item("B")
    assert test._root.get_item() == item("A", 1)
    assert test._root._left is None and test._root._right is None

    test = BST()
    test.insert(item("B", 1))   #Root, R child
    test.insert(item("C", 1)) 
    test.remove_item("B")
    assert test._root.get_item() == item("C", 1)
    assert test._root._left is None and test._root._right is None

    test = BST()
    test.insert(item("B", 1))   #Root, two children
    test.insert(item("A", 1)) 
    test.insert(item("C", 1)) 
    test.remove_item("B")
    assert test._root._right == None
    assert test._root.get_item() == item("C", 1)        #New root
    assert test._root._left.get_item() == item("A", 1)  #L of root
    assert test._root._left._right == None
    assert test._root._left._left == None

    test = BST()
    test.insert(item("B", 1))   #Del leaf
    test.insert(item("C", 1))   
    test.remove_item("C")       
    assert test._root._left == None
    assert test._root._right == None

    test.insert(item("C", 1))   #1 R child
    test.insert(item("D", 1))   
    test.remove_item("C")       
    assert test._root._left == None
    assert test._root._right.get_item() == "D"  #Still here

    test.insert(item("C", 1))   #1 L child
    test.remove_item("D")       
    assert test._root._left == None
    assert test._root._right.get_item() == "C"  #Still here

    test = BST()
    test.insert(item("A", 1))   #2 children, IOS directly to R
    test.insert(item("C", 1))  
    test.insert(item("B", 1))  
    test.insert(item("D", 1))  
    test.remove_item("C")       
    assert test._root.get_item() == "A"         #Root
    assert test._root._right.get_item() == "D"  #Right child
    assert test._root._right._right == None     #No right of D
    assert test._root._right._left.get_item() == "B"    #Left of D
    assert test._root._right._left._left == None        #Leaf
    assert test._root._right._left._right == None

    test = BST()
    test.insert(item("A", 1))   #2 children, find IOS
    test.insert(item("C", 1))  
    test.insert(item("B", 1))  
    test.insert(item("F", 1))  
    test.insert(item("D", 1))  
    test.insert(item("E", 1))  

    test.remove_item("C")      
    assert test._root.get_item() == "A"         #Root
    assert test._root._left == None
    assert test._root._right.get_item() == "D"  #Right of root
    assert test._root._right._left.get_item() == "B"    #Left of D
    assert test._root._right._left._left == None \
        and test._root._right._left._right == None      #Leaf
    assert test._root._right._right.get_item() == "F"   #Right of D
    assert test._root._right._right._right == None      #No R kid
    assert test._root._right._right._left.get_item() == "E" #Left of F
    assert test._root._right._right._left._left == None \
        and test._root._right._right._left._right == None   #Leaf

    assert test.remove_item("") == 0    #No match
    return




