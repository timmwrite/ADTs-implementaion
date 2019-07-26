# list of Item’s
# Found a match:



class Mapps():
    def __init__(self):
        self.mytable = [ ]

    def getitem (self, y):

        """Getitem gets the value of y from mytable.

        Args:
            Y: an value item in mytable.
        
        Returns:
            THe value of Y and the Key K.
        
        Time: 
            Linear time:O(n)

        """

        try:
            for item in self.mytable:
                if y == self.item._key:
                    pass
        except TypeError:
            self.mytable = 'The object should be iterable!'
        
        return self.item._value
            
    def delitem (self, y):

        """Delitem deletes the value of y from mytable.

        Args:
            Y: an value item in mytable.
        
        Returns:
            An iterable secquence without the value Y.

        Time:
            Constant time: O(1)

        """

        try:
            for x in range(len(self.mytable)):
                if y == self._table[x]._key: 
                    self.mytable.pop(x) 
        except TypeError:
            mytable = 'The object should be iterable!'

        return self.mytable

    def getlen(self):

        """Getlen get the length of the iterable.
        
        Returns:
           The length of the iterable.

        Time: 
            Linear time:O(n)

        """

        return len(self.mytable)

    def iterate_mytable(self):

        """Iterate_mytable loops through the iterable.
        
        Returns:
            The items in the sequence.

        Time: 
            Linear time:O(n)

        """
        for item in self._table:
            yield item._key