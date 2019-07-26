#Insert: inserts a new node into the list
#Size: returns size of list
#Search: searches list for a node containing the requested data and 
# returns that node if found, otherwise raises an error
#Delete: searches list for a node containing the requested data a
# nd removes it from list if found, otherwise raises an error

class Node:
    def __init__(self, data=None):
        
        self.data = data
        self.nextelement = None

class Stack:
    def __init__(self):
        
        self.head = None 
        self.size = 0
        self.list1 = Stack()

    def len(self):

        """Check the length of the stack.
        
        Returns:
            Returns the number of the items in the stack.

        Time: 
            Linear time:O(n)

        """

        return self.list1

    def push(self, element, next):

        """Push to add an element at the top of the stack.

        Par:
            element: the first iterable to be added in the stack.

            next: the second iterable to be added on the top of the stack.

        Time:
            Constant time: O(1)
        """
        list1.head = Node("element")
        next = Node("element2")
        next2 = Node("element3")
        
        """linking the first to the next node"""
        list1.head.nextelement = next

        """linking the second element to the next node"""
        next.nextelement = next2


    def remove(self):

        """Remove the an item from the stack.
        
        Returns:
            The the item removed from the stack.

        Time:
            Constant time: O(1)
        """
        try:
            return self.list1.pop()
        
        except IndexError:
            return 'The stack is empty'


    def isempty(self):

        """Isempty checks whether the stack is empty.
        
        Returns:
            if the stack is empty return True else return False.

        Time:
            Constant time: O(1)

        """
        return self.size


    

