import numpy as np
import time


def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

def bubblesort(x):

    """
    Describe how you are sorting `x`
"""

    #Bubble sort for integers

    #Pre-condition is in run file (only integers or floats)
    #Outer loop: make as many passes through array as there are members
    for i in range(len(x)):
        #Inner for loop goes through the array and swaps adjacent items if they are out of order.
        for j in range(len(x)-1):
            # If adjacent items are out of order, swap them
            if( x[j] > x[j+1] ):
                t = x[j+1]
                x[j+1] = x[j]
                x[j] = t

    return x

def quicksort(x):
    """
    Describe how you are sorting `x`
    """
    con = 0
    asn = 0
# Quicksort input function to tell initial values of p and r. Initial pivot point is in the middle of the array.
    def quicksortinput(x):
       quicksort(x,0,len(x)-1)

# Recursive quicksort function, partitions the array and then quicksorts each partition.
    def quicksort(x,p,r):
       if p < r:
           con = con + 1

           pivot = partition(x,p,r)
           asn = asn + 1

           quicksort(x,p,pivot-1)
           quicksort(x,pivot+1,r)

# Partition function: finds pivot value, defines the left value as the one directly above pivot value, and compares this to the right value.
    def partition(x,p,r):
       pivotval = x[p]
       left = p + 1
       right = r
# While left <= right:
       while left <= right:
           con = con + 1
           #move left up until you reach a value that is less than the pivot value
           while x[left] <= pivotval:
               con = con + 1
               left = left + 1
               asn = asn + 1
            #move right down until you reach a value that is greater than the pivot value
           while x[right] > pivotval:
               con = con + 1
               right = right -1
               asn = asn + 1
               # swap left and right
           if left < right:
             con = con + 1
             t = x[right]
             x[right] = x[left]
             x[left] = t
             asn = asn + 3
        # swap pivot value and right
       t = x[p]
       x[p] = x[right]
       x[right] = t
       asn = asn + 3
       # return right for use as new pivot value
       return right
    return x
