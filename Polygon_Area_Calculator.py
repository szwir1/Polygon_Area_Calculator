import pdb

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width_set):
        self.width = width_set

    def set_height(self, height_set):
        self.height = height_set

    def get_area(self):
        area = self.width * self.height
        return area
        
    def get_perimeter(self):
        circuit = 2 * (self.width + self.height)
        return circuit

    def get_diagonal(self):
        diagonal = ((self.width ** 2) + (self.height ** 2)) ** 0.5
        return diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return("Too big for picture.")
        row = ("*" * self.width) + "\n"
        picture = ""
        for x in range(self.height):
            picture += row
        return picture

    def __str__(self):
        return(f"Rectangle(width={self.width}, height={self.height})")

    def get_amount_inside(self, other):
        across = self.width // other.width
        down = self.height // other.height
        return across * down 


        
    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return(f"Square(side={self.width})")

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    
        
    


sq = Square(5)
sq.set_side(8)
print(sq.width)            # oczekujemy 8
print(sq.height)           # oczekujemy 8
print(sq.get_area())       # oczekujemy 64
print(sq.get_perimeter())  # oczekujemy 32
