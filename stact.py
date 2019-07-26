#Add Items 
#check the length
#Pop an item
#pick 
#Pushing Item


class Stack:
    def __init__(self):
        
        self.stact = []

    def add_items(self, items):
        self.stack.append(items)
        return self.stack

        """Add_items to the empty stack.

        Par:
            Items the elements in the stack.
        
        Returns:
            Returns the update stack.

        Time:
            Constant time: O(1)

        """
        

    def isempty(self, items):

        """Isempty checks whether the stack is empty.

        Par:
            Items the elements in the stack.
        
        Returns:
            if the stack is empty return True else return False.

        Time:
            Constant time: O(1)

        """
        if self.items == []:
           return True


    def check_len(self, items):

        return len(self.items)

        """Check the length of the stack.

        Par:
            Items the elements in the stack..
        
        Returns:
            Returns the number of the items in the list.

        Time: 
            Linear time:O(n)

        """

    def push_Item(self, items):

        """Push_items at the to of the stack.

        Par:
            Items the elements in the stack.
        
        Returns:
            Returns the update stack.

        Time:
            Constant time: O(1)
        """

        self.stack.append(items)
        return self.stack

    def remove_item(self):

        try:
            return self.stack.pop()
                
        except IndexError:
            return 'The stack is empty'
        
        """Remove_item the an item from the stack.
        
        Returns:
            The the item removed from the stack.

        Time:
            Constant time: O(1)
        """
    
    def pick_item(self):
        
        """Pick_item check the item at the top of the stack.
        """
        if len(self.stack) != []:
            return self.stack(-1)
        

    