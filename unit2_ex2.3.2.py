# exercise 1: 
'''
Given the data series words, which has the values and indexes as shown in the following code:

[ ] words
8 The
2 quick
6 brown
1 fox
7 jumps
5 overs
4 the
0 lazy
3 dogs
dtype: object
'''

# exercise 1.1: Which command will give us the output 'The'?

# Answer: words.iloc[0]

# exercise 1.2: Which command will give us the output 'fox'?

# Answer: words.loc[1]

# exercise 1.3: Which command will give us the output 'dogs'?

# Answer: words.iloc[-1]

# exercise 2:
'''
A slice operation on a data series also supports placement. Write a placement into
slice so that series_of_strings contains the following series:

[ ] series_of_strings
0 this
1 is
2 blah
3 blah
4 blah
dtype: object

'''
# Answer: series_of_strings.iloc[2:]="bla"

# exercise 3:
'''
We know that the dtype of the data series series_of_numbers is int64.
What will be the dtype after the next placement?

'''
# Answer: object

# exercise 4:
'''
We have identified the following data series:

[ ] series_of_strings
First this
Second is
Third a
Fourth Pandas
Fifth Series
dtype: object

Which of the expressions will return the result:

Third a
Fifth Series
dtype: object

'''
# Answer: series_of_strings.iloc[2::2]

# exercise 5:
'''
We created a data series:

[ ] series_of_strings = pd.Series(['this','is','a','Pandas','Series'])
We saw that it is possible to refer to the members of the series with the help of iloc.
Now it seems that to retrieve more than one array, iloc can also accept a list of locations.
Write an expression that creates (by passing a list of positions to the iloc method of series_of_strings) the following series:

3 Pandas
1 is
2 a
3 Pandas
4 Series
dtype: object

'''
# Answer: series_of_strings.iloc[[3, 1, 2, 3, 4]]

# exercise 6:
'''
We have seen that it is possible to perform truncation when accessing a series with iloc.
Is it possible to cut even when using loc? Are there any differences in how slice works?

'''
# Answer: The slice works in a very similar way, but in the case of slice on loc,
# the last member we specify is included in the range (unlike slice on iloc).

# exercise 7:
'''
Index the data series series_of_strings and then retrieve from this series with loc, so that the following output is obtained:

Second is
Second a
Second Pandas
dtype: object

'''
# Answer: series_of_strings.index = ['First', 'Second', 'Second', 'Second', 'Fifth']
# series_of_strings.loc["Second"]










