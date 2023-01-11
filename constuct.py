
class Rectangle:
    def __init__(self,length,breadth,unit_cost=0):
        self.length=length
        self.breadth=breadth
        self.unit_cost=unit_cost
    def get_perimeter(self):
        return 2*(self.length+self.breadth)
    def get_area(self):
        return self.length*self.breadth
    def calculate_cost(self):
        area=self.get_area()
        return area*self.unit_cost
r=Rectangle(160,120,2000)
print("area of rectangle:",r.get_area())
print("cost of rectangle:",r.calculate_costs())