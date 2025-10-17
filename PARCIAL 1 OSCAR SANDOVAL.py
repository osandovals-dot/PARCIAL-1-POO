import firebase_admin
from firebase_admin import credentials, db

# Inicialización de Firebase
cred = credentials.Certificate(r"C:\Users\User\Downloads\bibliotecaoscar.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://bibliotecaoscar-a7820-default-rtdb.firebaseio.com/"  
})



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
        # Referencias a las ramas de la base de datos
        self.ref_libros = db.reference("libros")
        self.ref_usuarios = db.reference("usuarios")
        self.ref_categorias = db.reference("categorias")

        # Categorías por defecto (si no existen en Firebase)
        if not self.ref_categorias.get():
            self.ref_categorias.set(["Ciencia", "Literatura", "Historia"])

    def registrar_libro(self, usuario, titulo, autor, categoria):
        if not isinstance(usuario, Administrador):
            print("Solo un administrador puede registrar libros.")
            return

        # Agregar categoría si no existe
        categorias = self.ref_categorias.get() or []
        if categoria not in categorias:
            categorias.append(categoria)
            self.ref_categorias.set(categorias)

        # Guardar el libro en Firebase
        nuevo_libro = {
            "titulo": titulo,
            "autor": autor,
            "categoria": categoria
        }
        self.ref_libros.push(nuevo_libro)
        print(f"Libro '{titulo}' registrado con éxito en Firebase.")

    def registrar_usuario(self, usuario):
        nuevo_usuario = {
            "nombre": usuario.nombre,
            "documento": usuario.documento,
            "tipo": usuario.tipo
        }
        self.ref_usuarios.push(nuevo_usuario)
        print(f"Usuario '{usuario.nombre}' registrado con éxito en Firebase.")

    def mostrar_libros(self):
        print("\n--- Lista de Libros ---")
        libros = self.ref_libros.get()
        if not libros:
            print("No hay libros registrados.")
            return
        for id_libro, datos in libros.items():
            print(f"{datos['titulo']} - {datos['autor']} - {datos['categoria']}")

    def mostrar_usuarios(self, usuario):
        if not isinstance(usuario, Administrador):
            print("Solo un administrador puede ver la lista de usuarios.")
            return

        print("\n--- Lista de Usuarios ---")
        usuarios = self.ref_usuarios.get()
        if not usuarios:
            print("No hay usuarios registrados.")
            return
        for id_usuario, datos in usuarios.items():
            print(f"{datos['nombre']} (Documento: {datos['documento']}) - {datos['tipo']}")

    def mostrar_categorias(self):
        print("\n--- Categorías disponibles ---")
        categorias = self.ref_categorias.get()
        for c in categorias:
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

