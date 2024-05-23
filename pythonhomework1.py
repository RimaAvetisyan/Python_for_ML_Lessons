"""
# 1. Write a Python program to print the following string in a specific format (see the output). Go to the editor
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :
#
# Twinkle, twinkle, little star,
# 	How I wonder what you are!
# 		Up above the world so high,
# 		Like a diamond in the sky.
# Twinkle, twinkle, little star,
# 	How I wonder what you are
# Click me to see the sample solution
"""

# S="Twinkle, twinkle, little star,\n {''>5} How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
# print(s)


"""
# 2. Write a Python program to get the Python version you are using. Go to the editor
"""
# import sys
# print("Python version")
# print(sys.version)
# print("Version info.")
# print(sys.version_info)
#

"""

#
# 3. Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

"""
# import datetime
# now = datetime.datetime.now()
# print("Current date and time : ")
# print(now.strftime("%Y-%m-%d %H:%M:%S"))

"""

# 4. Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504
# Click me to see the sample solution"""
#
#
# from math import pi
# r = float(input("Input radius : "))
# print(" area  " + str(pi * r**2))

"""
#
# 5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them. Go to the editor
# Click me to see the sample solution"""

#
# fname = input('input your first name ')
# lname = input('input your last name ')
#
# print('hello'+lname+' '+fname)

"""

# 6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. Go to the editor
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')
# Click me to see the sample solution"""

# values = input("Input some comma seprated numbers : ")
# lst = values.split(",")
# tpl = tuple(list)
# print('List : ', lst)
# print('Tuple : ', tpl)

"""

# 7. Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
# Sample filename : abc.java
# Output : java
# Click me to see the sample solution"""

#
# filename = input("Input the Filename: ")
# extns = filename.split(".")
# print("The extension of the file is : " + repr(extns[-1]))

"""
#
# 8. Write a Python program to display the first and last colors from the following list. Go to the editor
# color_list = ["Red","Green","White" ,"Black"]
# Click me to see the sample solution"""
#
# color_list = ["Red", "Green", "White", "Black"]
# print(color_list[0], ',', color_list[-1])



"""

# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014
# Click me to see the sample solution"""

# exam_st_date = (11, 12, 2014)
# print(f"The examination will start from :{exam_st_date[0]}/{exam_st_date[1]}/{exam_st_date[2]} ")
#

"""

10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5
Expected Result : 615
Click me to see the sample solution"""

# n = int(input('n='))
# print(n+(n*10+n)+(n*100+n*10+n))


"""

11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.
Click me to see the sample solution"""

#
# print(abs.__doc__)
#



"""

12. Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
Click me to see the sample solution"""
#
# import calendar
# y = int(input("Input the year : "))
# m = int(input("Input the month : "))
# print(calendar.month(y, m))

"""

13. Write a Python program to print the following 'here document'. Go to the editor
Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
Click me to see the sample solution"""
#
#
# print("""
# a string that you "don't" have to escape
# This
# is a  ....... multi-line
# heredoc string --------> example
# """)


"""

14. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
Click me to see the sample solution"""
#
# from datetime import date
# f_date = date(2014, 7, 2)
# l_date = date(2014, 7, 11)
# delta = l_date - f_date
# print(delta.days)

"""

15. Write a Python program to get the volume of a sphere with radius 6.
Click me to see the sample solution"""

# pi = 3.1415926535897931
# r = 6.0
# V = 4.0/3.0*pi * r**3
# print('The volume of the sphere is: ', V)

"""

16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference. Go to the editor
Click me to see the sample solution"""

# def difference(n):
#     if n <= 17:
#         return 17 - n
#     else:
#         return (n - 17) * 2
#
# print(difference(22))
# print(difference(14))

"""

17. Write a Python program to test whether a number is within 100 of 1000 or 2000. Go to the editor
Click me to see the sample solution"""

#
# def near_thousand(n):
#     return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
#
#
# print(near_thousand(1000))
# print(near_thousand(900))
# print(near_thousand(800))
# print(near_thousand(2200))

"""

18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum. Go to the editor
Click me to see the sample solution"""


# def sum_thrice(x, y, z):
#     sum = x + y + z
#
#     if x == y == z:
#         sum = sum * 3
#     return sum
#
#
# print(sum_thrice(1, 2, 3))
# print(sum_thrice(3, 3, 3))

"""

19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged. Go to the editor
Click me to see the sample solution"""
#
# def new_string(str):
#   if len(str) >= 2 and str[:2] == "Is":
#     return str
#   return "Is" + str
#
# print(new_string("Array"))
# print(new_string("IsEmpty"))

"""

20. Write a Python program to get a string which is n (non-negative integer) copies of a given string. Go to the editor
Click me to see the sample solution """

# def larger_string(str, n):
#    result = ""
#    for i in range(n):
#       result = result + str
#    return result
#
# print(larger_string('abc', 2))
# print(larger_string('.py', 3))

