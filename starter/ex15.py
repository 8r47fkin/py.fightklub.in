# imports argument values from sys a package
from sys import argv

# two argument first is script then the other is file name 

script, filename = argv

# we are assigning a variable txt which calls a function, to open a file where the filename is pulled from argv

txt = open(filename)

# a functional print statement, where it prints the filename
# then in next it reads the context of the file

print(f"Here's your file {filename}:")
print(txt.read())

#first it prints the statement "type the filename again"
#then it reassigns the filename to a variable called file_again 

print("type the filename again:")
file_again = input(">")

# then it assigns txt_again variable to open function with file_again, then it print the txt_again function which ask to open and read file_again

txt_again = open(file_again)

print(txt_again.read())
