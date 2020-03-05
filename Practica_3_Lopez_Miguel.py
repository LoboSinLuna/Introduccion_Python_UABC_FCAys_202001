class Estudiante:
 #Indicamos atributos
 edad = 21
 carrera = "Desconocida"
 universidad = "Desconocida"
 genero = "Masculino"
 
 #definimos funciones
 def festejar(self) :
   print("Festejando...")
   
 def estudiar(self, materia) :
   print("Estudiando "+  materia )
   
 def llorar(self) :
   print("Llorando...")
   
 def dormir(self) :
   print("Durmiendo...")
   
   #Ajustamos la edad
 def cambiarEdad(self, edadAlumno) :
   self.edad = edadAlumno
   print("Nueva Edad =", edadAlumno)
   
#Generamos un nuevo Estudiante
Miguel = Estudiante()
Miguel.estudiar("Logica Para La Programacion")
#imprimimos atributo del objeto
Miguel.cambiarEdad(21)
print(Miguel.edad)