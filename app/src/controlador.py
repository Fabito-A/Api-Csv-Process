#---------------------------------------------------------#
#                coneccion a la base de datos             #
#---------------------------------------------------------#
import json
import sqlite3
import os
import procesar_Csv as Csv
from flask import Flask,jsonify

#obtener directorio relativo para acceder a la base de datos 
controlador = Flask(__name__)
nombre_bd='basedatos_001.sqlite3'
nom_ruta=os.getcwd()
ruta=str(os.path.join(nom_ruta,'app','database',nombre_bd))
#variables
columnas =[]

@controlador.route('/creaDb')
def crea_baseDatos(db=ruta):
   try:
      conect=sqlite3.connect(db)
      conect.commit()
      conect.close()
   except Exception as Error:
      print(Error)
#funcion que realiza la insersion de un archivo csv sin conocer su longitud
@controlador.route('/insertarCsv/<string:Nom_Arch>')
def insertarReg(Nom_Arch,db=ruta):
   try:
      print(Nom_Arch)
      Nom_Arch='datosPrueba.csv'
      conect=sqlite3.connect(db)
      Csv.insertar_archivo(Nom_Arch,conect)
      return ("recibido")
   except Exception as Error:
      print(Error)
      return("ocurrio un error")

@controlador.route('/consultar')
def consultar (Nom_arch='datosPrueba.csv',db=ruta):
   conect=sqlite3.connect(db)
   cursor=conect.cursor()
   comando=f'''SELECT *FROM "MAIN"."{Nom_arch}"'''
   print(comando)
   cursor.execute(comando)
   datos=cursor.fetchall()
   conect.commit()
   conect.close()
   return json.dumps(datos)

@controlador.route('/borrarTb<string:Nom_Arch>')
def borrar_tabla(Nom_arch='datosPrueba.csv',db=ruta):
   conect=sqlite3.connect(db)
   cursor=conect.cursor()
   comando=f'''DROP TABLE "MAIN"."{Nom_arch}"'''
   cursor.execute(comando)
   datos=cursor.fetchall()
   conect.commit()
   conect.close()
   return("Se elimino la tabla ",Nom_arch)

if __name__ =="__main__":
   controlador.run(debug=True, port=5000)

