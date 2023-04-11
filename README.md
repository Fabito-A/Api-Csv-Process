# Api Csv Process
Se realiza la creacion del la logica encargada de procesar el archivo csv y comunicarse con la base de datos
Por el momento esta dividido en 2 archivos python controlador.py y procesar_Csv
para controlador.py se implemento el servidor flask que atendera las peticiones externas tales como: 
crear una base de datos si no existe en el directorio Proyecto_web/app/database,
insertar datos a partir de un archivo csv(dentro de la carpeta Proyecto_web/app/src/archivos se encuentra un csv de ejemplo)
eliminar la tabla de la base de datos
insertar los datos del archivo en la base de datos que se podra consultar mediante un objeto json 

para procesar_Csv.py es un modulo encargado de leer el archivo csv mediante la libreria pandas y que a su vez 
se encargara de realizar la insercion de data con el comando sql propio de la libreria eso incluye la tabla bajo el 
nombre del archivo fuente 

por el momento para el despliegue del servidor se debe ejecutar el archivo controlador.py 
acceder al navegador web http://127.0.0.1:5000 

http://127.0.0.1:5000/consultar <-  consulta el contenido de la base de datos con un formato json
http://127.0.0.1:5000/borrarTb/"nombre base datos" <-borra el contenido de la base de datos
http://127.0.0.1:5000/insertarCsv/"nombre archivo" <-inserta los registros bajo el nombre del archivo que debe estar por el momento ubicado en Proyecto_web/app/src/archivos 
http://127.0.0.1:5000/creaDb  <-crea la base de datos si no existe bajo el nombre de basedatos_001.sqlite3
