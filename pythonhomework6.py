""" numpy """
# զանգված -> numpy array

import numpy as np
import random

# 1. Ստեղծել np զանգված, որը կպարունակի 100 պատահական ամբողջ թիվ։ Այնուհետև ստանալ այն տարրերի ինդեքսները,
# որոնք ավարտվում են 6-ով։

# arr = np.random.randint(0, 50, 100)
# print(arr)
# for i in range(len(arr)):
#     if arr[i] % 10 == 6:
#         print(i, end=', ')

# 2. Ստեղծել np զանգված, որի բոլոր տարրերը կլինեն 0-ներ, իսկ անկյունագծայինները՝ 1։


# n = int(input('n='))
# arr = np.eye(n, n, dtype=int)
# print(arr)

# 3. Ստեղծել երկու np միաչափ զանգված արդեն պատրաստի պիտոնական լիստերից։ Ապա կցեք երկու զանգվածներն իրար
# հորիզոնական ուղությամբ։

# lst1 = [1, 2, 5, 8, 6, 4, 5, 4, 8]
# lst2 = [5, 2, 5, 4, 6, 1, 5, 9, 6]
# arr1 = np.array(lst1)
# arr2 = np.array(lst2)
#
# arr3 = np.append(arr1, arr2)
# arr3.shape = (2, len(lst1))
# print(arr3)

# 4. Ստեղծել երկու np միաչափ զանգված արդեն պատրաստի պիտոնական լիստերից։ Ապա կցեք երկու
# զանգվածներն իրար վերտիկալ ուղությամբ։

# lst1 = [1, 2, 5, 8, 6, 4, 5, 4, 8]
# lst2 = [5, 2, 5, 4, 6, 1, 5, 9, 6]
# arr1 = np.array(lst1)
# arr2 = np.array(lst2)
#
# arr3 = np.append(arr1, arr2)
# arr3.shape = (len(lst1), 2)
# print(arr3)


# 5. Ստեղծել երկչափ զանգված, որը կունենա (3, 3) shape: Այնուհետև ստեղծել նոր զանգված, որը կլինի նախորդ զանգվածը, սակայն
# առաջին և երրորդ սյուների տեղերը փոխած։

# arr = np.random.randint(0, 10, (3, 3))
# print(arr)
# arr1 = np.copy(arr)
# arr1[0] = arr[2]
# arr1[2] = arr[0]
# print(arr1)

# 6.  Ստեղծել երեք զանգված։ Առաջինը պետք է պարունակի միայն 0-ներ, երկրորդը միայն 1-եր, իսկ երրորդը միայն 9-եր։

# n = int(input('n='))
# arr1 = np.zeros(n, dtype=int)
# arr2 = np.ones(n, dtype=int)
# arr3 = arr2*9
# print(arr1, arr2, arr3)

# 7. Ստեղծել (10, 10) shape-ով զանգված։ Ապա փոխել դրա shape-ը հնարավոր բոլոր տարբերակներով։
#
# arr = np.random.randint(0, 1, (10, 10))
# print(arr)
# for i in range(101):
#     for j in range(101):
#         if i * j == 100:
#             arr.shape = (i, j)
#             print(f"({i},{j})")
#             print(arr)


# 8. Ստեղծել երկու երկչափ զանգված և հաշվել դրանց ա) տարր առ տարր արտադրյալը, բ) մատրիցային արտադրյալը։

# arr1 = np.random.randint(0, 5, (4, 4))
# arr2 = np.random.randint(0, 5, (4, 4))
# print(arr1)
# print(arr2)
# print(arr1*arr2)
# print(np.dot(arr1, arr2))

# 9. Ստեղծել երկու զանգված (10, 10) shape-ի, որոնք կպարունակեն 0-ից 20-ը պատահական թվեր։ Բաժանել մատրիցներն իրար։
# Այնուհետև առանձնացնել նոր մատրիցի մեջ մատրիցների այն տարրերը, որոնք թիվ են (inf կամ nan չեն): Ստանալ inf-երի և
# nan-երի նաև դրանց ինդեքսները։
#
# arr1 = np.random.randint(0, 20, (10, 10))
# arr2 = np.random.randint(0, 20, (10, 10))
#
# arr3 = np.divide(arr1, arr2)
# print("this is divided array", arr3)
#
# arr4 = arr3[(arr3 != np.inf) & (arr3 != np.nan)]
# print('this is cleaned array', arr4)
#
# print('this is index array', (arr3 == np.inf) | (arr3 == np.nan))
#

# 10. Ստեղծել (3, 3) մատրից, որի տարրերը կլինեն 11-19, սակայն բացահայտ կերպով սահմանել տարրերի տիպը որպես float։

# arr = np.arange(11, 20, dtype=float).reshape((3, 3))
#
# print(arr)

""" numpy Part 2 """

# 1. Create a numpy array from a python list consisting even numbers from 0-20.
# 0-20 զույգ թվերը պարունակող Python լիստից ստեղծել զանգված

# lst = []
# for i in range(0, 21, 2):
#     lst.append(i)
# print(lst)
# arr = np.array(lst)
# print(arr)

# 2. Create a 3x3 numpy array, which will contain 3s only.
# Ստեղծել 3x3 զանգված, որը կպարունակի միայն 3-ներ:

# arr = np.ones((3, 3), dtype=int)*3
# print(arr)

# 3. Create a 1D numpy array with length 18. Reshape it to 3 columns and 6 rows.
# Ստեղծել միաչափ զանգված 18 երկկարությամբ։ Ապա այն դարձնել երկչափ զանգված, որը կունենա 3 սյուն և 6 տող։

# arr = np.arange(18)
# print(arr)
# a = arr.reshape((6, 3))
# print(a)

# 4. Create two numpy arrays of shape 10x10. One of them must contain the numbers from 1-100, the other from 100-1.
# Add them and output the result.
# Ստեղծել 10x10 երկու զանգված, որոնցից մեկը կպարունակի 1-100 թվերը, իսկ մյուսը՝ 100-1։ Գումարել դրանք և վերադարձնել
# արդյունքը։

# arr1 = np.arange(1, 101)
# arr2 = np.arange(100, 0, -1)
#
# print(arr1+arr2)


# 5. In how many ways can we reshape an array of length 12? Write down all the possibilities (2D).
# Քանի՞ ձևով կարող ենք 12 երկարությամբ զանգվածի կառուցվածքը փոխել (reshape)։ Գրել բոլոր հնարավոր (2D) տարբերակները։

# arr = np.ones(12)
# print(arr)
# for i in range(13):
#     for j in range(13):
#         if i * j == 12:
#             arr.shape = (i, j)
#             print(f"({i},{j})")
#             print(arr)


# 6. Create an array of shape (5, 5) that will contain zeros except for the diagonal. The diagonal should be all 4s.
# Ստեղծել 5x5 զանգված, որը կպարունակի 0-ներ բացառությամբ անկյունագծից։ Անկյունագծի տարրերը պետք է լինեն 4։
#
# arr = np.eye(5, dtype=int)*4
# print(arr)


# 7․ Create a numpy array that will contain random numbers from 0, 100 and will have 20 columns with 5 rows.
# Ստեղծել 0-100 պատահական թվերից կազմված զանգված, որը կունենա 5 տող և 20 սյուն։

# arr = np.random.randint(0, 100, (5, 20))
# print(arr)

# 8․ Create a 3 dimensional array from a 1 dimensional array of length 100.
# Ստեղծել եռաչափ զանգված 100 տարր պարունակող միաչափ զանգվածից։

# arr = np.arange(100)
# print(arr)
# a = arr.reshape(5, 5, 4)
# print(a)

# 9. Create a 3x3 array containing random numbers from (0, 1). Then, change the datatype of the array to integers
# (you need to do some googling for this).
# Ստեղծել 3x3 չափսի զանգված, որը կպարունակի 0-1 պատահական տվեր։ Ստեղծելուց հետո, փոխել զանգվածի արժեքների տիպը ամբողջ
# թվերի (պետք կլինի գուգլում փնտրել համապտասխան մեթոդը)։

# arr = np.random.randint(0, 2, (3, 3))
# print(arr.dtype)
# arr = arr.astype('float64')
# print(arr.dtype)

# 10. Create two arrays of shape 3x3 that will contain random numbers from 1-100. Calculate their scalar product,
# dot product, division and difference. Use np methods AND corresponding operators.
# Ստեղծել երկու 3x3 զանգված։ Դրանք պետք է պարունակեն 1-100 պատահական թվեր։ Այնուհետև հաշվել դրանց սկալար արտադրյալը
# (համապտասխան տարրերն իրար հետ), վեկտորական արտադրյալը, քանորդը և տարբերությունը։ Օգտվել և՛ մեթոդներից և՛ համապատասխան
# օպերատորներից։

# arr1 = np.random.randint(1, 101, (3, 3))
# arr2 = np.random.randint(1, 101, (3, 3))
#
# print(arr1*arr2)
# print(np.multiply(arr1, arr2))
#
# print(arr1@arr2)
# print(np.dot(arr1, arr2))
#
# print(arr1/arr2)
# print(np.divide(arr1, arr2))
#
# print(arr1-arr2)
# print(np.subtract(arr1, arr2))


# 11. Create an array of shape 5x5. Calculate its determinant. If the determinant is non-zero, calculate the inverse as
# well. Otherwise, tell the user that the matrix in non-invertible.
# Ստեղծել 5x5 զանգված։ Հաշվել դրա որոշիչը։ Եթե այն 0 չէ, հաշվել մատրիցի հակադարձը։ Հակառակ դեպքում տպել, որ մատրիցը
# հակադարձելի չէ։

# arr = np.random.randint(1, 5, (5, 5))
# deter = np.linalg.det(arr)
#
# if deter == 0:
#     print('the matrix is non-invertible')
# else:
#     print(deter)
#     print(np.linalg.inv(arr))

# 12. Create an array of shape 3x3 that will contain numbers from 1-10. Calculate the scalar and dot products
# of it with its transposed version.
# Ստեղծել 1-10 թվերը պարունակող 3x3 զանգված։ Հաշվել դրա և իր տրանսպոնացված մատրիցի սկալար և վեկտորական արտադրյալները։

# arr = np.random.randint(1, 11, (3, 3))
# arr1 = arr.transpose()
# print(arr)
# print(arr1)
# print(arr*arr1)
# print(arr@arr1)

# 13. Create a 3x3 array of random integers. Calculate its inverse (check if possible). Then find the vector product of
# these. What do you get?
# Ստեղծել պատահական ամբողջ թվեր պարունակող 3x3 զանգված։ Հաշվել դրա հակադարձը, եթե հնարավոր է (կրկին ստուգել որոշիչի
# պայմանը)։ Ապա հաշվել հակադարձի և օրիգինալ զանգվածների վեկտորական արտադրյալը։ Ի՞նչ կստանանք։

# arr = np.random.randint(1, 11, (3, 3))
#
# deter = np.linalg.det(arr)
#
# if deter == 0:
#     print('the matrix is non-invertible')
# else:
#     a=np.linalg.inv(arr)
#     print(a)
#
# eye = a@arr
# print(np.around(eye).astype(int))