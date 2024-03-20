print("**TIENDA COMIC**")
print("*********")

class Producto:
    contador_id = 1

    def _init_(objeto_actual, nombre, precio, ubicacion, descripcion, casa, referencia, pais_origen, unidades, garantia):
        objeto_actual.id = Producto.contador_id
        Producto.contador_id += 1
        objeto_actual.nombre = nombre
        objeto_actual.precio = precio
        objeto_actual.ubicacion = ubicacion
        objeto_actual.descripcion = descripcion
        objeto_actual.casa = casa
        objeto_actual.referencia = referencia
        objeto_actual.pais_origen = pais_origen
        objeto_actual.unidades = unidades
        objeto_actual.garantia = garantia

class TiendaComics:
    def _init_(objeto_actual):
        objeto_actual.inventario = []

    def agregar_producto(objeto_actual, producto):
        objeto_actual.inventario.append(producto)
        print("Producto registrado exitosamente.")

    def mostrar_productos_bodega(objeto_actual):
        if not objeto_actual.inventario:
            print("No hay productos en bodega.")
            return
        print("Productos en bodega:")
        for producto in objeto_actual.inventario:
            print(f"ID: {producto.id}, Nombre: {producto.nombre}, Unidades: {producto.unidades}")

    def buscar_producto_por_nombre(objeto_actual, nombre):
        encontrado = False
        for producto in objeto_actual.inventario:
            if producto.nombre.lower() == nombre.lower():
                print(f"ID: {producto.id}, Nombre: {producto.nombre}, Precio: {producto.precio}, Descripción: {producto.descripcion}")
                encontrado = True
        if not encontrado:
            print("Producto no encontrado.")

    def modificar_unidades_compradas(objeto_actual, nombre, nuevas_unidades):
        for producto in objeto_actual.inventario:
            if producto.nombre.lower() == nombre.lower():
                if nuevas_unidades <= producto.unidades:
                    producto.unidades = nuevas_unidades
                    print("Unidades modificadas exitosamente.")
                else:
                    print("Error: Las nuevas unidades no pueden ser mayores que las unidades originales.")
                return
        print("Producto no encontrado.")

    def eliminar_producto(objeto_actual, nombre):
        for producto in objeto_actual.inventario:
            if producto.nombre.lower() == nombre.lower():
                confirmacion = input("¿Estás seguro que deseas eliminar este producto? (s/n): ")
                if confirmacion.lower() == "s":
                    objeto_actual.inventario.remove(producto)
                    print("Producto eliminado correctamente.")
                return
        print("Producto no encontrado.")

def main():
    tienda = TiendaComics()

    while True:
        print("\n--- Menú ---")
        print("1. Registrar producto")
        print("2. Mostrar productos en bodega")
        print("3. Buscar producto por nombre")
        print("4. Modificar unidades compradas de un producto")
        print("5. Eliminar producto")
        print("6. Salir")

        opcion = input("Ingrese el número de la opción que desea: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio unitario del producto: "))
            ubicacion = input("Ubicación en la tienda (A, B, C o D): ")
            descripcion = input("Descripción del producto: ")
            casa = input("Casa a la que pertenece el producto (Marvel, DC, etc): ")
            referencia = input("Referencia del producto: ")
            pais_origen = input("País de origen del producto: ")
            unidades = int(input("Número de unidades compradas del producto: "))
            garantia = input("Producto con garantía extendida (true/false): ").lower() == "true"
            producto = Producto(nombre, precio, ubicacion, descripcion, casa, referencia, pais_origen, unidades, garantia)
            tienda.agregar_producto(producto)

        elif opcion == "2":
            tienda.mostrar_productos_bodega()

        elif opcion == "3":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            tienda.buscar_producto_por_nombre(nombre)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto al que desea modificar las unidades compradas: ")
            nuevas_unidades = int(input("Ingrese el nuevo número de unidades compradas: "))
            tienda.modificar_unidades_compradas(nombre, nuevas_unidades)

        elif opcion == "5":
            nombre = input("Ingrese el nombre del producto que desea eliminar: ")
            tienda.eliminar_producto(nombre)

        elif opcion == "6":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 6.")

if _name_ == "_main_":
    main()