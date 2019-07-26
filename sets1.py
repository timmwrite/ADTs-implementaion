#Add Items
#Pop an Element
#UPdate  an Element
#Union 




class Sets:
    def __init__(self):

        self.my_list = my_list()



    def add_items(self, elements):
        self.my_list = my_list.append(elements)
        self.set_1 = set_1.append(elements)

    def pop_item(self, element):

        """Pop_item delete the a specified elements in the iterable.

        Args:
            Element: an item in the iterable.
        
        Returns:
            The update iterable after the element was poped.

        Constant time: O(1)

        """

        self.my_list.pop(element)
        return self.my_list
   
    def update(self, elements):

        """Update elements in the iterable.

        Args:
            Element: an item in the iterable.
        
        Returns:
            The updated iterable.
        
        Time:
            Constant time: O(1)

        """
        
        self.my_list.update(elements)
        return self.my_list

    def union(self, set_1, my_list):

        """Union combines two sets ensuring there is no repetation of the elemnt on the new sequence.

        Args:
            Set_1: an iterable containg the elements.
            My_list: an iterable containg the elements.
        
        Returns:
            Return a set containing the union of sets.

        Time:
            Constant time: O(1)

        """

        self.new_set = set_1.union(my_list)
        return self.new_set

    def intersection(self, set_1, my_list):

        """Intersects the tow sets.

        Pare:
            et_1: an iterable containg the elements.
            My_list: an iterable containg the elements.
        
        Returns:
            Returns a set, that is the intersection of two other sets

        Time:
            Constant time: O(1)

        """
        self.new_intersection = set_1.intersection(my_list)
        return self.new_intersection




   
        
    