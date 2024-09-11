
class GraphicObject:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        print(f"Drawing object with width {self.width} and height {self.height}")

class Rectangle(GraphicObject):
    def __init__(self, width, height):
        super().__init__(width, height)

#тут я спробувала створити клас Квадрата, в якому нам потрібно знати тільки його сторону 
class Square(GraphicObject):
    def __init__(self, side):  
        super().__init__( side, side)
        self.side = side    
    def draw(self):
        print(f"Drawing square with side {self.side}")

class Button(Rectangle):
    def __init__(self, width, height, name):
        super().__init__(width, height)
        self.name = name

    def on_click(self):
        print(f"Button '{self.name}' was clicked!")

    def draw(self):
        super().draw() 
        print(f"Button name: '{self.name}'")

rectangle = Rectangle(100, 50)
rectangle.draw()

square1 = Square(30)
square1.draw()

button = Button(150, 70, "Submit")
button.draw()

button.on_click()
