# Max and Min in a Unsorted Array
# In this problem, we will look for smallest and largest integer from a list of unsorted integers. 
# The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

# Bonus Challenge: Is it possible to find the max and min in a single traversal?

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return None, None

    min_num = ints [0]
    max_num = ints [0]

    for num in ints:
        if num > max_num:
            max_num = num

        if num < min_num:
            min_num = num

    return min_num, max_num


print ("Pass" if ((0, 55) == get_min_max([5,5,55,1,2,3, 6,2, 0, 9])) else "Fail")
print ("Pass" if ((None, None) == get_min_max([])) else "Fail")
print ("Pass" if ((1, 1) == get_min_max([1])) else "Fail")
print ("Pass" if ((1, 1) == get_min_max([1,1,1,1,1])) else "Fail")
# Sorting usually requires O(n log n) time Can you come up with a O(n) algorithm (i.e., linear time)?