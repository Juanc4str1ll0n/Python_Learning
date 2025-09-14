#Usa el reloj del computador

import datetime 

date = datetime.date(2025, 1, 2)
today = datetime.date.today()  #retorna el dia de hoy

time = datetime.time(12, 30, 2)
nowTime = datetime.datetime.now() #Retorna la hora actual y el dia 

#Esto se hace para editar la presentacion de la hora en String, se puede ver en la documentacion de la libreria 
nowTime = nowTime.strftime("%H:%M:%S %m-%d-%Y")

target_datetime = datetime.datetime(2035, 1, 2, 12, 30, 1)

current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date not passed ")
