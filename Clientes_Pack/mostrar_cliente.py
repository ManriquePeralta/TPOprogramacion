from Clientes_Pack.lista_clientes import clientes  
def mostrar_clientes():
    print("\n " + " ===== LISTA DE CLIENTES ACTIVOS =====")
    activos = [c for c in clientes if c[4] == "activo"]
    
    if len(clientes) == 0:
        print("⚠️ No hay clientes activos.")
        return
    else:
        # Ordenar por ID en lugar de DNI y Email
        clientes_ordenados = sorted(clientes, key=lambda fila: fila[0])
        
        # Encabezado
        print(f'{"ID":<5} | {"Nombre":<10} | {"DNI":<10} |  {"Email"} |  {"Estado"}')
        print("-" * 70)
        
        # Filas
        for c in clientes_ordenados:
            print(f'{c[0]:<5} | {c[1]:<10} | {c[2]:<10} | {c[3]} | {c[4]}')
    
    return clientes_ordenados
