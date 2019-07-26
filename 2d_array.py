#2d rows and columns where individual elemenst can be accessed

class Dimention():
    def __init__(self):
        self.row = 0
        self.column = 0
        self.my_array = [[0 for i in range(column)], i in range(row)]

    
    
    
    def create(self,rows,columns):
        """Create a 2d array (matrix) and pass in rows and columns.

        Par:
            rows are "horizontal" collections of iterables ina an array.
            columns are "vertical" collections of iterables ina an array.
        
        Returns:
            Returns the newly created array.

        Time:
            Constant time: O(1)

        """
        self.row = row
        self.column = column
        self.my_array = self.my_array = [[0 for i in range(column)], i in range(row)]
        return self.my_array

      
     
    def get_num_rows(self):

        """Access the number of rows and return the number of rows.
        
        Returns:
            Returns the numbers of rows in the array.

        Time: 
            Linear time:O(n)

        """
        for k in range(row):
            return self.row
  
    
    def get_num_columns(self, row, column):

        """Access the number of columns and return the number of columns.

        Par:
            rows are "horizontal" collections of iterables ina an array.
            columns are "vertical" collections of iterables ina an array.
        
        Returns:
            Returns the numbers of columns in the array.

        Time: 
            Linear time:O(n)

        """
        self.my_array = [[0 for i in range(column)], i in range(row)]
        return self.my_array      
   
    #Clear the array
    def clear_array(self,value):

        """Clear_array the array.

        Par:
            value of the items in the array
        
        Returns:
            Returns an empty array.

        Time:
            Constant time: O(1)

        """

        self.my_array = my_array.clear()
  
  
    def get_item(self,row,column):

        """Getitem gets the value of rows and columns from my_array.

        Par:
            rows are "horizontal" collections of iterables ina an array.
            columns are "vertical" collections of iterables ina an array.
        
        Returns:
            The value of rows and the columns.

        Time: 
            Linear time:O(n)
        """
        return self.my_array[column][row]
  