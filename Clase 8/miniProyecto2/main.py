from controller import estudiantesController
from controller import docentesController
from controller import cursosController

def menuGeneral():
    while True:
        print("\n--- Menú General ---")
        print("1. Menú de Estudiantes")
        print("2. Menú de Docentes")
        print("3. Menú de Cursos")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menuEstudiantes()
        elif opcion == "2":
            menuDocente()
        elif opcion == "3":
            menuCursos()
        elif opcion == "4":
            print("Saliendo del menú general.")
            break
       

def menuEstudiantes():
    while True:
        print("\n--- Menú de Estudiantes ---")
        print("1. Crear Estudiante")
        print("2. Mostrar Estudiantes")
        print("3. Buscar Estudiante por Documento")
        print("4. Modificar Estudiante")
        print("5. Eliminar Estudiante")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero_documento = input("Ingrese el número de documento: ")
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            fecha_nacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
            email = input("Ingrese el email: ")
            telefono = input("Ingrese el teléfono: ")

            estudiantesController.crear_estudiante(numero_documento, nombre, apellido, fecha_nacimiento, email, telefono)
        elif opcion == "2":
            estudiantesController.mostar_estudiantes() 
        elif opcion == "3":
            id_estudiante = input("Ingrese el número de documento del estudiante: ")
            estudiantesController.mostrar_estudiante(id_estudiante)
        elif opcion == "4":
            numero_documento = input("Ingrese el número de documento del estudiante a modificar: ")
            nombre = input("Ingrese el nuevo nombre: ")
            apellido = input("Ingrese el nuevo apellido: ")
            fecha_nacimiento = input("Ingrese la nueva fecha de nacimiento (YYYY-MM-DD): ")
            email = input("Ingrese el nuevo email: ")
            telefono = input("Ingrese el nuevo teléfono: ")

            estudiantesController.modificar_estudiante(numero_documento, nombre, apellido, fecha_nacimiento, email, telefono)
        elif opcion == "5":
            numero_documento = input("Ingrese el número de documento del estudiante a eliminar: ")
            estudiantesController.eliminar_estudiante(numero_documento)
        elif opcion == "6":
            print("Saliendo del menú de estudiantes.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            menuEstudiantes()
def menuDocente():
    while True:
        print("\n--- Menú de Docentes ---")
        print("1. Crear Docente")
        print("2. Mostrar Docentes")
        print("3. Buscar Docente por Documento")
        print("4. Actualizar Docente")
        print("5. Eliminar Docente")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero_documento = input("Ingrese el número de documento: ")
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            email = input("Ingrese el email: ")
            telefono = input("Ingrese el teléfono: ")
            especialidad = input("Ingrese la especialidad: ")

            docentesController.crear_docente(numero_documento, nombre, apellido, email, telefono, especialidad)
        elif opcion == "2":
            docentesController.mostrar_docentes()

        elif opcion == "3":
            numero_documento = input("Ingrese el número de documento del docente: ")
            docentesController.mostrar_docente(numero_documento)
        elif opcion == "4":
            numero_documento = input("Ingrese el número de documento del docente a actualizar: ")
            nombre = input("Ingrese el nuevo nombre: ")
            apellido = input("Ingrese el nuevo apellido: ")
            email = input("Ingrese el nuevo email: ")
            telefono = input("Ingrese el nuevo teléfono: ")
            especialidad = input("Ingrese la nueva especialidad: ")

            docentesController.modificar_docente(numero_documento, nombre, apellido, email, telefono, especialidad)
        elif opcion == "5":
            numero_documento = input("Ingrese el número de documento del docente a eliminar: ")
            docentesController.eliminar_docente(numero_documento)
        elif opcion == "6":
            print("Saliendo del menú de docentes.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menuCursos():
    while True:
        print("\n--- Menú de Cursos ---")
        print("1. Ver Cursos")
        print("2. Ver Cursos por Docente")
        print("6. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            cursosController.mostrar_cursos()
        elif opcion == "2":
            id_docente = input("Ingrese el número de documento del docente: ")
            cursosController.mostrar_curso_por_docente(id_docente)

        elif opcion == "6":
            print("Saliendo del menú de cursos.")
            break

if __name__ == "__main__":
    menuGeneral()

