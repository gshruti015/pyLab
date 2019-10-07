#!/usr/bin/env python
# coding: utf-8

# Exercise 1.
# ```
# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT, and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 7
# DOWN 5 LEFT 2 RIGHT 9 X
# The numbers after the direction are steps. Please write a Python program to compute the distance from the 
# current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following movements obtained from the user input are given to the program: 
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# X
# Then the output of the program should be: 2
# Note: X means the end of movement.
# ```

# In[ ]:


movement_dict={}
movement = []
while (True):
    l = input("Enter steps intereatevley, enter 'X'to stop ")
    movement.append(l)
    if l == 'X':
        break
movement= movement[:-1] # remove the 'X'

for i in range(len(movement)):
    val = movement[i].split(' ')  # this splits the UP 2 into two values UP and 2, and stores them in a list called val
    movement_dict[val[0]] = val[1] # this uses the indexes in val to assign key and value to the dictionory
    
origin = [0,0]
for k,v in movement_dict.items():
    if(k=='UP'):
        origin[1] = origin[1] + int(v) 
    if(k=='DOWN'):
        origin[1] = origin[1] - int(v) 
    if(k=='LEFT'):
        origin[0] = origin[0] - int(v)
    if(k=='RIGHT'):
        origin[0] = origin[0] + int(v)
dist = int((origin[0]**2 + origin[1]**2)**1/2) # computing euclidean
print(int(round(dist))) # rounding and printing to nearest integer


# Exercise 2.
# ```
# Write a Python program to compute the frequency of words from the article. The output should output after sorting the key alphanumerically. Suppose the article is obtained from the user. The input ends until the user sends a new line: X
# Example:
# Please provide the article:
# Beginner means someone who has just gone through an introductory Python course.
# He can solve some problems with 1 or 2 Python classes or functions.
# Normally, the answers could directly be found in the textbooks.
# Intermediate means someone who has just learned Python, but already has a relatively strong programming background from before.
# X
# Output: 
# 1: 1
# 2: 1 
# an: 1
# . . .
# ```

# In[ ]:


print("Please provide the article:")
article = []
while (True):
    l = input("Enter lines intereatevley, enter 'X' to stop ") 
    l = l.lower()
    val = l.split(" ")    
    article.append(val)
    if l.upper().lower() == 'x':
        break
        
article_new = [j.replace(".", "") for i in article for j in i] #list comprehsnion for nested loop, also replaces full stop
article_new = article_new[:-1]
unique_item = {}

for item in article_new:
    unique_item[item]= unique_item.get(item,0)+1

d_keys = list(unique_item.keys())
d_keys.sort()
for k in d_keys:
    print(k, unique_item[k])

