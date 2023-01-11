#Accept a file name from user and print extension of that

filename=input("enter the filename: ")
extension=filename.split(".")
print("extension of file is:" + repr(extension[-1]))