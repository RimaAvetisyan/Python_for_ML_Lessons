import random
import math

"""IF, ELIF, ELSE"""

# 1. Enter your name, then find the sum of the ASCII values of the first and the last letter in your name. If
# that number is larger than 500, print "I've got a great name!", and "I've got a fancy name!" otherwise.
# Ներմուծեք ձեր անունը և գտեք անվան առաջին և վերջին տառերի ASCII արժեքների գումարը։ Եթե թիվը մեծ է 500-ից, տպել
# "I've got a great name!", իսկ հակառակ դեպքում՝ "I've got a fancy name!"։
#
# name = input('enter your name')
# s = ord(name[0])+ord(name[-1])
# if s > 500:
#     print("I've got a great name!")
# else:
#     print("I've got a fancy name!")


# 2. Ask the user for a movie c. If the title starts with a capital letter, print "Great title!", otherwise print
# "Titles start with capital letters...". If the input starts with a special character [!, @, #, $, %, ^, &], print "I
# doubt that this is a title.".
# Պահանջել ներմուծել ֆիլմի վերնագիր։ Եթե վերնագիրը սկսվում է մեծատառով, տպել "Great title!", հակառակ դեպքում տպել
# "Titles start with capital letters..."։ Եթե ներմուծվածը սկսվում է [!, @, #, $, %, ^, &] նշաններով, տպել "I doubt that
# this is a title."․

# lst = ['!', '@', '#', '$', '%', ' ^', ' &']
# title = input('Enter title')
# a = title[0]
# if 90 >= ord(a) >= 65:
#     print("Great title!")
# elif 122 >= ord(a) >= 97:
#     print("Titles start with capital letters...")
# elif a in lst:
#     print("I doubt that this is a title.")


# 3. Ask the user to input his/her age. If the user is older than 17, than tell them they're eligible to vote. If they
# are younger than 18, tell them how many years do they have to wait.
# Հարցրեք օգտատիրոջ տարիքը։ Եթե նա 17 տարեկանից մեծ է, նրան տեղյակ պահեք, որ կարող է քվեարկել։ Հակառակ դեպքում ասեք, թե
# քանի տարուց նա կկարողանա դա անել։

# age = int(input('enter your age'))
# if age > 17:
#     print('you are eligible to vote')
# else:
#     print(f'you have to wait {18-age} years')



# 4. Write a program that will tell us whether a given year is a leap year or not.
# Գրել ծրագիր, որը կտեղեկացնի, թե տրված տարին նահանջ է, թե ոչ։

# year = int(input('enter year'))
#
# if((year % 400 == 0) or  (year % 100 != 0) and  (year % 4 == 0)):
#     print("Given Year is a leap Year")
# else:
#     print("Given Year is not a leap Year")

# 5. Using 'random' module, generate a random number between -1000 and 1000. If the number is positive, print positive.
# If it's negative, print negative along with the absolute value of the number.
# Օգտագործելով random գրադարանը, գեներացնել [-1000,1000]-ը տիրույթում պատահական թիվ։ Եթե թիվը դրական է, տպել positive.
# Հակառակ դեպքում տպել negative և այդ թվի բացարձակ արժեքը։

# number = random.randint(-1000, 1000)
# if number >= 0:
#     print('positive')
# else:
#     print(f'negative,absolute value : {abs(number)}')


# 6. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the
# string length is less than 2, return instead of the empty string.
# Գրել ծրագիր, որը կվերադարձնի նոր սթրինգ տրված սթրինգի առաջին և վերջին երկու տառերը պարունակող։ Եթե սթրինգի
# երկարությունը երկուսից փոքր է, վերադարձնել օրիգինալ սթրինգը։


# s = input()
# if len(s) <= 2:
#     print(s)
# else:
#     s1 = s[0:2]+s[-1:-3:-1]
#     print(s1)


"""LOOPS"""

# 1. Create a 3x3 matrix that will contain the squares of the numbers from 1-9 using a nested loop.
# Օգտագործելով ցիկլեր, ստեղծել 3x3 մատրից, որը կպարունակի 1-9 թվերի քառակուսիները։

# x = []
# y = []
# a = 1
# for _ in range(3):
#     for _ in range(3):
#         y.append(a*a)
#         a += 1
#     x.append(y)
#     y = []
#
# print(x)

# 2. Count the number of 'b's (and 'B's) in the given string. DO NOT use the count() method.
# Հաշվել տրված սթրինգում 'b'-երի քանակը։ Չօգտագործել count() մեթոդը։

# s = input()
# q = 0
# for i in s.lower():
#     if i == 'b':
#         q += 1
# print(q)

# 3. Write a program that will print the factorial of n.
# Գրել ծրագիր, որը կտպի n թվի ֆակտորիալը։
#
# n = int(input())
# if n == 0:
#     print(1)
# else:
#     p = 1
#     for i in range(2, n+1):
#         p *= i
#     print(p)
#
#
# 4. Write a program to calculate the length of a string. DO NOT use the len() function.
# Գրել ծրագիր, որն առանց len() ֆունկցիայի կիրառման կվերադարձնի սթրինգի երկարությունը։

#
# s = input()
# q = 0
# for _ in s:
#     q += 1
# print(q)

# 5․ Write a program, that will return a new string containing only those characters in the original string that have
# prime indices.
# Վերադարձնել նոր սթրինգ, որը տրված սթրինգի միայն այն տարրերը կպարունակի, որոնց ինդեքսները պարզ թվեր են։

# poem = """All that is gold does not glitter,
# Not all those who wander are lost;
# The old that is strong does not wither,
# Deep roots are not reached by the frost.
# """
# poem1 = poem[2]
# for i in range(3, len(poem)):
#     t = True
#     for j in range(2, int(math.sqrt(i))+1):
#         if i % j == 0:
#             t = False
#             break
#     if t:
#         poem1 += poem[i]
# print(poem1)
