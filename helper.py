import datetime


def get_time_from_datastamp(datastamp):
    start_time_seconds = datastamp / 1000
    start_time_datetime = datetime.datetime.fromtimestamp(start_time_seconds)

    # Extraer horas, minutos y segundos
    hours = start_time_datetime.hour
    minutes = start_time_datetime.minute
    seconds = start_time_datetime.second
    
    return f"{hours}:{minutes}:{seconds}"


def extract_data_and_generate_dict(ruta: str) -> dict:
    #abrimos el archivo json y guardamos los datos
    ruta = ruta.split(" ")[0]
    ruta_data = ruta + ".com.samsung.health.exercise.live_data.json"
    ruta_location = ruta + ".com.samsung.health.exercise.location_data.json"
    ruta_pre = "./data/jsons/com.samsung.shealth.exercise"
    
    ruta_final = ruta_pre + "/" + ruta_data[0] + "/" +  ruta_data
    
    ruta_location = ruta_pre + "/" + ruta_location[0] + "/" + ruta_location
        
    
    try:
        with open(ruta_final, 'r') as file:
            data = file.read()
            
        with open(ruta_location, 'r') as file:
            location_data = file.read()
            
    except:
        return {"speed": None, "heart_rate": None, "location": None}
    
    #convertimos el string a un diccionario
    data = eval(data)
    location_data = eval(location_data)
    
    all_results = {"speed": None, "heart_rate": None, "location": None}
    
    try:
        if len(data) > 0:
            
            all_results["speed"] = create_dict(data, "speed", 60)
            
            all_results["heart_rate"] = create_dict(data, "heart_rate", 60)
            
        if len(location_data) > 0:
            all_results["location"] = create_multi_dict(location_data, 60)  

        return all_results
    
    except:
        return {"speed": None, "heart_rate": None, "location": None}
    
    
def create_dict(data: list, variable:str, limit:int = 60):
    cantidad = 0
    new_dict = {}
    
    for minidict in data:
        if cantidad >= limit:
            break
        
        if minidict.get(variable) == None:
            continue
        else:
            new_dict[cantidad] = minidict[variable]
            cantidad += 1
            
    return new_dict

def create_multi_dict(data: list, limit:int = 60):
    cantidad = 0
    new_dict = {}
    
    for minidict in data:
        if cantidad >= limit:
            break
        
        if minidict.get("latitude") == None:
            continue
        else:
            new_dict[cantidad] = str(minidict["latitude"]) + ";" + str(minidict["longitude"])
            cantidad += 1
            
    return new_dict
            
    
    

