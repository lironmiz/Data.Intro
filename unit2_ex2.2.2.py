# exercise 1 
'''
Looking at the records obtained in the output of artists.tail(), 
what can you say about the band named Right the Starts relative to the band named Cody Longo?

'''
# Answer: Right the Starts has less followers than Cody Longo, yet has a higher popularity score

# exercise 2
'''
Dror and Keren decided to organize a party. Keren is responsible for the playlist and Dror sent her a file called dror_playlist.csv in which is a table of songs he wants to include in the list. Keren printed to the screen the first five lines in the file, and this is how they look:
song_name;artist;for_dancing;duration_seconds
Take On Me;a-ha;no;225
Shape of You; Ed Sheeran; yes; 233
Dance Monkey; Tones and I; yes; 209
Girl Like Me; Shakira; yes; 222
Karen tried to load the file using the command:

[ ] songs = pd.read_csv('dror_playlist.csv')
But when she checked what the DataFrame contained, she found that all the content appeared in one column instead of separate columns:

song_name;artists;for_dancing;duration_seconds
0 Take On Me;a-ha;no;225
1 Shape Of You; Ed Sheeran; yes; 233
2 Dance Monkey; Tones and I; yes; 209
3 Girl Like Me; Shakira; yes; 222

What is the explanation for the result?

'''
# Answer: The file uses a non-comma separator. Kern must specify the separator with the optional sep argument

# exercise 3
'''
In the Python language it is possible to 'chain' expressions. For example, suppose that we want the string "this is a title" to appear in capital letters and that it be centered in a field that is 40 characters long. We know that the first operation can be performed using the upper method, which returns a string, and the second operation using the center method.
We can achieve the cumulative effect of the two actions by 'chaining' the two actions as follows:

[ ] "this is a title".upper().center(40,'*')
************THIS IS A TITLE************
The action that is performed first is upper followed by center - although in this case, we could have performed the actions in the opposite order and reached the same result.
What do you think will be the result of the following thread:

[ ] artists.head().tail()

'''
# Answer: The first five lines in artists will be printed

# exercise 4
'''
What would be the dtype of a column containing the following data:
2, 2.5, 5.6, 7, 1, 3.1, 4

'''
# Answer: float64

