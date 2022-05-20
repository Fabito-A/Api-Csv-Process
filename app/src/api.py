#api de conexion a la logica de python 
import json
from flask import Flask,jsonify, request
import controlador

api=Flask(__name__)

@api.route('/procesar',methods=['POST'])
def procesar_archivo():
    print(request.json)
    if request.method =='POST':
        data=request.get_json()
        valor=data["archivo"]
        mensaje=controlador.insertarReg(valor)   
        return jsonify(mensaje)
   
@api.route('/consultar',methods=['GET'])
def consultar_archivo():
    print(request.json)
    if request.method== 'GET':
        data=request.get_json()
        valor=data['archivo']
        resp=controlador.consultar(valor)
        return json.dumps(resp)

@api.route('/borrarTb',methods=['DELETE'])
def borrar_tabla():
    print(request.json)
    if request.method== 'DELETE':
        data=request.get_json()
        valor=data["tabla"]
        resp=controlador.borrar_tabla(valor)
        return resp

@api.route('/listar',methods=['GET'])
def listar_tablas():
    if request.method=='GET':
        data=controlador.listar_tablas()
        return jsonify(data)


if __name__ =="__main__":
   api.run(debug=True, port=5000)