#!/usr/bin/env python
# coding: utf-8

# 1. Given customer bank saving data customer-savings.txt, please answer the following questions using Python programming.
#   1. What’s the average balance for male and female?
#   2. What’s the average balance for while collar and bluecollar in England?
#   
#   
# ```
# Data columns in customer-savings.txt (separated by comma):
# Customer ID, Customer Name, Customer Surname, Gender, Age, Region, Job Classification, Date joined, Balance 
# 
# 100000001,Simon,Walsh,Male,21,England,White Collar,05.Jan.15,113810.15 
# 100000003,Liam,Brown,Male,46,England,White Collar,07.Jan.15,101536.83
# ```

# In[ ]:


file = open('customer-savings.txt','r')
fileread = file.readlines()
men = 0
women = 0
wcollar = 0
bcollar = 0
final=[]

for i in range(len(fileread)):
    final.append(fileread[i].rstrip('\n').split(','))

for val in final:
    if val[3] =="Male":
        men+= float(val[-1])
    if val[3] =="Female":
        women+= float(val[-1])
    if val[-4] == 'England':
        if val[-3] =="White Collar":
            wcollar+=float(val[-1])
        if val[-3] =="Blue Collar":
            bcollar+= float(val[-1])

menavg = round(men/len(fileread),2)
womenavg = round(women/len(fileread),2)
wcollaravg = round(wcollar/len(fileread),2)
bcollaravg = round(bcollar/len(fileread),2)

print("Average balance for male: " +str(menavg)+'\n'+"average balance for female: " + str(womenavg)+'\n'
      + "average balance for white collar: " + str(wcollaravg)+'\n'+ "average balance for blue collar: " + str(bcollaravg)+'\n')


# 2. Combine multiple files
# 
# ```
# Use Python programming to combine two text files: customer-status.txt and sales.txt
# 
# Data columns in customer-status.txt (separated by comma):
# Account Number, Name, Status 
# 527099,Sanford and Sons,bronze
# 
# Data columns in sales.txt (separated by comma):
# Account Name, Name, SKU, Quantity, Unit Price, Ext Price, Date
# 163416,Purdy-Kunde,S1-30248,19,65.03,1235.57,2014-03-01 16:07:40 527099,Sanford and Sons,S2-  82423,3,76.21,228.63,2014-03-01 17:18:01
# 
# After you combine, you will see the following:
# 527099,Sanford and Sons,S2-82423,3,76.21,228.63,2014-03-01 17:18:01,bronze
# ```

# In[ ]:


file1 = open('customer-status.csv','r')
file2 = open('sales.csv','r')
file11 = file1.readlines()
file21 = file2.readlines()

file1f = []
file2f = []


for line in range(len(file11)):
    file1f.append(file11[line].rstrip('\n').split(','))

for line in range(len(file21)):
    file2f.append(file21[line].rstrip('\n').split(','))
    
# uncomment based on type of ouput required:

# Module 1
# # this is for complete records
# for i in range(len(file2f)):
#     for j in range(len(file1f)):
#         if file2f[i][0] == file1f[j][0]:
#             file2f[i].append(file1f[j][-1])

# for line in range(len(file2f)):
#     print(file2f[line])
# print(len(file2f)) #equal to length of initial file


# Module 2
# # this is for only relevant records
# finalff=[]   
# val=[]
# for i in range(len(file2f)):
#     for j in range(len(file1f)):
#         if file2f[i][0] == file1f[j][0]:
#             val= file2f[i]
#             val.append(file1f[j][-1])            
#             finalff.append(val)
            
# for line in range(len(finalff)):
#     print(finalff[line])
# print(len(finalff)) #equal to length of common records

