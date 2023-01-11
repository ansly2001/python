'''a="hello"
b="how are u?"
print(a+b)
c=5
d=5
print(c+d)

class moverload:
    def display(self,a="none",b="done"):
        print(a,b)
obj=moverload()
obj.display()
obj.display(10)
obj.display(10,20)

class father():
    def transportation(self):
        print("cycle")
    
class son(father):
    def transportation(self):
        print("bike")
obj=son()
obj.transportation()
# data encapculation
class encap:
    __a=10
    def __display(self):
        print("welcome")
        print("instance variable",self.__a)
    def show(self):
        print(10)
        self.__display()
        
obj=encap()
#print(obj.a)
#
obj.show()
#obj.display()

#data abstraction
from abc import ABC,abstractmethod
class Aclass(ABC):
    @abstractmethod
    def display(self):
        none
    @abstractmethod
    def show(self):
        none
        
class Demo(Aclass):
    def display(self):
        print("abstract methods")
    def show(self):
        print()
        
obj=Demo()
#obj.display()
obj.show()'''

#exception handling
#l=[10,20,30,40,50]
try:
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    c=a/b
   # print(l[5])
except Exception as e:
    b=1
    c=a/b
    print(c)
else:
    print("no exception")
finally:
    print("the try except is finished")
        
