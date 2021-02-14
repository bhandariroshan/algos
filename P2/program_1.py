# Finding the Square Root of an Integer
# Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

# For example if the given number is 16, then the answer would be 4.

# If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

# The expected time complexity is O(log(n))

# Here is some boilerplate code and test cases to start with:

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if number == 1 or number == 0:
        return number

    is_complex = False
    if number < 0:
        is_complex = True

    number = abs(number)
    low = 0 
    high = number
    mid = None
    old_mid = None

    while old_mid ==None or old_mid != mid:
        if mid:
            old_mid = mid
        mid = (low + high) // 2
        if mid**2 > number:
            high = mid
        else:
            low = mid

    if is_complex:
        number = str(mid) + 'i'

    return mid


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  ('i' == sqrt(-1)) else "Fail")
print ("Pass" if  ('3i' == sqrt(-1)) else "Fail")