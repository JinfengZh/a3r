#!/usr/bin/env python
# coding: utf-8
# %%
from utilities import traite_train_test
import pandas as pd



# %%
def read(args):
    trainset, testset,n_users,n_attributes,n_attribute_types = read_ratings(args.name)
    return trainset, testset, n_users, n_attributes,n_attribute_types
       


# %%



def read_ratings(name):
    if name == 'book':
        trainset = pd.read_csv(str(name) + '/train.csv')
        testset = pd.read_csv(str(name) + '/test.csv')
        trainset = traite_train_test(trainset)
        testset = traite_train_test(testset)
        hehe_test = trainset.copy()
        df_empty = testset.copy()
        df_empty['user'] = df_empty['user'].astype('int')
        df_empty['rating'] = df_empty['rating'].astype('float')
        df_empty['item'] = df_empty['item'].astype('int')
        hehe_test.index = range(len(hehe_test))
        df_empty.index = range(len(df_empty))
        n_users, n_attributes,n_attribute_types = 5576, 1712, 2
        return hehe_test,df_empty, n_users, n_attributes, n_attribute_types
        
    
    else:
        if name == 'netflix':
            trainset = pd.read_csv(str(name) + '/train.csv')
            testset = pd.read_csv(str(name) + '/test.csv')
            trainset['user_rating'] = (trainset['user_rating'] + 1) * 2 + 1
            testset['user_rating'] = (testset['user_rating'] + 1) * 2 + 1
            trainset = traite_train_test(trainset)
            testset = traite_train_test(testset)
            hehe_test = trainset.copy()
            df_empty = testset.copy()
            df_empty['user_id'] = df_empty['user_id'].astype('int')
            df_empty['user_rating'] = df_empty['user_rating'].astype('float')
            df_empty['movie'] = df_empty['movie'].astype('int')
            hehe_test.index = range(len(hehe_test))
            df_empty.index = range(len(df_empty))
        
        else:
            trainset = pd.read_csv(str(name) + '/train.csv')
            testset = pd.read_csv(str(name) + '/test.csv')
            trainset = traite_train_test(trainset)
            testset = traite_train_test(testset)
            hehe_test = trainset.copy()
            df_empty = testset.copy()
            df_empty['user_id'] = df_empty['user_id'].astype('int')
            df_empty['user_rating'] = df_empty['user_rating'].astype('float')
            df_empty['movie'] = df_empty['movie'].astype('int')
            hehe_test.index = range(len(hehe_test))
            df_empty.index = range(len(df_empty))
        
        if name == 'movielens100k':
            n_users, n_attributes = 943, 4328
        if name == 'mivielendevelop':
            n_users, n_attributes = 610, 22428
        if name == 'netflix':
            n_users, n_attributes = 5128,1154
        n_attribute_types = 3
        return hehe_test,df_empty, n_users, n_attributes, n_attribute_types

