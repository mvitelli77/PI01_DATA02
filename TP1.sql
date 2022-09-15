CREATE DATABASE  IF NOT EXISTS `TP1` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `TP1`;

SELECT *
FROM constructors_filtrados;

ALTER TABLE constructors_filtrados
DROP MyUnknownColumn;

# Pregunta 1: Anio con mas carreras
SELECT year, count(year) as 'cantidad carreras corridas en el anio'
FROM races
GROUP BY year
ORDER BY count(year) DESC
LIMIT 1;

SELECT MAX(co.cant_carr) as 'cantidad maxima de carreras corridas en un anio' FROM 
   (SELECT count(year) as cant_carr 
    FROM races
	GROUP BY year) co;

# Pregunta 2: Piloto con mayor cantidad de primeros premios
SELECT MAX(gan.driver) as 'cantidad carreras ganadas', gan.driverId as piloto FROM 
       (SELECT driverId, COUNT(driverId) as driver
       FROM results_filtrados
       WHERE positionOrder='1'
       GROUP BY driverId) gan;

SELECT d.surname
FROM drivers d
JOIN results_filtrados r
 ON  (d.driverId=r.driverId)
 WHERE d.driverId= "1";

# Pregunta 3> Nombre del circuito mas corrido
SELECT COUNT(circuitId), name
FROM races
GROUP BY circuitId
ORDER BY COUNT(circuitId) DESC;

# Pregunta 4> Piloto con mayor cantidad de puntos en equipo Britanico o Americano
SELECT sum(r.points), r.driverId, d.surname
FROM results_filtrados r
JOIN drivers d
ON (r.driverId=d.driverId)
JOIN constructors_filtrados c
ON (c.constructorId=r.constructorId)
GROUP BY r.driverId and c.nationality="British" or c.nationality="American"
ORDER BY SUM(points) DESC;

SELECT driverId, constructorId
FROM results_filtrados
WHERE driverId=1;

SELECT name, constructorId
FROM constructors_filtrados
WHERE constructorId=1 or constructorId=131;

