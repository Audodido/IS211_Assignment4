import argparse
# other imports go here
from timeit import Timer
import timeit
import time 
import random


def get_me_random_list(n, rand_val=True):
    """Generate list of n elements in random or ordered"""

    a_list = list(range(n)) 
    random.shuffle(a_list)

    if rand_val:    
        return a_list
    
    else:
        a_list.sort()
        return a_list

def sequential_search(a_list,item):

    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found 
    

def ordered_sequential_search(a_list,item):
    
    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos+1

    return found


def binary_search_iterative(a_list,item):
    first = 0
    last = len(a_list) - 1
    found = False
    
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found
        
    
def binary_search_recursive(a_list,item):

    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        return True
    else:
        if item < a_list[midpoint]:
            return binary_search(a_list[:midpoint], item)
        else:
            return binary_search(a_list[midpoint + 1:], item)


def time_getter(func, n, rand_val=True):
    """Takes n and calls list gen function then gets average time for func to run"""

    t1 = Timer("{}({},{})".format(func, get_me_random_list(n, rand_val), 99999999), setup="from __main__ import {}".format(func))
    func_avg = t1.timeit(number=100)
    
    return func_avg


if __name__ == "__main__":
    """Main entry point"""

    #SEQUENTIAL SEARCH
    # average durations for lists that are 500, 1000, 5000 in length
    ss_avg_duration_500 = time_getter("sequential_search", 500)
    ss_avg_duration_1000 = time_getter("sequential_search", 1000)
    ss_avg_duration_5000 = time_getter("sequential_search", 5000)
    # average of the average durations
    ss_total_duration = sum([ss_avg_duration_500, ss_avg_duration_1000, ss_avg_duration_5000]) / len([ss_avg_duration_500, ss_avg_duration_1000, ss_avg_duration_5000])

    # ORDERED SEQUENTIAL SEARCH
    # average durations for lists that are 500, 1000, 5000 in length
    oss_avg_duration_500 = time_getter("ordered_sequential_search", 500, False)
    oss_avg_duration_1000 = time_getter("ordered_sequential_search", 1000, False)
    oss_avg_duration_5000 = time_getter("ordered_sequential_search", 5000, False)
    # average of the average durations
    oss_total_duration = sum([oss_avg_duration_500, oss_avg_duration_1000, oss_avg_duration_5000]) / len([oss_avg_duration_500, oss_avg_duration_1000, oss_avg_duration_5000])

    # BINARY SEARCH ITERATIVE
    bsi_avg_duration_500 = time_getter("binary_search_iterative", 500, False)
    bsi_avg_duration_1000 = time_getter("binary_search_iterative", 1000, False)
    bsi_avg_duration_5000 = time_getter("binary_search_iterative", 5000, False) 
    # average of the average durations  
    bsi_total_duration = sum([bsi_avg_duration_500, bsi_avg_duration_1000, bsi_avg_duration_5000]) / len([bsi_avg_duration_500, bsi_avg_duration_1000, bsi_avg_duration_5000])

    # BINARY SEARCH RECURSIVE
    bsr_avg_duration_500 = time_getter("binary_search_iterative", 500, False)
    bsr_avg_duration_1000 = time_getter("binary_search_iterative", 1000, False)
    bsr_avg_duration_5000 = time_getter("binary_search_iterative", 5000, False) 
    # average of the average durations  
    bsr_total_duration = sum([bsr_avg_duration_500, bsr_avg_duration_1000, bsr_avg_duration_5000]) / len([bsr_avg_duration_500, bsr_avg_duration_1000, bsr_avg_duration_5000])



    #OUTPUTS
    print("Sequential Search took%10f seconds to run, on average" % ss_total_duration)
    print("Ordered Sequential Search took%10f seconds to run, on average" % oss_total_duration)
    print("Binary Search Iterative took%10f seconds to run, on average" % bsi_total_duration)
    print("Binary Search Recursive took%10f seconds to run, on average" % bsr_total_duration)

