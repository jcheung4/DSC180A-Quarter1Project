#!/usr/bin/env python
# coding: utf-8

# In[6]:

# Modifies the DETR custom training script in order to match our data naming convention
with open('detr/datasets/custom.py', 'r+') as file:
    content = file.read()
    
    modified_content = content.replace("train2017", "training_imgs")
    modified_content = modified_content.replace("val2017", "validation_imgs")
    
    file.seek(0)
    file.write(modified_content)
    file.truncate()
    
    file.close()
