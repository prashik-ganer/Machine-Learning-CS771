#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import math
X_seen=np.load('X_seen.npy', encoding='bytes', allow_pickle=True)
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


# In[2]:


#Using second method to find mean of unseen classes
#Loading class_attributes_seen dataset
class_attributes_seen=np.load('class_attributes_seen.npy', encoding='bytes', allow_pickle=True)
#Loading class_attributes_unseen dataset
class_attributes_unseen=np.load('class_attributes_unseen.npy', encoding='bytes', allow_pickle=True) 
As=class_attributes_seen
temp1 = np.dot(As.T, As)
iden = np.identity(85)
lambada = [0.01, 0.1, 1, 10, 20, 50, 100]
Xtest=np.load('Xtest.npy', encoding='bytes', allow_pickle=True) 
Ytest=np.load('Ytest.npy', encoding='bytes', allow_pickle=True) 
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

