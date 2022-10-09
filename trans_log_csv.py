#!/home/gato/anaconda3/bin/python

import re
import pandas as pd
import sys
import subprocess as sp

def extract_pid(path):
    path = path
    reg = r"\[(\d+)\]"
    result = re.search(reg, path)
    if result is None:
        return"nada"
    return(result[1])

def month(path):  
    path = path
    reg = r"([\w+]{3})"
    result = re.search(reg, path)
    if result is None:
        return"nada"
    return(result[1])

def day(path):  
    path = path
    reg = r"([0-9]{2})"
    result = re.search(reg, path)
    if result is None:
        return"nada"
    return(result[1])
  
def time(path):
    path = path
    reg = r"(\d{1,2}:\d{1,2}:\d{1,2})"
    result = re.search(reg, path)
    if result is None:
        return"nada"
    return(result[1])

def name(path):
    path = path
    reg = r"([\w\.]{4,6})"
    result = re.search(reg, path)
    if result is None:
        return"nada"
    return(result[1])

def message(path):
    path = path
    reg = r"]: ([\w\W\.\[\]\:]*)"
    result = re.search(reg, path)
    if result is None:
        return"nada"
    return(result[1])

if __name__ == '__main__':
    
    log_dict = {}
    pid_lis = []
    mes = []
    dia = []
    tiempo = []
    nombre = []
    mensaje = []

    # bash command: cat /var/log/syslog > syslog.log
    
    path = 'syslog.log'
    with open(path) as f:
        for line in f:
            mes.append(month(line))
            dia.append(day(line))
            tiempo.append(time(line))
            pid_lis.append(extract_pid(line))
            nombre.append(name(line))
            mensaje.append(message(line))


    log_dict['pid'] = pid_lis
    log_dict['user'] = nombre
    log_dict['month'] = mes
    log_dict['day'] = dia
    log_dict['time'] = tiempo
    log_dict['message'] = mensaje
    

    df = pd.DataFrame(log_dict)
    df.to_csv('log-out.csv', index=False)
    print(df.info())
    print(df.describe())
    