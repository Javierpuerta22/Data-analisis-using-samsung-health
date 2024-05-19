import pandas as pd
import numpy as np
import os
from helper import *

exercise_csv = pd.read_csv('./data_resumed/general/exercise.csv', sep=',')




#hacemos el bucle para recopilar los datos de todas las rutas
datos = []
datos_location = []
datos_speed = []
a = 0
for index, row in exercise_csv.iterrows():
    
    route = row["location_data"]
    
    res = extract_data_and_generate_dict(route)
    
    if res["speed"] != None:
        speed_data = res["speed"]
        speed_data["id"] = index
        speed_data["time"] = row["start_time"].split(" ")[1]
        speed_data["date"] = row["start_time"].split(" ")[0]
        datos_speed.append(speed_data)
        
    if res["heart_rate"] != None:
        speed_data = res["heart_rate"]
        speed_data["id"] = index
        speed_data["time"] = row["start_time"].split(" ")[1]
        speed_data["date"] = row["start_time"].split(" ")[0]
        datos.append(speed_data)
    
    if res["location"] != None:
        location_data = res["location"]
        location_data["id"] = index
        location_data["time"] = row["start_time"].split(" ")[1]
        location_data["date"] = row["start_time"].split(" ")[0]
        datos_location.append(location_data)
    
    a += 1
    
    if a % 100 == 0:
        print(a)

#creamos un dataframe con los datos
df = pd.DataFrame(datos)
df = df.fillna(0)
df.to_csv("./data_resumed/personal_data/heart_rate.csv", index=False)

df_location = pd.DataFrame(datos_location)
df_location = df_location.fillna(0)
df_location.to_csv("./data_resumed/personal_data/location.csv", index=False)

df_speed = pd.DataFrame(datos_speed)
df_speed = df_speed.fillna(0)
df_speed.to_csv("./data_resumed/personal_data/speed.csv", index=False)
print("Done!")

