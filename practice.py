import random

def get_me_random_list(n, rand_val=True):
    """Generate list of n elements in random or non-random order"""

    if rand_val:    
        a_list = list(range(n)) 
        random.shuffle(a_list)
        # a_list = [random.randint(1, 9) for a in range(n)]
        return a_list
    
    else:
        a_list = list(range(n)) 
        return a_list

print(get_me_random_list(10, False))