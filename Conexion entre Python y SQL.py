# Conexion entre Python y SQL
from platform import python_compiler
import pymysql

conexion = pymysql.connect (host='localhost', database='TP1', user ='root', password='Misql123#')

cursor = conexion.cursor()
cursor.execute(" SELECT year, count(year) as 'cantidad carreras corridas en el anio' FROM races GROUP BY year ORDER BY count(year) DESC LIMIT 1;  ")
for year in cursor:
    print ("Anio con mas carreras corridas:", year[0])

conexion.close()