class publisher:
    def __init__(self,n):
        self.name=n
    def display(self):
        print("Name of publisher is:",self.name)
class Book(publisher):
    def __init__(self,n,t,a):
        super().__init__(n)
        self.title=t
        self.author=a
    def display(self):
        print("Title of the book is:",self.title)
        print("Author of the book is:",self.author)
class python(Book):
    def __init__(self,n,t,a,p,pgs):
        super().__init__(n,t,a)
        self.price=p
        self.pages=pgs
    def display(self):
        print("Pulisher of the book is:",p1.name)
        print("Title of the book is   :",p1.title)
        print("Author of the book is  :",p1.author)
        print("Price of the book is   :",p1.price)
        print("Pages of the book is   :",p1.pages)
p1=python("Python Programming","Introduction to python","Jeeva Jose",450,300)
p1.display()