class Area():
    def __init__(self, radius):
        self.radius = radius

    def calc_hekef(self,radius):
        return  (self.radius)*3.14*2

    def calc_area(self,radius):
        return (self.radius)*3.14**2

    def __str__(self):
        return f'the radius is {radius}, the hekef is {self.calc_hekef} and the area is {self.area}'

radius = Area(6)
print(radius,radius.calc_hekef(radius),radius.calc_hekef(radius))
