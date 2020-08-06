class Rectangle:
    def __init__(self, width, height):
        self.width = width;
        self.height = height;

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, num):
        self.width = num

    def set_height(self, num):
        self.height = num

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width < 50 and self.height < 50:
            draw_width = "*" * self.width
            return (draw_width + "\n") * self.height
        else:
            return "Too big for picture."

    def get_amount_inside(self, Rectangle):
        if (self.width < Rectangle.width or self.height < Rectangle.height):
            return 0
        timesfitwidth = int(self.width / Rectangle.width)
        timesfitheight = int(self.height / Rectangle.height)
        return timesfitwidth * timesfitheight

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side)

    def __repr__(self):
        return f"Square(side={self.width})"

    def set_side(self, num):
        self.width = num
        self.height = num

    def set_width(self, num):
        self.width = num
        self.height = num

    def set_height(self, num):
        self.width = num
        self.height = num
