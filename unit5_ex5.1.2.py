# exercise 5.1.2 from unit 5
'''
Two data tables are given:

The owners table contains the names of four members and the types of animals they own:
Owner pet_type
0 Adam cat
1 Betty cat
2 Betty dog
3 Jackie dog
4 Fred iguana
In the table you can see that Adam has a cat, Betty has a cat and a dog,
Jackie has a dog, and Fred has an iguana.
The activities table contains a description of possible activities for each animal:
pet_type Activity
0 cat feed
1 cat cuddle
2 dog play with stick
3 dog walk
In the table you can see that a cat can be fed or cuddled, and that with a dog you can 
play with a stick or go for a walk.
Now execute the following line of code:
owners_and_activities = pd.merge(owners, activities, on='pet_type')

For each of the following lines:
Choose "true" if the row will appear in the owners_and_activities table after merging,
or "false" if the row will not appear.
'''
# 1:
'''
Owner	 pet_type	  Activity
Adam	   dog      play with 
                 stick
'''

# Answer: wrong 

# 2:
'''
Owner	pet_type	Activity
Betty	cat	      cuddle
'''

# Answer: right

# 3:
'''
Owner	pet_type	Activity
Fred	iguana	   feed
'''

# Answer: wrong
