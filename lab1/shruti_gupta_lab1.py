#!/usr/bin/env python
# coding: utf-8

'''1. Write a Python program that prints each item and its corresponding type from the following list. (10 mins) 
Sample List: datalist = [1452, 11.23, 1+2j, True, 'University of Maryland', (0, -1), [5, 12], {"class":'404', "section":'A'}]'''

datalist = [1452, 11.23, 1+2j, True, 'University of Maryland', (0, -1), [5, 12], {"class":'404', "section":'A'}]

for i in datalist:
    print(i, "Type", type(i))



'''2. Create a calculator that can add, subtract, multiply or divide depending upon
the input from the user, using loop and conditional statements. (20 mins)
Sample running output:
Select operation: 1.Add 2.Subtract 3.Multiply 4.Divide
Enter choice (1/2/3/4): 3
Enter first number: 15
Enter second number: 14
15 * 14 = 210
Do you want to do another calculation (y/n)? n (if ‘y’, run your program again)
Bye…
'''

while(True):
    print("Select operation: 1.ADD 2.Subtract 3.Multiply 4.Divide")
    x=int(input("Enter choice (1/2/3/4): "))
    y=int(input("Enter first number: "))
    z=int(input("Enter second number: "))
                
    if(x==1):
        i=y+z
        print(y, " + ", z," = ", i)
     
    elif(x==2):
        i=y-z
        print(y, " - ", z," = ", i)    
     
    elif(x==3):
        i=y*z
        print(y, " * ", z," = ", i) 
          
    else:
        i=y/z
        print(y, " / ", z," = ", i)
        
    cal=input("Do you want to do another calculation (y/n)")
    if (cal=='y'):
        continue
    else:
        print("Bye...")
        break



'''3. Write a Python program to construct the following pattern, using a nested
loop. The longest line (n) is from user input (e.g., n=5 for the following pattern).
(45 mins)
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*'''
x=int(input("Enter a number so see Magic : "))
j=x-1

for i in range(1, x+1):
    print("* " *i)
for j in range(j, 0, -1):   
    print("* " *j)
