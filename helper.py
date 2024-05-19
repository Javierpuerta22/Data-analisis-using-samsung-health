import datetime


def get_time_from_datastamp(datastamp):
    start_time_seconds = datastamp / 1000
    start_time_datetime = datetime.datetime.fromtimestamp(start_time_seconds)

    # Extraer horas, minutos y segundos
    hours = start_time_datetime.hour
    minutes = start_time_datetime.minute
    seconds = start_time_datetime.second
    
    return f"{hours}:{minutes}:{seconds}"