class MultidArray:

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def create_array(self):

        """Create a new array (matrix).
        
        Returns:
            Returns the newly created array.

        Time:
            Constant time: O(1)

        """
        self.multid_array = [[None for i in range(self.row)] for j in range(self.col)]
        return self.multid_array

    def add_elements(self, elements):

        """Add_elements to the newly created array.

        Par:
            elements the iterables in the array
        
        Returns:
            Returns the updated created array.

        Time:
            Constant time: O(1)

        """
        self.multid_array += self.multid_array.append(elements)
        return self.multid_array

    def shape_of_array(self):

        """Shape_of_array theposition of the rows and columns in the array.
        
        Returns:
            Returns the number of rows and columns of the multidimensional array.

        Time: 
            Linear time:O(n)

        """
        self.shape = (self.row, self.col)
        return self.shape

    def get_element(self, element):

        """Retrieves element from a specific row and column

        Par:
            elements the iterables in the array
        
        Returns:
            The retrived emelemts in the array.
        
        Time: 
            Linear time:O(n)

        """
        self.retrieved_element = self.multid_array[self.row][self.col]
        return self.retrieved_element

    def remove_element(self, get_element):

        """Removes element from a specified index.

        Args:
            Retrieves element from a specific row and column
        
        Returns:
            The poped elements from the array

        Time:
            Constant time: O(1)

        """
        
        self.removed_element = self.multid_array.pop(get_element)
        return self.removed_element
