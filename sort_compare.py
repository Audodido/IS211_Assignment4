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
    

def insertion_sort(a_list):

    for index in range(1, len(a_list)):

        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
            
        a_list[position] = current_value


def shell_sort(a_list):

    sublist_count = len(a_list) // 2

    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)

        sublist_count = sublist_count // 2

def gap_insertion_sort(a_list, start, gap):

    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
    
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
            a_list[position] = current_value
    
    return a_list
            


def python_sort(a_list):

    a_list.sort()

    return a_list


def time_getter(func, n):
    """Takes n and calls list gen function then gets average time for func to run"""

    n = n // 2

    t1 = Timer("{}({})".format(func, get_me_random_list(n)), setup="from __main__ import {}".format(func))
    func_avg = t1.timeit(number=100)

    return func_avg



if __name__ == "__main__":
    """Main entry point"""

    #INSERTION SORT
    is_avg_duration_500 = time_getter("insertion_sort", 500)
    is_avg_duration_1000 = time_getter("insertion_sort", 1000)
    is_avg_duration_5000 = time_getter("insertion_sort", 5000)
    # average durations for lists that are 500, 1000, 5000 in length
    is_total_duration = sum([is_avg_duration_500, is_avg_duration_1000, is_avg_duration_5000]) / len([is_avg_duration_500, is_avg_duration_1000, is_avg_duration_5000])

    #SHELL SORT
    ss_avg_duration_500 = time_getter("shell_sort", 500)
    ss_avg_duration_1000 = time_getter("shell_sort", 1000)
    ss_avg_duration_5000 = time_getter("shell_sort", 5000)
    ss_total_duration = sum([ss_avg_duration_500, ss_avg_duration_1000, ss_avg_duration_5000]) / len([ss_avg_duration_500, ss_avg_duration_1000, ss_avg_duration_5000])

    #PYTHON SORT
    ps_avg_duration_500 = time_getter("shell_sort", 500)
    ps_avg_duration_1000 = time_getter("shell_sort", 1000)
    ps_avg_duration_5000 = time_getter("shell_sort", 5000)
    ps_total_duration = sum([ps_avg_duration_500, ps_avg_duration_1000, ps_avg_duration_5000]) / len([ps_avg_duration_500, ps_avg_duration_1000, ps_avg_duration_5000])


    #OUTPUTS
    print("Insertion Sort took%10f seconds to run, on average" % is_total_duration)
    print("Shell Sort took%10f seconds to run, on average" % ss_total_duration)
    print("Python Sort took%10f seconds to run, on average" % ps_total_duration)