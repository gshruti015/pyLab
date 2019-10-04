#!/usr/bin/env python
# coding: utf-8

# Design an interactive product management system using Python fuctions.
# ```
# 1) display system functions
# function name: show_functions Parameters:
# None Return:
# The user choice Description:
# This function prints out all possible functionalities of the system to let users choose. The output should look like the following:
# *********************************************
# * 1. Generate overall stats for all products (total #, avg #, min, and max) * 2. Calculate the amount for a given product
# * 3. Update the amount for a given product *********************************************
# 2) Generate overall stats for all products
# function name: gen_stats Parameters:
# None Return:
# None Description:
# Generate all basic stats of all products, such as the total amount for all products, the average, the maximum and the minimum.
# 3) calculate the amount of a given product
# function name: check_stock() Parameters:
# Product name Return:
# The number in stock for that product Description
# Retrieve the corresponding number in stock for a given product. The given product is obtained from the user (raw_input).
# 4) update the amount for a give product
# function name: update_stock() Parameters:
# The stock dictionary, a given product, the number (positive means increase, negative means decrease)
# Return:
# None
# Description:
# Update the number in stock for a given product. The stock dictionary also needs to be
# updated.
# Note: 1. the system is always running until the user stops it. (You can use infinite loop with break statement somewhere in the loop)
#     
# 2. You can design a main function which will be the starting point when you execute the entire program. Please use the following codes. Main function is also a function like others.
# def main():
# place your codes here
# if __name__ == ‘__main__’: main()
# ```

def show_functions():
    delimiter = '*********************************************\n'
    opt1 = '* 1.Generate overall stats for all products (total #, avg #, min, and max)\n'
    opt2 = '* 2. Calculate the amount for a given product\n'
    opt3 = '* 3. Update the amount for a given product\n'
    print(delimiter+opt1+opt2+opt3+delimiter)
    choice = input("Enter the operation choice you want to perform ")
    return choice

def gen_stats(product_stock):
    list_total = [product_stock[i] for i in product_stock]
    length = sum(list_total)/len(product_stock)
    maxp = max(list_total)
    minp = min(list_total)
    return sum(list_total), length, maxp, minp


def check_stock(product_stock):
    pname = input("Enter product name ")
    val = product_stock.get(pname)
    return val


def update_stock(product_stock):
    pname = input("Enter product name")
    pvalue = input("Enter product increase/decrease value")
    product_stock[pname]+=int(pvalue)             
    return(product_stock)

def main():

    product_stock = {"computer":35, "chair": 100, "desk": 20, "iphone": 15}
    print("The current stock", product_stock)
    
    while(True):         
        choice = show_functions()    
        if choice == '1':
            total, avg, minimum, maximum = gen_stats(product_stock)
            print("total:",total,"\naverage:",avg,"\nminimum:",minimum,"\nmaximum:",maximum)
        elif choice == '2':
            val = check_stock(product_stock)
            print("Current Stock value for entererd product is", val)
        elif choice == '3':
            updated_stock = update_stock(product_stock)
        else:
            print("wrong operations...")
        
        option = input("\nDo you want to perform another operation [Enter(y/n)] :")
        
        if option == 'n':
            break
        
    print('Bye!')
if __name__ == '__main__':
    main()
