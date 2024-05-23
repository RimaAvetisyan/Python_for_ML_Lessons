""" Dictionaries, Sets """
import random

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
# and the values are square of keys. Do this using loops and comprehensions.
# Գրել ծրագիր, որը կստեղծի և կտպի dictionary, որի բանալիները [1,15] թվերն են, իսկ արժեքները դրանց քառակուսիները։
# Առաջադրանքը կատարել և՛ loop-երով, և՛ comprehension—ներով։


# dict_1 = {}
# for i in range(1, 16):
#     dict_1[i] = i*i
# print(dict_1)

#
# dict_1 = {i: i*i for i in range(1, 16)}
# print(dict_1)

# 4. Create 2 sets and find their symmetric difference without using the dedicated method.
# Ստեղծել 2 սեթ և առանց symmetric_difference-ը գործածելու գտնել դրանց սիմետրիկ տարբերությունը։

# set1 = {2, 4, 5, 8}
# set2 = {3, 4, 5}
# set3 = set1.union(set2)
# set4 = set()
# for i in set3:
#     if i not in set1 or i not in set2:
#         set4.add(i)
#
# print(set4)
#
# print(set1.symmetric_difference(set2))

# 5․ Write a Python program to remove the intersection of a 2nd set from the 1st set.
# Գրել ծրագիր, որը կջնջի սեթերի հատումն առաջին սեթից։

# set1 = {2, 4, 5, 8}
# set2 = {3, 4, 5}
# set3 = set1.difference(set2)
#
# print(set3)

""" Functions """

# 1.  Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target.

#
# def integer(lst, tar):
#     for i in range(len(lst)-1):
#         if lst[i]+lst[i+1] == tar:
#             return i, i+1
#
#
# lst = [1, 5, 25, 85, 5, 6, 8, 9, 47]
# print(integer(lst, 6))

# 2․ You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future
# to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


# def maxprofit(prices):
#     maxi = 0
#     for i in range(len(prices)):
#         for j in range(i, len(prices)):
#             if prices[j] - prices[i] > maxi:
#                 maxi = prices[j]-prices[i]
#     return maxi
#
#
# prices = [5, 6, 8, 11, 15, 4, 6, 8]
# print(maxprofit(prices))

# 3. Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements
# of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# (Optional) You must write an algorithm that runs in O(n) time and without using the division operation.


# def answer(nums):
#     n = len(nums)
#     result = [1] * n
#     d = 1
#     for i in range(n):
#         result[i] *= d
#         d *= nums[i]
#     d = 1
#     for i in range(n - 1, -1, -1):
#         result[i] *= d
#         d *= nums[i]
#     return result
#
#
# lst = [2, 6, 5]
# print(answer(lst))


# 4. You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Example:
#   Input: n = 3
#   Output: 3
#   Explanation: There are three ways to climb to the top.
#     1. 1 step + 1 step + 1 step
#     2. 1 step + 2 steps
#     3. 2 steps + 1 step

# def countways(n):
#     if n <= 3:
#         return n
#     return countways(n - 1) + countways(n - 2)
#
#
# s = 5
# print("Number of ways = ", countways(s))


# 5. Hangman!
# Create the hangman game. A list containing random words is provided. Each time the program runs, one random word must
# be selected. Then the user will try to guess the letters of the word. They will have lives equal to the length of the
# word. Now, about the formatting. Say we have the word car. The program must then output underscores equal to the
# length of the word.

# Guess a letter!
# _ _ _
#
# if we input 'a', the program will output:

# Guess a letter!
# _ a _

# and so on.

# Ստեղծում ենք մեր սեփական "Կախաղան" խաղը։ Ծրագիրը պահելու է պատահական բառ տրված "random_words" ֆայլից: Խաղացողը պետք է
# գուշակի տառ։ Եթե տառը բառի մեջ գոյություն չունի, խաղացողը կորցնում է "կյանք" (կյանքերը բառի երկարության չափ են): Եթե
# տառը կա, այն բացվում է և խաղացողը անցնում է հաջորդ տառը գուշակելուն։ Ծրագրի աշխատանքը պետք է հետևյալ տեսքն ունենա։
# Ենթադրենք բառը car է։ Կոնսոլում հետևյալ տեսքստն ենք տեսնելու

# Guess a letter!
# _ _ _

# Եթե ներմուծենք a, կստանանք հետևյալ տեսքստը

# Guess a letter!
# _ a _

# և այդպես շարունակ։ Եթե խաղացողի կյանքերը սպառվեն, տեղեկացրեք նրան և խաղից դուրս եկեք։ Հաղթելու դեպքում տպեք
# շնորհավորանք
#
# random_words = ['apple', 'girl', 'boy', 'women']
# word = random_words[random.randint(0, len(random_words))]
# blank = '-'*len(word)
# print('Guess a letter! \n ', blank)
# lives = len(word)
# while lives > 0:
#     letter = input()
#     if letter in word:
#         i = word.index(letter)
#         blank = blank[0:i]+letter+blank[i+1:]
#     else:
#         lives -= 1
#     if '-' not in blank:
#         print('You win!')
#         print('Word ---', blank)
#         break
#     if lives == 0:
#         print('Game over...')
#     else:
#         print('Guess a letter! \n ', blank)





