# import random

# def get_me_random_list(n, rand_val=True):
#     """Generate list of n elements in random or non-random order"""

#     if rand_val:    
#         a_list = list(range(n)) 
#         random.shuffle(a_list)
#         # a_list = [random.randint(1, 9) for a in range(n)]
#         return a_list
    
#     else:
#         a_list = list(range(n)) 
#         return a_list

# print(get_me_random_list(10, False))

import argparse
# other imports go here
from timeit import Timer
import timeit
import time 
import random



def get_me_random_list(n):
    """Generate list of n elements in random order"""

    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


# def insertion_sort(a_list):

#     for index in range(1, len(a_list)):

#         current_value = a_list[index]
#         position = index

#         while position > 0 and a_list[position - 1] > current_value:
#             a_list[position] = a_list[position - 1]
#             position = position - 1
            
#         a_list[position] = current_value



# def time_getter(func, n):
#     """Takes n and calls list gen function then gets average time for func to run"""

#     n = n // 2

#     t1 = Timer("{}({})".format(func, get_me_random_list(n)), setup="from __main__ import {}".format(func))
#     func_avg = t1.timeit(number=100)
    
#     return func_avg


# def python_sort(a_list):

#     a_list.sort()

#     return a_list

# a_list = get_me_random_list(30)
# # insertion_sort(a_list)
# # print(time_getter("insertion_sort", 500))

# print(python_sort(a_list))



def get_me_random_list(n):
    """Generate list of n elements in random order"""

    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list
    

def insertion_sort(a_list):

    for index in range(1, len(a_list)):

        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
            
        a_list[position] = current_value

    
def time_getter(func, n):
    """Takes n and calls list gen function then gets average time for func to run"""

    n = n // 2

    t1 = Timer("{}({})".format(func, get_me_random_list(n)), setup="from __main__ import {}".format(func))
    func_avg = t1.timeit(number=100)

    return func_avg


is_avg_duration_5000 = time_getter("insertion_sort", 5000)

print(is_avg_duration_5000)
