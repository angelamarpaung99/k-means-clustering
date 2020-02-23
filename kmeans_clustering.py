# -*- coding: utf-8 -*-
"""KMeans-Clustering.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pwdm5H4-ie9XxVQfQ9YHgR9-2O87QHXh
"""

import pandas as pd # learn more: https://python.org/pypi/pandas
import numpy as np
import math
import random as r
import copy

df = pd.read_csv('https://raw.githubusercontent.com/machine-learning-course/syllabus/gh-pages/hiw-2019b/dataset-students-ml-2019b.csv')
df['nim'] = df['nim'].astype(str)

# TODO: Your k-means algorithm here
# Count euclidean distance
def euclidean_distance(x,center):
  return math.sqrt(sum([(a-b) **2 for a,b in zip(x, center)]))

#Encode Categorical Variable
dow_of_birth_encode = {"dow_of_birth": {"Monday": 1, "Tuesday": 2, "Wednesday" : 3, "Thursday" : 4, "Friday" : 5, "Saturday" : 6, "Sunday" : 7}}
df.replace(dow_of_birth_encode, inplace=True)
df.head()

X = df.iloc[:,[4,8,9]].values

#Initialize first centroid based on data
K = 4
curr_centroid = []
for i in range(K):
  idx = r.randint(0,65)
  curr_centroid.append([X[idx][0], X[idx][1], X[idx][2]])

#Applying k-means to the dataset
prev_centroid = [None]
while (curr_centroid != prev_centroid):
  sum_c0_x, sum_c0_y, sum_c0_z, sum_c1_x, sum_c1_y, sum_c1_z, sum_c2_x, sum_c2_y, sum_c2_z, sum_c3_x, sum_c3_y, sum_c3_z,i_c0,i_c1,i_c2,i_c3 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
  cluster = [0 for x in range(K)]
  c_result = [0 for x in range(len(X))]
  temp = copy.deepcopy(prev_centroid)
  for i in range(len(X)):   
    cluster[0] = euclidean_distance(X[i], curr_centroid[0])
    cluster[1] = euclidean_distance(X[i], curr_centroid[1])
    cluster[2] = euclidean_distance(X[i], curr_centroid[2])
    cluster[3] = euclidean_distance(X[i], curr_centroid[3])
    c_result[i] = cluster.index(min(cluster))
    if (c_result[i] == 0):
      i_c0 += 1
      sum_c0_x += X[i][0]
      sum_c0_y += X[i][1]
      sum_c0_z += X[i][2]
    elif (c_result[i] == 1):
      i_c1 += 1
      sum_c1_x += X[i][0]
      sum_c1_y += X[i][1]
      sum_c1_z += X[i][2]
    elif (c_result[i] == 2):
      i_c2 += 1
      sum_c2_x += X[i][0]
      sum_c2_y += X[i][1]
      sum_c2_z += X[i][2]
    elif (c_result[i] == 3):  
      i_c3 += 1
      sum_c3_x += X[i][0]
      sum_c3_y += X[i][1]
      sum_c3_z += X[i][2]
  prev_centroid = copy.deepcopy(curr_centroid)
  if (i_c0 != 0):
    curr_centroid[0] = [(sum_c0_x/i_c0), (sum_c0_y/i_c0), (sum_c0_z/i_c0)]
  if (i_c1 != 0):
    curr_centroid[1] = [(sum_c1_x/i_c1), (sum_c1_y/i_c1), (sum_c1_z/i_c1)]
  if (i_c2 != 0):
    curr_centroid[2] = [(sum_c2_x/i_c2), (sum_c2_y/i_c2), (sum_c2_z/i_c2)]
  if (i_c3 != 0):
    curr_centroid[3] = [(sum_c3_x/i_c3), (sum_c3_y/i_c3), (sum_c3_z/i_c3)]

c_result = [v +1 for v in c_result]

dist = []
for i in range(len(X)):
  if (c_result[i] == 1):
    dist.append(euclidean_distance(X[i], curr_centroid[0]))
  elif (c_result[i] == 2):
   dist.append(euclidean_distance(X[i], curr_centroid[1]))
  elif (c_result[i] == 3):
   dist.append(euclidean_distance(X[i], curr_centroid[2]))
  else:
   dist.append(euclidean_distance(X[i], curr_centroid[3]))
   
print()
print('Model Code: E')
for i in range(len(X)): 
  print('%s,%s,%0.4f' % (df.loc[i,'nim'], c_result[i], dist[i]))

