#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
import os

get_ipython().run_line_magic('matplotlib', 'inline')


# In[15]:


image = cv2.imread('8.jpg')


# In[16]:


image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)


# In[17]:


def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))


# In[18]:


def get_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image


# In[19]:


modified_image = cv2.resize(image, (600, 400), interpolation = cv2.INTER_AREA)
modified_image = modified_image.reshape(modified_image.shape[0]*modified_image.shape[1], 3)


# In[20]:


# n_clusters = number_of_colors
clf = KMeans(n_clusters =  2) 
labels = clf.fit_predict(modified_image)


# In[21]:


counts = Counter(labels)
show_chart = True #
center_colors = clf.cluster_centers_
# We get ordered colors by iterating through the keys
ordered_colors = [center_colors[i] for i in counts.keys()]
hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
rgb_colors = [ordered_colors[i] for i in counts.keys()]
print(hex_colors)
print(center_colors)
if (show_chart):
    plt.figure(figsize = (8, 6))
    plt.pie(counts.values(), labels = hex_colors, colors = hex_colors)  


# In[ ]:





# In[ ]:




