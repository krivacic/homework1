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

# Quicksort input function to tell initial values of p and r. Initial pivot point is in the middle of the array.
    def quicksortinput(x):
       quickSortHelper(x,0,len(x)-1)

# Recursive quicksort function, partitions the array and then quicksorts each partition.
    def quickSortHelper(x,p,r):
       if p < r:

           pivot = partition(x,p,r)

           quickSortHelper(x,p,pivot-1)
           quickSortHelper(x,pivot+1,r)

# Partition function: finds pivot value, defines the left value as the one directly above pivot value, and compares this to the right value.
    def partition(x,p,r):
       pivotval = x[p]

       left = p + 1
       right = r
# While left < right, if the value left is less than the value of right, swap left and right. Otherwise go to the next item in the array.
       while left < right:
           if left < right:
               t = x[right]
               x[right] = x[left]
               x[left] = t
           while left <= right and x[left] <= pivotval:
               left = left + 1

           while x[right] >= pivotval and right >= left:
               right = right -1

       t = x[p]
       x[p] = x[right]
       x[right] = t

       return right

    quicksortinput(x)
    return x
