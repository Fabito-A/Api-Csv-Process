#---------------------------------------------------------#
#                procesar archivo csv                     #
# objetivo: leer el archivo csv en el  directorio archivos#
#---------------------------------------------------------#
from shutil import ExecError
import pandas as pd 
import os                           
#---------------------------------------------------------#
# objetivo: procesar el archivo csv                       #
#---------------------------------------------------------#
#obtener directorio relativo
def obtenerRuta(arch=""):
    nom_ruta=os.getcwd()
    ruta=str(os.path.join(nom_ruta,'app','src','archivos',arch))
    return ruta

def insertar_archivo(archivo="datosPrueba.csv",conn=None):
    ruta=obtenerRuta(archivo)
    datos_e=pd.read_csv(ruta,header=0,sep=";")
    datos=datos_e.fillna(0)
    try:
        datos.to_sql(archivo,conn,if_exists='append',index=False)
    except Exception as e:
        print("errro",e)
    

if __name__=="__main__":
    dat="datosPrueba2.csv"