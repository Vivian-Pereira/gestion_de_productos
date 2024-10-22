productos = []
def cargar_datos():
    try:
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(", ")
                productos.append({"nombre": nombre, "precio": float(precio), "cantidad": int(cantidad)})
        print("Datos cargados correctamente.")
    except FileNotFoundError:
        print("Archivo no encontrado. Se iniciará con una lista vacía.")
def guardar_datos():
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            archivo.write(f'{producto["nombre"]}, {producto["precio"]}, {producto["cantidad"]}\n')
    print("Datos guardados correctamente.")
def añadir_producto():
    nombre = input("Introduce el nombre del producto: ")
    while True:
        try:
            precio = float(input("Introduce el precio del producto: "))
            break
        except ValueError:
            print("Por favor, introduce un precio válido (número).")
    
    while True:
        try:
            cantidad = int(input("Introduce la cantidad disponible: "))
            break
        except ValueError:
            print("Por favor, introduce una cantidad válida (número entero).")

    productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    print(f"Producto '{nombre}' añadido correctamente.")
def ver_productos():
    if not productos:
        print("No hay productos en la lista.")
    else:
        print("\nLista de productos:")
        for i, producto in enumerate(productos, 1):
            print(f'{i}. {producto["nombre"]} - Precio: ${producto["precio"]}, Cantidad: {producto["cantidad"]}')
def actualizar_producto():
    nombre = input("Introduce el nombre del producto a actualizar: ")
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            nuevo_nombre = input(f"Introduce el nuevo nombre (o presiona Enter para mantener '{producto['nombre']}'): ")
            if nuevo_nombre:
                producto["nombre"] = nuevo_nombre

            while True:
                try:
                    nuevo_precio = input(f"Introduce el nuevo precio (o presiona Enter para mantener ${producto['precio']}): ")
                    if nuevo_precio:
                        producto["precio"] = float(nuevo_precio)
                    break
                except ValueError:
                    print("Por favor, introduce un precio válido (número).")
            
            while True:
                try:
                    nueva_cantidad = input(f"Introduce la nueva cantidad (o presiona Enter para mantener {producto['cantidad']}): ")
                    if nueva_cantidad:
                        producto["cantidad"] = int(nueva_cantidad)
                    break
                except ValueError:
                    print("Por favor, introduce una cantidad válida (número entero).")

            print(f"Producto '{nombre}' actualizado correctamente.")
            return
    print(f"Producto '{nombre}' no encontrado.")
def eliminar_producto():
    nombre = input("Introduce el nombre del producto a eliminar: ")
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            productos.remove(producto)
            print(f"Producto '{nombre}' eliminado correctamente.")
            return
    print(f"Producto '{nombre}' no encontrado.")
def menu():
    cargar_datos()
    while True:
        print("\n1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")
menu()
