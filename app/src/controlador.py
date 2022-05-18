#---------------------------------------------------------#
#                coneccion a la base de datos             #
#---------------------------------------------------------#
from crypt import methods
import sqlite3
import os
import procesar_Csv as Csv
from flask import Flask,jsonify

#obtener directorio relativo para acceder a la base de datos 
nombre_bd='basedatos_001.sqlite3'
nom_ruta=os.getcwd()
ruta=str(os.path.join(nom_ruta,'app','database',nombre_bd))
#variables
columnas =[]

def crea_baseDatos(db=ruta):
   try:
      conect=sqlite3.connect(db)
      conect.commit()
      conect.close()
   except Exception as Error:
      print(Error)
#funcion que realiza la insersion de un archivo csv sin conocer su longitud

def insertarReg(Nom_Arch="",db=ruta):
   try:
      Nom_Arch='datosPrueba.csv'
      conect=sqlite3.connect(db)
      Csv.insertar_archivo(Nom_Arch,conect)

   except Exception as Error:
       print(Error)


def consultar (Nom_arch='datosPrueba.csv',db=ruta):
   conect=sqlite3.connect(db)
   cursor=conect.cursor()
   comando=f'''SELECT *FROM "MAIN"."{Nom_arch}"'''
   print(comando)
   cursor.execute(comando)
   datos=cursor.fetchall()
   conect.commit()
   conect.close()

def borrar_tabla(Nom_arch='datosPrueba.csv',db=ruta):
   conect=sqlite3.connect(db)
   cursor=conect.cursor()
   comando=f'''DROP TABLE "MAIN"."{Nom_arch}"'''
   cursor.execute(comando)
   datos=cursor.fetchall()
   conect.commit()
   conect.close()

if __name__ =="__main__":
   crea_baseDatos()
   insertarReg()
   consultar()

