#!/usr/bin/env python
# coding: utf-8

# 1. Write a program that accepts a sentence from the keyboard, calculate and print out each unique character and its corresponding number of occurrence. Don’t count spaces. For example, if the input sentence is: the world is beautiful! , then the output should be the following:
# Hint:
# 1) use index to get a character in a string
# 2) use dictionary to store characters and their corresponding values (# of appearance) a, 1
# ```
# !, 1
# b, 1
# e, 2
# d, 1
# f ,1
# i, 2
# h, 1
# l, 2
# o, 1
# s ,1
# r ,1
# u, 2
# t, 2
# w ,1
# ```

sentence = input()
counts = dict()
sentence=list(sentence.replace(" ", ""))
for letter in sentence:
    counts[letter] = counts.get(letter,0)+1
print(counts)


# 2. Write a program that can sort a given dictionary either by key or value. The program allows users to choose operations (1: sort by key, 2: sort by value). If the given dictionary is: d={'x': 7, 'y': 2, 'a': 3, 'm': 2}, the running output is following.
# ```
# please select operation: (1: sort by key, 2: sort by value) 1 
# a, 3
# m, 2
# x, 7
# y ,2
# please select operation: (1: sort by key, 2: sort by value) 2 
# y ,2
# m, 2
# a, 3
# x, 7
# ```

choice = input("1: sort by key, 2: sort by value  ")
choice = int(choice)
newd = dict()
d={'x': 7, 'y': 2, 'a': 3, 'm': 2} 
d_keys = list(d.keys())
d_values = list(d.values())

if choice == 1:
    d_keys.sort()
    for k in d_keys:
        print(k, d[k])
else:
    d_values.sort()
    x = {}
    for k, v in d.items():
        if v in x:
            x[v] += [k] #adding [k] means adding as a list , x[v] is adding as a key 
        else:
            x[v] = [k]
    print(x)
