"""RECURSION"""

# 0. Write a recursive function that will print odd numbers from 'start' to 'stop'.
# Գրել ռեկուրսիվ ֆունկցիա, որը կտպի բոլոր կենտ թվերը [start, stop] միջակայքում։
# #
# start = int(input('start= '))
# stop = int(input('stop= '))
#
#
# def odd(start, stop):
#     if start > stop:
#         return
#     if start % 2 == 1:
#         print(start, ' ')
#     odd(start+1, stop)
#

# odd(start, stop)

# 1. Write the Fibonacci function using recursion.
# (Optional) The algorithm must have a time complexity of O(n)
# Գրել ֆունկցիա, որը ռեկուրսիվ կերպով կվերադարձնի ֆիբոնաչիի հաջորդականության n-րդ անդամը։
# (Լրացուցիչ) Ժամանակային բարդությունը պետք է լինի O(n)

# n = int(input('n='))
#
#
# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     return fib(n-1)+fib(n-2)
#
#
# print(fib(n))

# 2. Write a function to calculate the factorial of n recursively.
# Գրել ֆունկցիա, որը կհաշվի n-ի ֆակտորիալը ռեկուրսիվ կերպով

# n = int(input('n='))
#
#
# def fac(n):
#     if n == 1:
#         return n
#     return n*fac(n-1)
#
#
# print(fac(n))

# 3. Write a recursive function to calculate the sum of elements of a list.
# Գրել ֆունկցիա, որը ռեկուրսիվ կերպով կհաշվի լիստի տարրերի գումարը։

# lst = [1, 5, 9, 6, 8, 7]
#
#
# def sum(lst, n):
#     if n == 0:
#         return lst[0]
#     return lst[n]+sum(lst, n-1)
#
#
# print(sum(lst, len(lst)-1))

# 4. Write a recursive function to calculate the geometric sum of n.
# Գրել ռեկուրսիվ ֆունկցիա, որը կհաշվի մինչև n երկրաչափական գումարը: a-ն և r-ը պետք է լինեն պարամետրեր։
# a * r + a * r ^ 2 + a * r ^ 3 + ...
# #
# a = int(input('a='))
# r = int(input('r='))
# n = int(input('n='))
#
#
# def geosum(a, r, n):
#     if n == 0:
#         return a
#     return a*pow(r, n)+geosum(a, r, n-1)
#
#
# print(geosum(a, r, n))

# 5. Write a recursive function to calculate the sum of reciprocals of powers of 2.
# Գրել ռեկուրսիվ ֆունկցիա, որը կհաշվի երկրաչափական գումարը, որտեղ r = 1 / 2 է։ Փորձեք բացրձրացնել n-ի արժեքը հետաքրքիր
# արդյունք ստանալու համար։

# r = 1/2
# n = int(input('n='))
# a = int(input('start='))
#
#
# def geosum(a, r, n):
#     if n == 1:
#         return a
#     return geosum(a, r, n-1)/2
#
#
# print(geosum(a, r, n))

# 6. Write a recursive function to calculate n-th power of a.
# Գրել ֆունկցիա, որը ռեկուրսիվ կերպով կհաշվի a-ի n աստիճանը։

# a = int(input('a='))
# n = int(input('n='))
#
#
# def power(a, n):
#     if n == 1:
#         return a
#     return a*power(a, n-1)
#
#
# print(power(a, n))

# 7. Write a recursive function that evaluates a mathematical expression. Example input - "5 + 6"
# Գրել ռեկուրսիվ ֆունկցիա, որը կհաշվի մաթեմատիկական արտահայտություն փոխանցված սթրինգի միջոցով։ Օրինակ՝ "5 + 6"



# 8. Write a recursive function that reverses a string
# Գրել ֆունկցիա, որը ռեկուրսիվ կերպով կշրջի և կվերադարձնի փոխանցված սթրինգը։

# string = input('enter string')
#
#
# def rev(string, len):
#     if len == 1:
#         return string
#     return string[len-1]+rev(string[:len-1], len-1)
#
#
# print(rev(string, len(string)))

# 9. Given a string, compute recursively a new string where all the lowercase 'x' chars have been moved
# to the end of the string.
# Գրել ռեկուրսիվ ֆունկցիա, որը որպես արգումենտ կվերցնի սթրինգ և կվերադարձնի նոր սթրինգ, որտեղ օրիգինալ սթրինգում գտնվող
# բոլոր x-երը տեղափոխվել են սթրինգի ամենավերջը։

# str = input()
#
#
# def strx(str):
#     if len(str) <= 1:
#         return str
#     if str[0] == 'x':
#         return strx(str[1:]) + str[0]
#     return str[0] + strx(str[1:])
#
#
# print(strx(str))