import threading
import time

def revisar_correos():
    for i in range(3):
        print("Revisando correos...")
        time.sleep(1)

def descargar_archivo():
    for i in range(3):
        print("Descargando archivo...")
        time.sleep(2)

def escuchar_musica():
    for i in range(3):
        print("Escuchando música...")
        time.sleep(0.1)

hilo1 = threading.Thread(target=revisar_correos)
hilo2 = threading.Thread(target=descargar_archivo)
hilo3 = threading.Thread(target=escuchar_musica)

hilo1.start()
hilo2.start()
hilo3.start()

hilo1.join()
hilo2.join()
hilo3.join()

print("✅ Todas las tareas terminaron.")
