#!/usr/bin/env python
# coding: utf-8

# In[106]:


import mysql.connector
con = mysql.connector.connect(host='localhost',user='root',password='rootuser',database='course')
cur = con.cursor()


# In[107]:


query = 'CREATE TABLE course.doctors (docID INT(11) PRIMARY KEY, name VARCHAR(50) DEFAULT NULL, speciality  VARCHAR(50) DEFAULT NULL, numReviews INT(11) DEFAULT NULl, city tinytext DEFAULT NULL, state varchar(2) DEFAULT NULL)'
cur.execute(query)


# In[108]:


filename = 'doctors.txt'
try:
    file = open('doctors.txt','r',encoding='utf-8',errors='ignore')
    fileread = file.readlines()
except UnicodeEncodeError: 
    pass

final=[]

for i in range(len(fileread)):
    final.append(fileread[i].rstrip('\n').split(','))
    
for i in range(len(final)):
    final[i][0] = int(final[i][0])
    final[i][3] = int(final[i][3])

datapush = [tuple(i) for i in final]

print(final[:10])
print(datapush[:10])


# In[110]:


for data in datapush:
    insert = "insert into doctors(docID, name, speciality, numReviews, city, state) values" + str(data)
    cur.execute(insert)  
con.commit()


# In[152]:


def fun1():
        q1 = "select count(*) from doctors where state = 'MD'"
        cur.execute(q1)
        res = cur.fetchone()
        print("Number of Doctors in MD: ",res[0])

        q2 = "select avg(numReviews) from doctors where state ='MD'"
        cur.execute(q2)
        res = cur.fetchone()
        print("Avg Reviews for Doctors in MD: ",res[0])

fun1()


# In[168]:


def fun2():
        q = "select name, speciality from doctors where state = 'MD' order by numReviews desc limit 10"
        cur.execute(q)
        res = cur.fetchall()
        for item in v:
            i1 = list(item)
            print(i1[0].ljust(30),i1[1])

fun2()


# In[153]:


def fun3():
        q1 = "update doctors set state = 'U' where state = '-'"
        cur.execute(q1)
        con.commit()
        q2 = "update doctors set city = 'U' where city = '-'"
        cur.execute(q2)
        con.commit()

fun3()

