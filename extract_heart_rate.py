import pandas as pd
import numpy as np
import os


exercise_csv = pd.read_csv('./data/com.samsung.shealth.exercise.20240517143852.csv', sep=',')
#print(exercise_csv.head())

#eliminamos las columnas que tienen NAN ya que nos interesan las que tienen datos que nos referencian los jsons de la actividad física
exercise_csv = exercise_csv.dropna(axis=1)
print(exercise_csv.columns)


rutas = exercise_csv['com.samsung.health.exercise.end_time'].values.tolist()
ruta = rutas[100]

def extract_heart_rate(ruta):
    #abrimos el archivo json y guardamos los datos
    print(ruta)
    print(ruta.split(" "))
    ruta = ruta.split(" ")[0]
    ruta += ".com.samsung.health.exercise.live_data.json"
    ruta_pre = "./data/jsons/com.samsung.shealth.exercise"
    
    ruta_final = ruta_pre + "/" + ruta[0] + "/" +  ruta
        
    
    
    with open(ruta_final, 'r') as file:
        data = file.read()

    #print(data)
    #print(type(data))

    #convertimos el string a un diccionario
    data = eval(data)
    print(data)
    
    result = [data2["heart_rate"] for data2 in data]
    
    return result
    
    
res = extract_heart_rate(ruta)

#dibujamos el gráfico
import matplotlib.pyplot as plt

plt.plot(res)
plt.show()

