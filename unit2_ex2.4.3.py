# 1: Which of the following commands will extract the last five cells from the followers column?

# Answer: All the answers are correct

# 2: What will the following code do?

# [ ] artists.sort_values('name')['name'].iloc[0]

# Answer: The code will return the name of the first artist sorted by name, like:artists['name'].min()

# 3: Write one line of code that performs the two actions we saw in the video: pulls from artists only the five most popular artists.

# Answer: popular_five = artists.sort_values([ 'popularity','followers'],ascending=False).head()

# 4: Write code to arrange the rows of the variable popular_five, which you created in the previous exercise, in the following order: Drake, Justin Bieber, BTS, Bad Bunny, Taylor Swift You must use the sort_values method only (and not loc or iloc!)

# Answer: popular_five.sort.values('genres')

# 5: The following expression retrieves lines 16 and 17:artists.iloc[15:17,:]  head and tail 
# should be concatenated to retrieve the exact same lines.

# Answer: artists.head(17).tail(2)

# 6: artists_by_name = artists[['name','followers']].sort_values('name') 
# artists_by_name.loc[artists_by_name.name < "Mashina",:].tail()
# what this code will do?

# Answer: The code will return the name and number of followers of five artists who come before sleep in alphabetical order

# 7: The Israeli artists we have seen so far have signed up to spotify with their name, spelled in English. However, there are many Israeli artists whose names appear in the table of artists in Hebrew.

# Our goals in this question are:

# Create a DataFrame consisting only of coaches whose names appear in Hebrew letters.
# After we have created it, find among them the artist whose number of followers is the highest.
# In this question you can use one of the properties of comparisons between strings: since a comparison between strings is done in alphabetical order, every name in Hebrew is 'greater than' (ie comes after) the word 'a' (for example the names 'Avner', 'David', 'Yitzchak' and in fact all the names), as well as any name in Hebrew that is 'smaller than' the word 'Tattat' (the word 'T' alone will not be enough, because the name 'Tamir' for example, will appear after 'T' in alphabetical order. That is why several repetitions of the letter 15 ).

# Answer: artists[['name','followers']].loc[(artists['name']>='א') & (artists['name']<='תתתתת'),:].sort_values('followers').iloc[-1,:]

# 8: Perform the retrieval shown in the last line of code without using the '&' sign.

# Answer: artists_indexed_by_popularity.loc[(artists_indexed_by_popularity['popularity']==46)].loc[artists_indexed_by_popularity['followers'] >= 105000].loc[artists_indexed_by_popularity['followers'] < 107000]
