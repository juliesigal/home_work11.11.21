class Circle():
    def __init__(self, radius):
        self.radius = radius

    def calc_hekef(self):
        return  (self.radius)*3.14*2

    def calc_area(self):
        return (self.radius)*3.14**2

    def __str__(self):
        return f'the radius is {radius1}' \
               f'the hekef is {self.calc_hekef()}' \
               f'and the area is {self.calc_area()}'
