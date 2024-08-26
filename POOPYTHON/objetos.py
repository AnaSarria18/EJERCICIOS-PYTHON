
""" from perro import Perro

#instancias
perro1 =Perro("Tango", "Beagle")
perro2 = Perro("Apolo", "Lobo Siberiano")

perro1.caminar(10)
perro2.ladrar()
perro1.ladrar()

#se le puede cambiar el nombre porque es publico llamando directamente al atributo
perro2.nombre="Zeus"
perro2.caminar(15)
 """
 
 
 
""" from persona import Persona
from aprendiz import Aprendiz
from instructor import Instructor

per = Persona(11, "Alejandro", "alejandro@gmail.com")
print(per.getIdentificacion())

per.setIdentificacion(111)
print(per.getIdentificacion())

per2 = Persona()
print(per.getNombre())

per3 = Persona(nombre="Rosa", correo="rosa@gmail.com", identificacion="12345")
per4 = Persona("13", "Maria", "maria@gmail.com")



aprendiz = Aprendiz(320, "99", "Marco Pinto", "marco@gmail.com")
print(aprendiz.getIdentificacion())
aprendiz.setIdentificacion("100")
print(aprendiz.getIdentificacion())
print(aprendiz.getPuntajeIcfes())
aprendiz.setPuntajeIcfes(380)
print(aprendiz.getPuntajeIcfes())


aprendiz.saludar() """




""" from alumno import Alumno
from curso import Curso

unCurso = Curso("Desarrollo wed en python")

alumno1 = Alumno("Maria", 18)
alumno2 = Alumno("Pedro", 21)
alumno3 = Alumno("Alejandro", 28)

unCurso.matricularAlumno(alumno1)
unCurso.matricularAlumno(alumno2)
unCurso.matricularAlumno(alumno3)

print(f"Curso: {unCurso.getNombre()}")
print("Relacion de alumnos Matriculados")

alumnos = unCurso.getAlumnos()

for a in alumnos:
    print(a)
    print(a)

for a in alumnos:
    print(a.getNombre())
    print(a.getEdad())
 """






from empleado import Empleado
from empresa import Empresa

#creamos una empresa
elSena = Empresa("SENA")

#agregamos empleados
elSena.agregarEmpleado("Martin Rojas", "Director regional", 7000000)
elSena.agregarEmpleado("Pablo Ortiz", "Instructor", 6000000)
elSena.agregarEmpleado("Monica Galindo", "Tesorera", 5250000)

#para cada empleado de la lista se esta imprimiendo 
print(f"Lista de empleados de la empresa {elSena}")

for empleado in elSena.getEmpleados():
    print(empleado)
    
