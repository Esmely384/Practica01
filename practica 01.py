print ("Sistema para calcular el promedio de una alumno")
# Creamos una variable para el nombre
nombre = input("Para comenzar, ¿Cuál es tu nombre?: ")
# Creamos variables para las materias
spanish = int (input(nombre + "¿Cuál es tu calificación de español?" ))
matematicas = int(input(nombre + "¿Cuál es tu calificación de matemáticas?" ))
quimica = int (input(nombre + "¿Cuál es tu calificación de química?" ))
historia = int(input(nombre + "¿Cuál es tu calificación de historia?" ))
computacion = int(input(nombre + "¿Cuál es tu calificación de computación?" ))
english = int(input(nombre + "¿Cuál es tu calificación de inglés?" ))
mentoria = int(input(nombre + "¿Cuál es tu calificación de mentoría?" ))
# Creamos variables para evaluar los promedios
promedio = (spanish + matematicas + quimica + historia + computacion + english + mentoria) / 7 
# Creamos una condicional para comparar el promedio
if promedio <= 6:
    print ( nombre + "siento informarte que no aprobaste tu promedio fue: ", promedio )
if promedio >= 6: 
    print ( nombre + "apenas aprobaste con un promedio de : ", promedio)
if promedio >= 7: 
    print ( nombre + "pasaste : ", promedio)
if promedio >= 8: 
    print ( "Felicidades" + nombre + "aprobaste con : ", promedio) 
if promedio >= 9: 
    print ( "Felicidades" + nombre + "aprobaste con : ", promedio + "sigue con el buen trabajo") 
if promedio >= 10: 
    print ( "Muchas felicidades" + nombre + "aprobaste con un promedio exelente de : ", promedio ) 
 