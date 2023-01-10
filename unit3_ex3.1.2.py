# exercise 3.1.2 from unit 3

# 1: How does the median method react in the case of a series where the number of data is even?

# Answer: Calculating the average between the two middle data

''' 
2: Write a function that receives a series of data (of type List) and calculates their median,
without using external libraries. To make the task easier, assume that the length of the series 
is odd. Make sure your implementation is correct (e.g. by comparing to pandas). Please note - 
it is necessary to import libraries, define variables, etc.
For example, for the input:
MyList = [3.12, 3.52, 3.4, 2.78, 3.68]
We will get the output:
3.4
'''
from math import sqrt

def calc_median (x):
    x.sort()
    return x[len(x) // 2]

print(calc_median([8, 5, 3, 1, 10, 12, 4]))
print(pd.Series([8, 5, 3, 1, 10, 12, 4]).median())

'''
3: For flying_mice_song_lengths from the previous question-
Use built-in python functions to calculate standard deviation without using external
libraries, other than those that exist in the Python standard library
'''

def calc_std(x):
    x_mean = sum(x) / len(x)
    squared_diffs_sum = 0
    for value in x:
        squared_diffs_sum += (value - x_mean) ** 2

    return sqrt(squared_diffs_sum / len(x))


print(calc_std(flying_mice_song_lengths))

