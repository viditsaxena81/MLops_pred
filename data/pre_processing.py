#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import numpy as np
import pandas as pd
import shutil


# In[2]:


# get absolute path of csv files from data folder
def get_absPath(filename):
    """Returns the path of the notebooks folder"""
    path = os.path.abspath(
        os.path.join(
            os.path.dirname(
                __file__), os.path.pardir, "data", filename
        )
    )
    return path


# In[3]:

def test_check_schema():
    datafile = get_absPath("healthinsurance.csv")
    # check that file exists
    assert os.path.exists(datafile)
    dataset = pd.read_csv(datafile)
    header = dataset[dataset.columns[:-1]]
    actual_columns = header.shape[1]
    # check header has expected number of columns
    assert actual_columns == expected_columns
# In[4]:

def preprocessing():
    datafile = get_absPath("healthinsurance.csv")
    dataset = pd.read_csv(datafile)
    dataset['age']=dataset['age'].fillna(value=dataset['age'].median())
    dataset['bmi']=dataset['bmi'].fillna(value=dataset['bmi'].median())
    dataset['bloodpressure']=dataset['bloodpressure'].replace(to_replace=0,value=dataset['bloodpressure'].median())
    dataset=dataset.drop(['city','job_title'],axis=1)
    dataset['hereditary_diseases']=dataset['hereditary_diseases'].replace(to_replace=['Alzheimer','Arthritis','Cancer','Diabetes','Epilepsy','EyeDisease','HeartDisease','High BP','Obesity'],value='Disease')
    dataset=pd.get_dummies(dataset, drop_first=True)
    dataset.to_csv('pre_processed.csv',index=False)
    # Save the dataset to the data folder
    os.makedirs('data', exist_ok=True)
    shutil.copy('pre_processed.csv',os.path.join('data', 'pre_processed.csv'))

    

