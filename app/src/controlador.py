#---------------------------------------------------------#
#                coneccion a la base de datos             #
#---------------------------------------------------------#
import sqlite3
import os
import procesar_Csv as Csv


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

def insertarReg(Nom_Arch,db=ruta):
   try:
      print(Nom_Arch)
      conect=sqlite3.connect(db)
      Csv.insertar_archivo(Nom_Arch,conect)
      mensaje="SE PROCESO ARHCIVO {}".format(Nom_Arch)
      conect.commit()
      conect.close()
      return (mensaje)
   except Exception as e:
      mensaje="ocurrio un error = {}".format(e)
      return(mensaje)

def consultar (Nom_arch='datosPrueba.csv',db=ruta):
   try:
      conect=sqlite3.connect(db)
      cursor=conect.cursor()
      comando=f'''SELECT *FROM "MAIN"."{Nom_arch}"'''
      print(comando)
      cursor.execute(comando)
      datos=cursor.fetchall()
      conect.commit()
      conect.close()
      return datos
   except:
      mensaje="OCURRO UN ERROR EN LA CONSULTA"
      return mensaje


def borrar_tabla(Nom_arch='datosPrueba.csv',db=ruta):
   try:
      conect=sqlite3.connect(db)
      cursor=conect.cursor()
      comando=f'''DROP TABLE "MAIN"."{Nom_arch}"'''
      cursor.execute(comando)
      conect.commit()
      conect.close()
      mensaje='SE ELIMINA TABLA {}'.format(Nom_arch)
      return mensaje
   except Exception as e:
      print("error",e)
      return e

def listar_tablas(db=ruta):
   try:
      conect=sqlite3.connect(db)
      cursor=conect.cursor()
      comando='''SELECT NAME FROM SQLITE_SCHEMA'''
      cursor.execute(comando)
      datos=cursor.fetchall()
      conect.commit()
      conect.close()
      return datos
   except Exception as e :
      return e


if __name__=="__main__":
   crea_baseDatos()
