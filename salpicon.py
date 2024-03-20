print("**SALPICONES TENTACIONES**")
print("*********")

def agregar_productos():
    productos = []
    n = int(input("Ingrese la cantidad de productos que desea agregar al salpicón: "))
    for i in range(1, n + 1):
        producto = {}
        producto["id"] = i
        producto["nombre"] = input(f"Ingrese el nombre del producto {i}: ")
        producto["precio_unidad"] = float(input(f"Ingrese el precio unidad {i}: "))
        producto["cantidad"] = int(input(f"Ingrese la cantidad del producto {i}: "))
        productos.append(producto)
    return productos

def costo_total(productos):
    costo_total = sum(producto["precio_unidad"] * producto["cantidad"] for producto in productos)
    return costo_total

def productos_ordenados_por_precio(productos):
    productos_ordenados = sorted(productos, key=lambda x: x["precio_unidad"], reverse=True)
    print("Productos ordenados por precio (de mayor a menor):")
    for producto in productos_ordenados:
        print(f"Nombre: {producto['nombre']}, Precio unidad: {producto['precio_unidad']}")

def producto_economico(productos):
    producto_barato = min(productos, key=lambda x: x["precio_unidad"])
    return producto_barato

productos = agregar_productos()

costo_total = costo_total(productos)

print(f"Costo total del salpicón: {costo_total}")

productos_ordenados_por_precio(productos)

producto_barato = producto_economico(productos)

print(f"El producto más barato es: {producto_barato['nombre']} con precio unitario de {producto_barato['precio_unidad']}")