## read information outside python files
## open(name of the file, mode)
# r - Read - Default value. Opens a file for reading, error if the file does not exist 
# w - Write - Opens a file for writing, creates the file if it does not exist
# a - Append - Opens a file for appending, creates the file if it does not exist
# x - Create - Creates the specified file, returns an error if the file exists
# t - Text - Default value. Text mode
# b - Binary - Binary mode (e.g. images)
# r+ - read and write
# 'w' overwrites everything in the file
## with (file, type) as variable - to automatically close the file without a .close()
## to check if the file is readable .readable()
## to spit out all the information within the file .read()
## to read a individual line within the file .readline()
## if there are subsequente .readline() the lines will be read one at a time
## .readlines()[index] - transform the files into a array
## for employee in employee_file.readlines():
##    print(employee)
## employee_file.close()

## with open("employee.txt", "r") as employee_file:

## employee_file.write("Toby - Human resources") to write to a file
## to add a new line prior to appending the entry employee_file.write("\nKelly - Customer Service")
# always check if the relative and absolute paths are the same 
# if not, specify the absolute pathing such as the eg. ('c:/Users/User/Desktop/Python/Python 101/employee.txt', 'a')

employee_file = open('c:/Users/User/Desktop/Python/Python 101/employee.txt', 'a')
employee_file.write("Jim - Sales")
#employee_file.write("\nDora - Explorer") - nem line
employee_file.close()

#import os

#cwd = os.getcwd()  # Get the current working directory (cwd)
#files = os.listdir(cwd)  # Get all the files in that directory
#print("Files in %r: %s" % (cwd, files))