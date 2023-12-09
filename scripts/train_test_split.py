#!/usr/bin/env python
# coding: utf-8

# In[4]:


import json
import shutil
import os

source_directory = 'data/images'
os.makedirs('data/training_imgs', exist_ok=True)
os.makedirs('data/validation_imgs', exist_ok=True)

#For Training
with open('data/annotations/custom_train.json') as file:
    train_data = json.load(file)
    
train_set = set()
for img in train_data['images']:
    train_set.add(img['file_name'])
    
for img_name in train_set:
    source_file = os.path.join(source_directory, img_name)
    destination_file = os.path.join('data/training_imgs', img_name)
    shutil.copy2(source_file, destination_file)
    
#For Validation
with open('data/annotations/custom_val.json') as file:
    val_data = json.load(file)
    
val_set = set()
for img in val_data['images']:
    val_set.add(img['file_name'])
    
for img_name in val_set:
    source_file = os.path.join(source_directory, img_name)
    destination_file = os.path.join('data/validation_imgs', img_name)
    shutil.copy2(source_file, destination_file)

