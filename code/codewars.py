#cat years dog years

# def human_years_cat_years_dog_years(human_years):
#     if human_years == 1:
#         cat_years = 15
#         dog_years = 15
#     elif human_years == 2:
#         cat_years = 24
#         dog_years = 24
#     else:
#         cat_years = 24 + (human_years - 2) * 4
#         dog_years = 24 + (human_years - 2) * 5
        
#     return [human_years, cat_years, dog_years]

#nearest square number

# def nearest_sq(n):
#     r = round(n ** 0.5)
#     return r ** 2


#sum of array singles
# def repeats(arr):
#     summ = 0
#     for i in arr:
#         if arr.count(i) == 1:
#             summ += i
#     return summ



#find the mine

# def mine_location(field):
#     for r_index, row in enumerate(field):
#         if 1 in row:
#             return [r_index,row.index(1)]


#rot13

# def rot13(message):
#     newmessage = ''
#     myabc = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     for i in message:
#         if i in myabc:
#             newmessage += myabc[myabc.index(i) + 13]
#         else:
#             newmessage += i
#     return newmessage

# triangular treasure

# def triangular(n):
#     if n < 1:
#         return 0
#     else:
#         return n * (n + 1) // 2


#hashtag generator

# def generate_hashtag(s):
#     if not s:
#         return False
#     s = s.split()
#     s = [word.capitalize() for word in s]
#     hash = "#" + "".join(s)
#     if len(hash) > 140:
#         return False
#     return hash

#variance

# import numpy as np
# def variance(numbers):
#     return np.var(numbers)

#permutatuibs

#xerxi 1 ar mushaobs ;/ (damtanja)
# def permutations(s):
#     result = [s]
#     if len(s) == 2:
#         result.append(s[1] + s[0])
#     elif len(s) > 2:
#         for index, num in enumerate(s):
#             for s in s[index: ] + s[:index]:
#                 result.append(num)
#     return list(result)

#advili xerxi 2

# import itertools
# def permutations(s):
#     permutation = ["".join(i) for i in itertools.permutations(s)]
#     return set(permutation)