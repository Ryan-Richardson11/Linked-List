class Node:
    """
    Creates the class Node

    Creates the attribute varible self.Data and self.Next
    """
    def __init__(self, d):
        self.Data = d
        self.Next = None
    """
    Creates the initializer method for the Node class

    Parameters: d
    """

class LinkedList:
    """
    Creates the class LinkedList where the functions of the linked list will be implemented

    Creates the attribute varible self.Data and self.Next
    """
    def __init__(self, d=None):
        if (d == None):
            self.Header = None
            self.Current = None
        else:
            self.Header = Node(d)
            self.Current = self.Header
    """
    Creates initializer method for the linkedlist class

    Parameters: d (defaulted to None)
    """
    def nextCurrent(self):
        if (self.Current.Next is not None):
            self.Current = self.Current.Next
        else:
            self.Current = self.Header
    """
    Creates the method nextCurrent in the linkedlist class

    Checks to make sure the next node is not None and moves from the current to the next node.
    Otherwise the current node will become the header.
    """
    def resetCurrent(self):
        self.Current = self.Header
    """
    Creates the method resetCurrent in the linkedlist class

    Resets the current node to the header.
    """
    def getCurrent(self):
        if (self.Current is not None):
            return self.Current.Data
        else:
            return None
    """
    Creates the method getCurrent in the linkedlist class

    If the list is not empty, returns the data of the current node. Else returns None.
    """
    def insertBeginning(self, d):
        if (self.Header is None):
            self.Header = Node(d)
            self.Current = self.Header
        else:
            Tmp = Node(d)
            Tmp.Next = self.Header
            self.Header = Tmp
    """
    Creates the method insertBeginnning in the linkedlist class

    If the list is empty, inserts new node containing the parameter d to be the new header.
    Sets current node to the header. Else creates a tmp variable for the new node and sets the previous
    header to the next node and updates back to the new node which is tmp and the current header.
    """
    def insertCurrentNext(self, d):
        if (self.Header is None):
            self.Header = Node(d)
            self.Current = self.Header
        else:
            Tmp = Node(d)
            Tmp.Next = self.Current.Next
            self.Current.Next = Tmp
    """
    Creates the method insertCurrentNext in the linkedlist class

    If the list is empty, the header becomes the new node and current is set to the header.
    Else creates a tmp variable set to the new node. Inserts the node next to the current one in the list.
    """
    def removeBeginning(self):
        if (self.Header is None):
            return None
        else:
            ans = self.Header.Data
            self.Header = self.Header.Next
            self.Current = self.Header
            return ans
    """
    Creates the method removeBeginnning in the linkedlist class

    If the list is empty, return None. Otherwise creates a ans variable set to the current headers data.
    Sets the new header and current to the next node and returns ans.
    """
    def removeCurrentNext(self):
        if (self.Current.Next is None):
            return None
        else:
            ans = self.Current.Next.Data
            self.Current.Next = self.Current.Next.Next
            return ans
    """
    Creates the method removeCurrentNext in the linkedlist class

    If there is no node after current, return None. Otherwise creates a ans variable set to the data of the next
    node after the current one. Current node is moved to the next node over and ans is returned.
    """
    def printList(self,msg="====="):
        p = self.Header
        print("====",msg)
        while (p is not None):
            print(p.Data, end=" ")
            p = p.Next
        if (self.Current is not None):
            print("Current:", self.Current.Data)
        else:
            print("Empty Linked List")
        input("----------------")
    """
    Creates the method printList in the linkedlist class

    While the list is not empty, data will be printed with each next node until there are none.
    Current node will be printed after the linked list.
    """

def read_file():
    """
    Creates read_file function

    Reads the data in the txt file and tranfers it to a sorted array. Inserts the array into a linked
    list and calls methods from the linked list class to perfrom functions on the list 
    """
    # Opens file in readmode
    myINfile = open("data.txt", "r")
    a = []
    for data in myINfile:
        list_a = data.strip()
        a.append(list_a)
    myINfile.close()
    a.sort(key=int)

    # Instantiates the object L in the linkedlist class.
    L = LinkedList()
    # Iterates through the array "a" to add each integer to the linked list "L"
    for data in a:
        L.insertCurrentNext(int(data))
        L.nextCurrent()
    # Asks for user input 
    x = eval(input("please enter a integer value: "))
    # While the list is not empty
    while L.getCurrent() is not None:
        # If x is the header, removes from beginning of the list.
        if x == L.Header.Data:
            L.removeBeginning()
            break
        # If there is a node after the current and is equal to x, remove that node.
        elif L.Current.Next is not None and L.Current.Next.Data == x:
            L.removeCurrentNext()
            break
        # If x is less than the first integer in the list, add x to the beginning.
        elif x < L.Header.Data:
            L.insertBeginning(x)
            break
        # If there is no node after the current one and x is larger than that data, add x to the end of the list.
        elif L.Current.Next is None and x > L.Current.Data:
            L.insertCurrentNext(x)
            break
        # If x is greater than the current node but less than the next one, insert it between the two nodes in the list
        elif L.Current.Data < x and x < L.Current.Next.Data:
            L.insertCurrentNext(x)
            break
        # Moves current node to iterate through the list.
        else:
            L.nextCurrent()
    # Prints the new list.
    L.printList()
# Function call.
read_file()

