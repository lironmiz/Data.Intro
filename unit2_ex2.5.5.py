# 1: 
'''
What will be the result of running the following code:'
'''
import numpy as np
arr = np.array([6, -2, 4, 7, 2])
arr + 3

# Answer: array([ 9, 1, 7, 10, 5])

# 2: 
'''
What will be the result of running the following code:'
'''

arr1 = np.array([6, -2, 4, 7, 2])
arr2 = np.array([4, 4, 2, 2, 1])

arr1 + arr2

# Answer: array([10, 2, 6, 9, 3])

# 3: 
'''
Look at the code in front of you:

arr = np.array([2, 4, 25, 529])
np.sqrt(arr)
Determine whether the result of running the code is:
array([ 1.41421356, 2. , 5. , 23. ])
'''

# Answer: yes

# 4: 
'''
Write a function that adds zeros at the end of an array according to the length of the given array and its desired length.
The function signature:
def pad_zeros(arr, new_length)

input:
arr: a numpy array
new_length: integer (int)

output:
new_arr: an array of length new_len, where the members of arr are in the first places, and zeros in the rest.
If new_len is exactly equal to or shorter than the length of arr, arr must be returned unchanged.
'''

import numpy as np

def pad_zeros(arr, new_length):
    if len(arr) >= new_length:
        return arr
    else:
        padding = np.zeros(new_length - len(arr))
        new_arr = np.concatenate((arr, padding))
        return new_arr

'''
part 2: 
In a certain office, the employees recorded the amount of soft drink cans they
consumed during the day. For each employee there is a numpy array by days, starting 
from the first day of the experiment. Some of the workers stopped consuming soft drink
cans after a few days, so the length of the arrays is not uniform.
You must produce an array in which the total of cans consumed daily.
Function signature: def sum_arrays(arr_list)
arr_list: a list in which each entry is a numpy array.
Output: a numpy array whose length is the length of the longest array in the list,
and it contains the amount of cans consumed daily, that is:
The first entry in the array shows the sum of all the first elements in all the arrays
The second entry in the array shows the sum of all the second terms (if any) and so on.


'''

def sum_arrays(arr_list):
    longest_array = max(arr_list, key=len)
    return np.add.reduce(arr_list, axis=0)[:len(longest_array)]
  
