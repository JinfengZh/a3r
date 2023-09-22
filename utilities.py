#!/usr/bin/env python
# coding: utf-8
# %%
import pickle
import pandas as pd
import torch
from torch import nn
from sklearn.preprocessing import LabelEncoder
from concurrent.futures import ProcessPoolExecutor
import numpy as np
from operator import itemgetter
THREADS = 16
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
import time
import torch.nn.functional as F
import json
loss_func = torch.nn.MSELoss()

# %%
from sklearn.preprocessing import LabelEncoder
import torch
loss_func = torch.nn.MSELoss()
from sklearn.metrics import f1_score, roc_auc_score,accuracy_score
from concurrent.futures import ProcessPoolExecutor
THREADS = 16
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"



def RMSE(data, model,name):  ### this function returns RMSE, MAE, precicion, recall, f1 score, accuracy, and the rating before averaging
    if name == 'book':
        users_index = data.iloc[:, 0].values
        users = torch.LongTensor(users_index).to(DEVICE)
        actors_id = data.iloc[:, 2]
        directors_id = data.iloc[:, 3]
        rating = torch.FloatTensor(data.iloc[:, 4].values).to(DEVICE)
        prediction,scores,contribute_actors,contribute_directors,cnm = model(users,actors_id, directors_id,0)
        rmse = loss_func(prediction, rating)
        mae = torch.nn.L1Loss()(prediction, rating)
        p,r,f = binary_predictions(rating, prediction)
        accuracy = arg_accuracy_int(rating,prediction)
        return rmse ** 0.5,mae,p,r,f, accuracy, cnm
        
    else:
        num_example = len(data)
        users_index = data.iloc[:, 0].values
        users = torch.LongTensor(users_index).to(DEVICE)
        actors_id = data.iloc[:, 2]
        directors_id = data.iloc[:, 3]
        genres_id = data.iloc[:, 4]
        rating = torch.FloatTensor(
        data.iloc[:, 5].values).to(DEVICE)
        prediction,scores,contribute_actors,contribute_directors,contribute_genres,cnm = model(users,actors_id, directors_id, genres_id,0)
        prediction = prediction.detach().numpy()
        predictions_bounded = np.maximum(prediction, np.ones(num_example) * 1.0)  # bound the lower values
        predictions_bounded = np.minimum(predictions_bounded, np.ones(num_example) * 5.0)
        prediction = torch.Tensor(predictions_bounded).to(DEVICE)
        rmse = loss_func(prediction, rating)
        mae = torch.nn.L1Loss()(prediction, rating)
        p,r,f = binary_predictions(rating, prediction)
        accuracy = arg_accuracy_int(rating,prediction)
        return rmse ** 0.5,mae,p,r,f, accuracy, cnm


# %%
def arg_accuracy_int(ratings, predictions): ###  This is the implementation in reference 13, it compute the accuracy of prediction
    ratings = ratings.cpu().detach().numpy()
    predictions = predictions.cpu().detach().numpy()
    total_nr = len(ratings)
    total_pred = 0
    for i in range(total_nr):
        (true_rating, pred_rating) = ratings[i], predictions[i]
        if round(pred_rating) >= int(true_rating)-1 and round(pred_rating) <= int(true_rating)+1:
            total_pred += 1

    return float(total_pred)/total_nr


def round_of_rating(number):
    return round(number * 2) / 2


def binary_predictions(true_ratings, predicted_ratings):
    assert len(true_ratings) == len(predicted_ratings)
    binary_true_ratings = []
    binary_predicted_ratings = []

    for i in range(len(true_ratings)):
        if true_ratings[i] >= 3:
            binary_true_ratings.append(1)
        else:
            binary_true_ratings.append(0)

        if predicted_ratings[i] >= 3:
            binary_predicted_ratings.append(1)
        else:
            binary_predicted_ratings.append(0)

    return precision_score(binary_true_ratings, binary_predicted_ratings), recall_score(binary_true_ratings, binary_predicted_ratings), f1_score(binary_true_ratings, binary_predicted_ratings)





# %%
def traite_train_test(df):
    df['actors'] = df['actors'].apply(lambda x: json.loads(x))
    df['director'] = df['director'].apply(lambda x: json.loads(x))
    df['genre'] = df['genre'].apply(lambda x: json.loads(x))
    return df
