import items

DUPLICATES = 2

class LLL_node():               #LLL Node
    def __init__(self, data):   #Constructor
        if not isinstance(data, items.item):
            raise TypeError("Item Value Expected")

        self._data = data
        self._next = None
        return
    
    def get_data(self):         #Get data (item)
        return self._data

    def display(self):          #Display contents
        self._data.display()
        return
    
    def get_next(self):         #Get next
        return self._next
    
    def set_next(self, new_next):   #Set next
        if not isinstance(new_next, LLL_node) and new_next is not None:
            raise TypeError("LLL Node Value Expected")

        self._next = new_next
        return
    
    def __del__(self):              #Destructor
        self._data = None
        self._next = None

class LLL():    #Class LLL (inside BST node)
    def __init__(self, data):   #Constructor with argument
        if not isinstance(data, items.item):
            raise TypeError("Item Value Expected")

        self._head = LLL_node(data)
        self._count = 1
        return

    def get_data(self):         #Returns item data
        return self._head.get_data()
    
    def display(self):          #Displays item
        if self._head == None:
            return 0
        return self.__display__(self._head)

    def __display__(self, head):
        if head == None:
            return 1
        head.display()
        print()
        return self.__display__(head.get_next())

    def insert(self, data) -> int:     #Insert in LLL of duplicates
        if not isinstance(data, items.item):
            raise TypeError("Item Value Expected")
        
        if self._count >= DUPLICATES:     #Exceeds max count of DUPLICATES
            return 0                      #Return 0 for failure

        self._count += 1

        hold = self._head        
        self._head = LLL_node(data)
        self._head.set_next(hold)
        return 1                          #Return 1 for success

    def delete(self) -> int:    #Delete item
        if self._head is None:
            raise TypeError("Empty List")

        hold = self._head.get_next()
        del self._head
        self._head = hold
        self._count -= 1
        return self._count      #Returns count; if 0, delete BST node

    def __del__(self):          #Destructor
        self._head = None
        return

#Tree node class
class BST_node():
    def __init__(self, data):       #Constructor with argument
        if not isinstance(data, items.item):
            raise TypeError("Item Value Expected")

        self._head = LLL(data)
        self._left = None
        self._right = None
        return

    def get_LLL(self):             #Get LLL
        return self._head
    
    def get_item(self):            #Get defining item of LLL
        return self._head.get_data()

    def get_left(self):             #Get left child
        return self._left

    def get_right(self):            #Get right child
        return self._right

    def set_right(self, new_right): #Set right child
        if not isinstance(new_right, BST_node) and new_right is not None:
            raise TypeError("BST_Node Value Expected")

        self._right = new_right
        return

    def set_left(self, new_left):   #Set left child
        if not isinstance(new_left, BST_node) and new_left is not None:
            raise TypeError("BST_Node Value Expected")

        self._left = new_left
        return
    
    def __del__(self):         #Destructor
        self._head = None
        self._left = None
        self._right = None

#Inventory BST
class BST():                        #BST for player inventory
    def __init__(self):             #Constructor
        self._root = None
    
    def display(self):              #Display all
        if self._root == None:
            return 0
        return self.__display__(self._root)

    def __display__(self, root) -> int:    #Display recursively
        if root == None:
            return 1

        self.__display__(root.get_left())
        root.get_LLL().display()
        self.__display__(root.get_right())
        return

    def insert(self, data):         #Insert 
        if not isinstance(data, items.item):
            raise TypeError("Item Value Expected")

        if self._root == None:                #New item
            self._root = BST_node(data)
            return 1

        return self.__insert__(self._root, data)

    def __insert__(self, root, data):   #Insert recursively
        if not isinstance(root, BST_node):
            raise TypeError("BST_node Value Expected")

        if root.get_item() == data:                 #Duplicate
            return root.get_LLL().insert(data)

        if root.get_item() < data and root.get_right() == None:     #Right child
            root.set_right(BST_node(data))
            return 1

        if root.get_item() > data and root.get_left() == None:      #Left child
            root.set_left(BST_node(data))
            return 1

        if root.get_item() < data:                                  #Traverse
            self.__insert__(root.get_right(), data)
        else:
            self.__insert__(root.get_left(), data)

    def retrieve(self, match) -> BST_node:      #Get node of match item
        if not isinstance(match, items.item) and not isinstance(match, str):   #Must be an item or string
            raise TypeError("Item Value Expected")

        if self._root == None:  #Empty list no match
            return None
        return self.__retrieve__(self._root, match) 

    def __retrieve__(self, root, match):    #Recursive retrieve
        if root == None:                    #No match
            return None

        if root.get_item() == match:        #Match!
            return root
        
        if root.get_item() < match:                                  #Traverse
            return self.__retrieve__(root.get_right(), match)
        return self.__retrieve__(root.get_left(), match)

    def remove_item(self, match) -> int:
        if not isinstance(match, items.item) and not isinstance(match, str):   #Must be an item or string
            raise TypeError("Item Value Expected")

        if self._root == None:      #No match
            return 0

        if self.retrieve(match) == None:
            return 0

        self._root = self.__remove_item__(self._root, match) 
        return 1 

    def __remove_item__(self, root, match):       #Remove one item
        if root == None:                          #No match
            return root

        if root.get_item() == match:              #Match!
            if root.get_LLL().delete() == 0:      #Delete entry in LLL
                return self.__remove_node__(root) #Remove node from BST
            else:
                return root                       #Do not remove node

        if root.get_item() < match:               #Traverse
            root.set_right(self.__remove_item__(root.get_right(), match)) #Reattach
        else:
            root.set_left(self.__remove_item__(root.get_left(), match))
        return root

    def __remove_node__(self, root):    #Remove node
        if root.get_left() == None and root.get_right() == None:    #Leaf
            return None

        if root.get_right() == None:    #One child: left
            hold = root.get_left()
            root = None
            return hold

        if root.get_left() == None:     #One child: right
            hold = root.get_right()
            root = None
            return hold

        if root.get_right().get_left() == None: #Two children &
            left = root.get_left()              #IOS directly to right
            right = root.get_right()
            root = None
            root = right
            root.set_left(left)
            return root             

        ios = self.__ios__(root.get_right())    #Get IOS
        left = root.get_left()                  #Hold L and R
        right = root.get_right()
        root = None
        root = ios                              #New root
        root.set_left(left)                     #Set L and R
        root.set_right(right)
        return root

    def __ios__(self, root):    #Get IOS
        if root.get_left().get_left() == None:  #Node before IOS
            hold = root.get_left()              #IOS
            root.set_left(root.get_left().get_right())
            return hold

        return self.__ios__(root.get_left())
        
    def __del__(self):  #Destructor
        self._root = None
        return