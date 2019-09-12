
#Lab 1

Note: If you want to use print statement to output without newline, please add the
following statement at the beginning for python 2.X. No necessary to add this for
python 3.X.
from __future__ import print_function
Then whenever you use “print”, you use: print(‘something’, end=‘’)


1. Write a Python program that prints each item and its corresponding type from
the following list. (10 mins)
Sample List: datalist = [1452, 11.23, 1+2j, True, 'University of Maryland', (0, -1),[5, 12], {"class":'404', "section":'A'}]

```
datalist =  [1452, 11.23, 1+2j, True, 'University of Maryland', (0, -1),[5, 12], {"class":'404', "section":'A'}]
for data in datalist:
    print("Data: " +str(data) +" Type: " +str(type(data)))
```

2. Create a calculator that can add, subtract, multiply or divide depending upon
the input from the user, using loop and conditional statements. (20 mins)
Sample running output:
Select operation: 1.Add 2.Subtract 3.Multiply 4.Divide
Enter choice (1/2/3/4): 3
Enter first number: 15
Enter second number: 14
15 * 14 = 210
Do you want to do another calculation (y/n)? n (if ‘y’, run your program again)
Bye…

```
while(True):
    print("Select Operations: 1.Add 2.Subtract 3.Multiply 4.Divide")
    line1 = input("Enter choice (1/2/3/4): ")
    num1  = input("Enter 1st Number ")
    num2  = input("Enter 2nd Number ")

    print("Selected Operation is: "+str(line1))
    if int(line1)==1:
        print("Calculator Result is : " + str(int(num1)+int(num2)))
    elif int(line1)==2:
        print("Calculator Result is : " + str(int(num1)-int(num2)))
    elif int(line1)==3:
        print("Calculator Result is : " + str(int(num1)*int(num2)))
    elif int(line1)==4:
        print("Calculator Result is : " + str(int(num1)/int(num2)))
    else:
        print("Invalid Inputs, please Enter another Calculation")

    line2 = input("Do you want to do another calculation (y/n)? ")
    print("Selected Choice is: "+ str(line2))
    print()
    if line2=='n':
        break
print("Bye...")
```

3. Write a Python program to construct the following pattern, using a nested
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
*

```
num = input("Enter n: ")
i=0
while(i<int(num)):
    print("*" *i)
    i=i+1
j= i+1
while(j>0):
    print("*" *j)
    j=j-1
```
