# You can do all of this in the `__main__.py` file, but this file exists
# to shows how to do relative import functions from another python file in
# the same directory as this one.
import numpy as np
from .algs import quicksort, bubblesort
import time


def run_stuff():
    """
    This function is called in `__main__.py`
    """
    print("This is `run()` from ", __file__)

    # x = np.random.rand(11)
    # x = np.array([0,1,8,5,6,6,7])
    # x = np.random.randint(10000, size = (100))
    # x = np.array([7,3,7,4,0,10,11,1])


    for i in range(100,1001,100):
        for q in range(100):
            x = np.random.randint(10000, size = (i))
            print("Unsorted input: ", x)
            if all(isinstance(item,float) for item in x) or all(isinstance(item,np.int64) for item in x):
                startbs = time.time()
                print("Bubble sort output: ", bubblesort(x))
                endbs = time.time()

                text_file = open('output_bubblesort_' + str(i) + '.txt', 'a')
                text_file.write(str(endbs - startbs) + '\n')
                text_file.close()

                startqs = time.time()
                print("Quick sort output: ", quicksort(x))
                endqs = time.time()

                text_file = open('output_quicksort_' + str(i) + '.txt', 'a')
                text_file.write(str(endqs - startqs) + '\n')
                text_file.close()
            else:
                print("Error: Input must be an array of floats or integers.")
