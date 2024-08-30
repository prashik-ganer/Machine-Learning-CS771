#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
X_seen=np.load('X_seen.npy', encoding='bytes', allow_pickle=True) 


# In[2]:


#Finding the means of seen class
class_means = []
for i in range(0,40):
    class_sample = X_seen[i]
    x=np.shape(class_sample)[0]
    m=[]
    for j in range(0,4096):
        sum=0
        for k in range(0,x):
            sum+=class_sample[k][j]
        mean=sum/x
        m.append(mean)
    class_means.append(m)
print(np.shape(class_means))


# In[3]:


#Loading class_attributes_seen dataset
class_attributes_seen=np.load('class_attributes_seen.npy', encoding='bytes', allow_pickle=True) 


# In[4]:


#Loading class_attributes_unseen dataset
class_attributes_unseen=np.load('class_attributes_unseen.npy', encoding='bytes', allow_pickle=True) 


# In[5]:


#Finding the similarity vector for unseen and seen class attributes.
sim_class=[]
for i in range(0,10):
    similarity=[]
    for j in range(0,40):
        dot_product = np.dot(class_attributes_unseen[i], class_attributes_seen[j])
        similarity.append(dot_product)
    sim_class.append(similarity)
print(np.shape(sim_class))
# print(sim_class)


# In[6]:


#Normalizing the similarity vector
weights=[]
for i in range(0,10):
    sum=0
    for j in range (0,40):
        sum=sum+sim_class[i][j]
    for j in range (0,40):
        sim_class[i][j]/=sum
print(np.shape(sim_class))
# print(sim_class)


# In[7]:


#For each of 10 unseen classes, finding the mean vector
mean_unseen=[]
for i in range(0,10):
    sum=[]
    for j in range(0,40):
        temp=[]
        for l in range (0,4096):
            temp.append(sim_class[i][j]*class_means[j][l])
        sum.append(temp)
    for k in range(1,40):
        for i in range(len(sum[0])):
            sum[0][i]+=sum[k][i]
    mean_unseen.append(sum[0])
print(np.shape(mean_unseen))
# print(mean_unseen)


# In[8]:


#Creating a prototype based classsification model and finding its accuracy
import math
Xtest=np.load('Xtest.npy', encoding='bytes', allow_pickle=True) 
Ytest=np.load('Ytest.npy', encoding='bytes', allow_pickle=True) 
y_pred = []
for x in Xtest:
    distances = np.linalg.norm(mean_unseen-x, axis=1)
    predicted_class = np.argmin(distances)
    y_pred.append(predicted_class+1)
    np.array(y_pred)
c=0
for i in range(len(y_pred)):
    if(y_pred[i]==Ytest[i]):
        c=c+1
accuracy = c/len(y_pred)
print(accuracy)


# In[9]:


#Using second method to find mean of unseen classes
As=class_attributes_seen
temp1 = np.dot(As.T, As)
iden = np.identity(85)
lambada = [0.01, 0.1, 1, 10, 20, 50, 100]
#Running loop over all the lambada values
for l in (lambada):
    temp2 = temp1 + l * iden
    inverse = np.linalg.inv(temp2)
    Ms=class_means
    W = np.dot(np.dot(inverse, As.T), Ms)
     #print(np.shape(W))
     #print(W)
    ac = class_attributes_unseen
    mean_unseen_2 = np.dot(ac, W)
    # print(np.shape(mean_unseen_2))
    
    #Performing prediction using unseen class means
    y_pred = []
    for x in Xtest:
        distances = np.linalg.norm(mean_unseen_2-x, axis=1)
        predicted_class = np.argmin(distances)
        y_pred.append(predicted_class+1)
        np.array(y_pred)
#     print(y_pred)
#Finding accuracy
    c=0
    for i in range(len(y_pred)):
        if(y_pred[i]==Ytest[i]):
            c=c+1
#     print(c)
    accuracy = c/len(y_pred)
    print(accuracy)


# In[ ]:





# In[ ]:





# In[ ]:




