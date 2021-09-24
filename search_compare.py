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
    # a_list = [random.randint(1, 9) for a in range(n)]
    return a_list


def sequential_search(a_list,item):

    #start = time.time()

    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1

    #end = time.time()

    #elapsed = end - start 

    return found #, elapsed
    

def ordered_sequential_search(a_list,item):
    pass


def binary_search_iterative(a_list,item):
    pass
    
    
def binary_search_recursive(a_list,item):
    pass



if __name__ == "__main__":
    """Main entry point"""

    t1 = Timer("sequential_search({},{})".format(get_me_random_list(500), -1), setup="from __main__ import sequential_search")
    seq_ser_avg = t1.timeit(number=500)
    #print(seq_ser_avg)
   
        ##https://stackabuse.com/python-string-interpolation-with-the-percent-operator/
    print(f"Result is {sequential_search(get_me_random_list(500), -1)}. Operation required {seq_ser_avg} seconds")



    # t1 = Timer("get_me_random_list({})".format(args.n), setup="from __main__ import get_me_random_list")
    # print(f"random list generator takes: {t1.timeit(number=1000)} seconds")