"""DATA STRUCTURES (Lists)"""
import random
# 1. Write a program to count the number of strings where the string length is 2 or more and the first and last
# character are same from a given list of strings.
# Գրել ծրագիր, որը կհաշվի լիստում եղած 2 կամ ավել երկարություն ունեցող լիստերի քանակը, որոնց առաջին և վերջին տառերը
# նույնն են։

# lst = ["dfhfgj", "fsjjjj", "fjffgfjf", "fhjjktyhg"]
# q = 0
# for i in lst:
#     if len(i) > 1:
#         if i[0] == i[-1]:
#             q += 1
# print(q)


# 2. Create a list from 5 user inputs.
# Ստեղծել լիստ 5 ներմուծված թվերից

# lst = []
# for _ in range(5):
#     lst.append(int(input()))
# print(lst)

# 3. Given a list of ints, print True if the list contains a 2 next to a 2 somewhere.
# Գրել ծրագիր, որը կտպի True, եթե տրված լիստում ինչ-որ տեղ 2 թվին 2 է հաջորդում։

# lst = [1, 4, 5, 2, 2, 5, 9]
# t = False
# for i in range(1, len(lst)):
#     if lst[i-1] == lst[i] == 2:
#         t = True
#         break
# print(t)

# 4. Given a list of ints, print True if every element is a 1 or a 4, and False otherwise.
# Գրել ծրագիր, որը կտպի True, եթե լիստի բոլոր էլեմենտները 1 կամ 4 են։ Հակառակ դեպքում տպել False:

# lst = [1, 4, 1, 1, 4, 4, 1, 4]
# t = True
# for i in lst:
#     if i != 1 and i != 4:
#         t = False
#         break
# print(t)

"""FUNCTIONS"""


# 1. We'll say that an element in an array is "alone" if there are values before and after it, and those values are
# different from it. Return a version of the given array where every instance of the given value which is alone is
# replaced by whichever value to its left or right is larger.
# Ենթադրենք տարրը "միայնակ" է, եթե նրանից առաջ կամ հետո գտնվող տարրերի արժեքը տարբերվում է իր արժեքից։ Ստեղծել ֆունկցիա,
# որը կվերցնի լիստ որպես արգումենտ և կվերադարձնի այդ լիստը ձևափոխված այնպես, որ բոլոր միայնակ տարրերը փոխարինված լինեն
# իրենցից աջ կամ ձախ գտնվող առավելագույն արժեք ունեցող տարրով ([4, 4, 1, 3, 3], այստեղ 1-ը կփոխարինվի 4-ով):

# lst = [4, 4, 1, 3, 3, 1]
# if lst[0] != lst[1]:
#     lst[0] = lst[1]
# if lst[-1] != lst[-2]:
#     lst[-1] = lst[-2]
#
# for i in range(1, len(lst)-1):
#     if lst[i] != lst[i-1] and lst[i] != lst[i+1]:
#         lst[i] = max(lst[i-1], lst[i+1])
# print(lst)


# 2. Write a function to create and print a list where the values are square of numbers between 1 and 30
# (both included).
# Ստեղծել ֆունկցիա, որը կստեղծի և կտպի լիստ, որի արժեքները [1, 30] միջակայքում գտնվող թվերի քառակուսիներն են։

# def square():
#     lst = []
#     for i in range(1, 31):
#         lst.append(i*i)
#     print(lst)
#
#
# square()

# 3. Write a function which will take one argument n. Return a list of size n, that will contain random numbers
# from (-100, 400).
# Ստեղծել ֆունկցիա, որը կվերցնի մեկ արգումենտ՝ n: Վերադարձնել n երկարությամբ լիստ, որը կպարունակի (-100, 400)
# միջակայքում գտնվող պատահական թվեր։

# def rnd(n):
#     lst = []
#     for _ in range(n):
#         lst.append(random.randint(-100, 400))
#     return lst
#
#
# n = int(input())
# print(rnd(n))

# 4. Write a function, that will take a list of words as an argument and return all the words in the list that start
# with a vowel.
# Ստեղծել ֆունկցիա, որը կվերցնի լիստ որպես արգումենտ (սթրինգերի) և կվերադարձնի մեկ այլ լիստ, որը կպարունակի այդ լիստի
# բոլոր այն բառերը, որոնք սկվում են ձայնավորով։

# def words(lst):
#     lst1 = ['a', 'e', 'i', 'o', 'u', 'y']
#     lst2 = []
#     for i in lst:
#         if i[0].lower() in lst1:
#             lst2.append(i)
#     return lst2
#
#
# lst = ['Andgrt', 'bdfvr', 'eniusdnh', 'fhncuf']
# print(words(lst))

# 5. We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
# Write a function to return the number of small bars to use, assuming we always use big bars before small bars. Return
# -1 if it can't be done.
# Մենք ուզում ենք պատրաստել որոշակի x կշռով շոկոլադ։ Ունենք փոքր և մեծ շոկոլադե սալիկներ, որոնք համապատասխանաբար
# կշռում են 1 և 5 կգ։ x կգ շոկոլադը պատրաստելու համար առաջինը օգտագործելու ենք մեծ սալիկները, ապա փոքր։ Սալիկները
# կտրատել հնարավոր չէ։ Գրել ֆունկցիա, որը կվերադարձնի անհրաժեշտ փոքր սալիկների քանակը։ Եթե հնարավոր չէ տրված սալիկների
# քանակով պատրաստել անհրաժեշտ շոկոլադը՝ վերադարձնել -1։
# Ֆւնկցիայի սահմանումն ունի հետևյալ տեսքը, որտեղ small, big -> հասանելի փոքր և մեծ սալիկների քանակը, իսկ goal-ը
# վերոնշյալ x-ն է։

# Ֆունկցիան պետք է ունենա հետևյալ սահմանումը

# def make_chocolate(small, big, goal):
#     if big >= goal // 5:
#         big_q = goal // 5
#     else:
#         big_q = big
#     small_q = goal - big_q*5
#     if small_q > small:
#         return -1
#     else:
#         return small_q
#
#
# small = int(input())
# big = int(input())
# goal = int(input())
# print(make_chocolate(small, big, goal))

# 6. Write a function that gets a numerical list as an argument. Find the sum of the elements. If a certain element is
# 13 stop the count and return whatever was the sum before that.
# Ստեղծել ֆունկցիա, որը կգումարի տրված լիստի բոլոր թվերը և կվերադարձնի այն։ Եթե տարրերից մեկը 13 է, դադարեցնել հաշվարկը
# և վերադարձնել մինչև այդ պահը հաշված գումարը։

# def suml(lst):
#     s = 0
#     for i in lst:
#         if i == 13:
#             return s
#         s += i
#     return s
#
#
# lst = [1, 45, 15, 45, 52, 13, 5, 1, 2, 6, 1, 4, 1]
# print(suml(lst))


""" Dictionaries"""

# 1. Ask for user input and add that input as a key into the dictionary. If the key exists, warn the user about it and
# do nothing. Assign some arbitrary value to it.
# Պահանջել ներմուծել բանալի և ավելացնել այդ բանալին dictionary-ի։ Եթե այն արդեն գոյություն ունի, տպել, որ բանալին արդեն
# կա և ոչինչ չանել։ Որպես արժեք տեղադրել պատահական օբյեկտ

# dict_1 = {'1': 'a', '2': 'b', '3': 'c'}
# key = input('enter key')
# if key in dict_1:
#     print('the key exists')
# else:
#     dict_1[key] = random.randint(1, 10)
#
# print(dict_1)

# 2. Loop through the values of a dictionary and add them to a new list.
# Ցիկլի միջոցով ավելացնել dictionary—ի արժեքները նոր լիստի մեջ։
# lst = []
# dict_1 = {'1': 'a', '2': 'b', '3': 'c'}
# for i in dict_1:
#     lst.append(dict_1[i])
# print(lst)

# 3. Write a script to print a dictionary where the keys are numbers between 1 and 15 (both included)
# and the values are square of keys.
# Գրել ծրագիր, որը կստեղծի և կտպի dictionary, որի բանալիները [1,15] թվերն են, իսկ արժեքները դրանց քառակուսիները։
#
# dict_1 = {}
# for i in range(1, 16):
#     dict_1[i] = i*i
# print(dict_1)
