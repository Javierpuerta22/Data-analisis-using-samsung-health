import pandas as pd
import numpy as np
import os
from helper import *

exercise_csv = pd.read_csv('./data/com.samsung.shealth.exercise.20240517143852.csv', sep=',')
#print(exercise_csv.head())

#eliminamos las columnas que tienen NAN ya que nos interesan las que tienen datos que nos referencian los jsons de la actividad física
exercise_csv = exercise_csv.dropna(axis=1)


columns_new = ['id', 'sensing_status', 'total_calorie', 'start_time', 'something', 'end_time', 'update_time', 'max_caloricburn_rate', 'time_offset', 'something2', 'folder', 'mean_time', "location_data"]

exercise_csv.columns = columns_new

exercise_csv.to_csv("./data_resumed/general/exercise.csv", index=False)

