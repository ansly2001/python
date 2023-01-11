class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
        
    def get_perimeter(self):
        return 2*(self.l+self.b)
    def get_area(self):
        return self.l*self.b
    def compare(self,s):
        try:
            if r.get_area()==s.get_area():
                print("both area are equal")
            elif r.get_area()>s.get_area():
                print("largest is:",r.get_area())
            else:
                print("largest is:",s.get_area())
        except:
            print("no exception")
l1=int(input("enter the value of length l1:"))
b1=int(input("enter the value of breadth b1:"))
l2=int(input("enter the value of length l2:"))
b2=int(input("enter the value of breadth b2:")) 
r=Rectangle(l1,b1)
print("area of rectangle:",r.get_area())
print("perimeter of rectangle:",r.get_perimeter())
s=Rectangle(l2,b2)
print("area of rectangle:",s.get_area())
print("perimeter of rectangle:",s.get_perimeter())
r.compare(s)

    