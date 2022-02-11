import os
import shutil 
import datetime


carpeta_objetivo="D:\\programacion\\test_carpetas\\testeo" + "\\"
carpeta_madre="D:\\programacion\\test_carpetas" + "\\"

for ruta,directorio,archivos in os.walk(carpeta_madre):
    
    if archivos:
        for archivo in archivos:
            if not os.path.isfile(carpeta_objetivo+archivo):
                os.rename(ruta+"\\"+archivo,carpeta_objetivo+archivo)

def mover_archivos(carpeta_madre,carpeta_objetivo):
    try:
        for ruta,directorio,archivos in os.walk(carpeta_madre):
            if archivos:
                for archivo in archivos:
                    if not os.path.isfile(carpeta_objetivo+archivo):
                        os.rename(ruta+"\\"+archivo,carpeta_objetivo+archivo)
        print("Sin miedo al exito")
    except Exception as e:
        print(e)

mover_archivos(carpeta_madre,carpeta_objetivo)