# Creo la FastAPI siguiendo los pasos indicados en la pagina oficial de FastAPI

from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


from fastapi import FastAPI
import pymysql

app = FastAPI()

# En MySQL cargue los datasets y realice las 4 consultas solicitadas.
 
# funcion para mostrar los datos de la primera pregunta " Anio con más carreras "
@app.get("/Consulta1")
def  uno():
    miConexion = pymysql.connect(host='127.0.0.1', user= 'root', password='Misql123#', database='TP1')   
    cur = miConexion.cursor()
    cur.execute("SELECT year, count(year) as 'cantidad carreras corridas en el anio' FROM races GROUP BY year ORDER BY count(year) DESC LIMIT 1;" )
    datos = [row for row in cur.fetchall()]
    miConexion.close()
    return (datos)

# Segunda Pregunta "Piloto con mayor cantidad de primeros puestos"
@app.get("/Consulta2")
def  dos():
    miConexion = pymysql.connect(host='127.0.0.1', user= 'root', password='Misql123#', database='TP1')
    cur = miConexion.cursor()
    cur.execute("SELECT MAX(gan.driver) as 'cantidad carreras ganadas', gan.driverId as piloto, d.surname as Nombre FROM (SELECT driverId, COUNT(driverId) as driver FROM results_filtrados WHERE positionOrder='1' GROUP BY driverId) gan JOIN drivers d ON (gan.driverId=d.driverId);")
    datos = [row for row in cur.fetchall()]
    miConexion.close()
    return (datos)

# Tercera pregunta "Nombre del circuito mas corrido"
@app.get("/Consulta3")
def  tres():
    miConexion = pymysql.connect(host='127.0.0.1', user= 'root', password='Misql123#', database='TP1')
    cur = miConexion.cursor()
    cur.execute(" SELECT COUNT(circuitId), name FROM races GROUP BY circuitId ORDER BY COUNT(circuitId) DESC LIMIT 1; ")
    datos = [row for row in cur.fetchall()]
    miConexion.close()
    return (datos)

# Cuarta pregunta "Nombre del circuito mas corrido"
@app.get("/Consulta4")
def  cuatro():
    miConexion = pymysql.connect(host='127.0.0.1', user= 'root', password='Misql123#', database='TP1')
    cur = miConexion.cursor()
    cur.execute(" SELECT sum(r.points), r.driverId, d.surname FROM results_filtrados r JOIN drivers d ON (r.driverId=d.driverId) JOIN constructors_filtrados c ON (c.constructorId=r.constructorId) GROUP BY r.driverId and c.nationality='British' or c.nationality='American' ORDER BY SUM(points) DESC LIMIT 1;")
    datos = [row for row in cur.fetchall()]
    miConexion.close()
    return (datos)


