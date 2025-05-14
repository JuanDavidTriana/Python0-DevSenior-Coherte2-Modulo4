def mostrar_estudiante(estudiante):
    """Mostrar los datos de un estudiante."""
    print("===================================")
    print("Número de documento:", estudiante[1])
    print("Nombre:", estudiante[2])
    print("Apellido:", estudiante[3])
    print("Fecha de nacimiento:", estudiante[4])
    print("Email:", estudiante[5])
    print("Teléfono:", estudiante[6])
    print("===================================")
    

def mostrar_estudiantes(estudiantes):
    """Mostrar la lista de estudiantes."""
    print("Lista de estudiantes:")
    for estudiante in estudiantes:
        mostrar_estudiante(estudiante)
    print("===================================")
