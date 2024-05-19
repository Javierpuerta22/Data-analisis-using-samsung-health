import pandas as pd
import numpy as np
import os
from helper import *

exercise_csv = pd.read_csv('./data/com.samsung.shealth.exercise.20240517143852.csv', sep=',')
#print(exercise_csv.head())

#eliminamos las columnas que tienen NAN ya que nos interesan las que tienen datos que nos referencian los jsons de la actividad física
exercise_csv = exercise_csv.dropna(axis=1)
print(exercise_csv.columns)


rutas = exercise_csv['com.samsung.health.exercise.end_time'].values.tolist()
ruta = rutas[100]

def extract_heart_rate(ruta):
    #abrimos el archivo json y guardamos los datos
    ruta = ruta.split(" ")[0]
    ruta += ".com.samsung.health.exercise.live_data.json"
    ruta_pre = "./data/jsons/com.samsung.shealth.exercise"
    
    ruta_final = ruta_pre + "/" + ruta[0] + "/" +  ruta
        
    
    try:
        with open(ruta_final, 'r') as file:
            data = file.read()
            
    except:
        return None

    #print(data)
    #print(type(data))

    #convertimos el string a un diccionario
    data = eval(data)
    #print(data)
    
    if len(data) > 0 and data[0].get("heart_rate", None) == None:
        return None
    
    elif len(data) == 0:
        return None
    try:
        result = {index: data2["heart_rate"] for index,data2 in enumerate(data) if index <= 60}
        
        
    except:
        return None
            
    return result


#hacemos el bucle para recopilar los datos de todas las rutas
datos = []
a = 0
for route in rutas:
    res = extract_heart_rate(route)
    
    if res == None:
        continue
    
    datos.append(res)
    a += 1
    
    if a % 100 == 0:
        print(a)

#creamos un dataframe con los datos
df = pd.DataFrame(datos)
df = df.fillna(0)
df = df.astype(float)
df.to_csv("heart_rate.csv", index=False)

    
"""res = extract_heart_rate(ruta)

#dibujamos el gráfico
import matplotlib.pyplot as plt

plt.plot(res)
plt.show()"""

