'''a=int(input("enter a:"))
b=int(input("enter b:"))
try:
    if b==0:
        raise Exception
    c=a/b
    print(c)
except:
    print("exception raised")

marks=int(input("enter marks:"))
try:
    if marks<0 or marks>100:
        raise Exception ("marks should be in between 0 and 100")
    print("marks=",marks)
except Exception as e:
    print(e)'''


class InvalidData(Exception):
    pass
class InvalidMarks(Exception):
    pass
marks=int(input("enter marks for student:"))
try:
    if marks<0 or marks>100:
        raise InvalidMarks
except InvalidMarks:
    print("marks should be in between 0 and 100")