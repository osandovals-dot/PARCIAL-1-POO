class Libro:
    def __init__(self, titulo, autor, categoria):
        # Atributos del libro
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
    
    def mostrar_info(self):
            # para devolver un str con la información
            return f"{self.titulo} - {self.autor} - {self.categoria}"

class Usuario:
    def __init__(self, usuario):
        # Atributos del usuario
        usuario = Usuario(usuario)

    def mostrar_info(self):
        # patra devolver un str con la información del usuario
        return f"{self.nombre} (Documento: {self.documento})"
    
class UsuarioNormal(Usuario):
    def __init__(self, nombre, documento):
        super().__init__(nombre, documento)
        self.tipo = "Normal"


class Administrador(Usuario):
    def __init__(self, nombre, documento):
        super().__init__(nombre, documento)
        self.tipo = "Administrador"
    
class Biblioteca:
    def __init__(self):
        # Listas para guardar los objetos de tipo Libro y Usuario
        self.libros = []
        self.usuarios = []

        # Mínimo 3 categorías iniciales
        self.categorias = ["Ciencia", "Literatura", "Historia"]

    def registrar_libro(self, titulo, autor, categoria):
        if not isinstance(Usuario, Administrador): #REVISAR ESTOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
            print("Solo un administrador puede registrar libros.")
            main()
        # Si la categoría no existe se agrega automáticamente
        if categoria not in self.categorias:
            self.categorias.append(categoria)

        # Crear un objeto Libro con los datos
        nuevo_libro = Libro(titulo, autor, categoria)

        # Agregar el objeto Libro a la lista de libros
        self.libros.append(nuevo_libro)

    def registrar_usuario(self, usuario):
        # Crear un objeto Usuario con los datos
        usuario = Usuario(usuario)

        # Agregar el objeto Usuario a la lista de usuarios
        self.usuarios.append(usuario)

    def mostrar_libros(self):
        # Mostrar todos los libros registrados
        print("\n--- Lista de Libros ---")
        for libro in self.libros:
            print(libro.mostrar_info())
    
    def mostrar_usuarios(self):
        if not isinstance(Usuario, Administrador): #REVISAR ESTOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
            print("Solo un administrador puede ver los usuarios.")
            main()
        # Mostrar todos los usuarios registrados
        print("\n--- Lista de Usuarios ---")
        for usuario in self.usuarios:
            #Igual que en los libros, cada usuario sabe como "presentarse"
            print(usuario.mostrar_info())

    def mostrar_categorias(self):
        # Mostrar todas las categorías disponibles
        print("\n--- Categorías disponibles ---")
        for c in self.categorias:
            print("-", c)

# Crear una biblioteca (un objeto de la clase Biblioteca)
#biblioteca = Biblioteca()

# Registrar libros en la biblioteca EJEMPLOOOO
#biblioteca.registrar_libro("Cien años de soledad", "Gabo", "Literatura")
#biblioteca.registrar_libro("Fundamentos de Física", "Serway", "Ciencia")
#biblioteca.registrar_libro("Historia Universal", "Hobsbawm", "Historia")

# Registrar usuarios en la biblioteca EJEMPLOOOO
#biblioteca.registrar_usuario("Ana Pérez", "12345")
#biblioteca.registrar_usuario("Luis Gómez", "67890")

# Mostrar toda la información almacenada
#biblioteca.mostrar_libros()      # Lista de libros
#biblioteca.mostrar_usuarios()    # Lista de usuarios
#biblioteca.mostrar_categorias()  # Categorías

#PROGRAMA PRINCIPAL
# PROGRAMA PRINCIPAL
def main():
    biblioteca = Biblioteca()

    # Registro de usuario
    Tipo_de_usuario = int(input("Qué tipo de usuario es usted:\n1. Usuario Normal\n2. Administrador\n---> "))

    if Tipo_de_usuario == 1:
        nombre = input("Nombre: ")
        documento = input("Documento: ")
        usuario = UsuarioNormal(nombre, documento)
        biblioteca.registrar_usuario(usuario)

    elif Tipo_de_usuario == 2:
        nombre = input("Nombre: ")
        documento = input("Documento: ")
        usuario = Administrador(nombre, documento)
        biblioteca.registrar_usuario(usuario)

    else:
        print("Opción inválida.")
        return

    biblioteca.registrar_usuario(usuario)

    # Menú principal en bucle
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar nuevo libro")
        print("2. Mostrar libros")
        print("3. Mostrar usuarios")
        print("4. Mostrar categorías")
        print("5. Salir")

        opcion = int(input("---> "))

        if opcion == 1:
            Nombre_del_libro = input("Título del libro: ")
            Autor_del_libro = input("Autor del libro: ")
            Genero_del_libro = input("Categoría del libro: ")
            biblioteca.registrar_libro(usuario, Nombre_del_libro, Autor_del_libro, Genero_del_libro)

        elif opcion == 2:
            biblioteca.mostrar_libros()

        elif opcion == 3:
            biblioteca.mostrar_usuarios(usuario)

        elif opcion == 4:
            biblioteca.mostrar_categorias()

        elif opcion == 5:
            print("Saliendo del sistema")
            break

        else:
            print("Opción inválida, intente de nuevo.")
main()
