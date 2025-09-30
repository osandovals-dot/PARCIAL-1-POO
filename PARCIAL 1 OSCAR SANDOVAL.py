


# CLASE LIBRO

class Libro:
    def __init__(self, titulo, autor, categoria):
        # Guardamos los atributos básicos de un libro
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
    
    def mostrar_info(self):
        # Devolvemos la información del libro en un formato legible
        return f"{self.titulo} - {self.autor} - {self.categoria}"



# CLASE USUARIO (GENÉRICA)

class Usuario:
    def __init__(self, nombre, documento):
        # Atributos comunes para cualquier usuario
        self.nombre = nombre
        self.documento = documento

    def mostrar_info(self):
        # Cada usuario puede mostrar su información
        return f"{self.nombre} (Documento: {self.documento})"



# SUBCLASE USUARIO NORMAL

class UsuarioNormal(Usuario):
    def __init__(self, nombre, documento):
        # Heredamos de Usuario y añadimos un tipo
        super().__init__(nombre, documento)
        self.tipo = "Normal"



# SUBCLASE ADMINISTRADOR

class Administrador(Usuario):
    def __init__(self, nombre, documento):
        # Heredamos de Usuario y añadimos un tipo
        super().__init__(nombre, documento)
        self.tipo = "Administrador"



# CLASE BIBLIOTECA

class Biblioteca:
    def __init__(self):
        # Inicializamos las listas para guardar libros y usuarios
        self.libros = []
        self.usuarios = []
        # Arrancamos con categorías mínimas
        self.categorias = ["Ciencia", "Literatura", "Historia"]

    def registrar_libro(self, usuario, titulo, autor, categoria):
        # Validamos que SOLO un administrador pueda registrar libros
        if not isinstance(usuario, Administrador):
            print("Solo un administrador puede registrar libros.")
            return

        # Si la categoría no existe, se agrega automáticamente
        if categoria not in self.categorias:
            self.categorias.append(categoria)

        # Creamos un nuevo objeto Libro con los datos ingresados
        nuevo_libro = Libro(titulo, autor, categoria)

        # Lo añadimos a la lista de libros
        self.libros.append(nuevo_libro)
        print(f"Libro '{titulo}' registrado con éxito.")

    def registrar_usuario(self, usuario):
        # Añadimos un objeto usuario (ya instanciado) a la lista
        self.usuarios.append(usuario)
        print(f"Usuario '{usuario.nombre}' registrado con éxito.")

    def mostrar_libros(self):
        # Mostramos todos los libros almacenados
        print("\n--- Lista de Libros ---")
        if not self.libros:
            print("No hay libros registrados.")
        for libro in self.libros:
            print(libro.mostrar_info())
    
    def mostrar_usuarios(self, usuario):
        # Validamos que SOLO un administrador pueda ver usuarios
        if not isinstance(usuario, Administrador):
            print("Solo un administrador puede ver la lista de usuarios.")
            return

        # Mostramos los usuarios registrados
        print("\n--- Lista de Usuarios ---")
        if not self.usuarios:
            print("No hay usuarios registrados.")
        for u in self.usuarios:
            print(u.mostrar_info())

    def mostrar_categorias(self):
        # Mostramos todas las categorías disponibles
        print("\n--- Categorías disponibles ---")
        for c in self.categorias:
            print("-", c)


# PROGRAMA PRINCIPAL

def main():
    # Creamos la biblioteca
    biblioteca = Biblioteca()

    # Primero pedimos el tipo de usuario
    Tipo_de_usuario = int(input("Qué tipo de usuario es usted:\n1. Usuario Normal\n2. Administrador\n---> "))

    if Tipo_de_usuario == 1:
        # Si es usuario normal, pedimos datos
        nombre = input("Nombre: ")
        documento = input("Documento: ")
        usuario = UsuarioNormal(nombre, documento)
        biblioteca.registrar_usuario(usuario)

    elif Tipo_de_usuario == 2:
        # Si es administrador, pedimos datos
        nombre = input("Nombre: ")
        documento = input("Documento: ")
        usuario = Administrador(nombre, documento)
        biblioteca.registrar_usuario(usuario)

    else:
        # Validamos si meten un número que no corresponde
        print("Opción inválida.")
        return

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
            # Pedimos datos para registrar un libro
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            categoria = input("Categoría del libro: ")
            biblioteca.registrar_libro(usuario, titulo, autor, categoria)

        elif opcion == 2:
            biblioteca.mostrar_libros()

        elif opcion == 3:
            biblioteca.mostrar_usuarios(usuario)

        elif opcion == 4:
            biblioteca.mostrar_categorias()

        elif opcion == 5:
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida, intente de nuevo.")


# Ejecutamos el programa principal
if __name__ == "__main__":
    main()

