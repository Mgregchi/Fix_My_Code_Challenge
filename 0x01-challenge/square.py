#!/usr/bin/python3

class Square():
    """
    This class represents a square.
    """

    def __init__(self, **kwargs):
        """
        Initializes a Square object.
        
        Args:
            width (int): The width of the square.
            height (int): The height of the square.
        """
        self.width = kwargs.get('width', 0)
        self.height = kwargs.get('height', 0)

    def area_of_my_square(self):
        """
        Calculates the area of the square.
        
        Returns:
            int: The area of the square.
        """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """
        Calculates the perimeter of the square.
        
        Returns:
            int: The perimeter of the square.
        """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        Returns a string representation of the square.
        
        Returns:
            str: The string representation of the square.
        """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
