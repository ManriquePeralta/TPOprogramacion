# Funciones auxiliares para la gestión de reservas y paquetes turísticos


# Búsqueda secuencial para encontrar el índice del dato en la posición especificada
def busqueda_secuencial_por_posicion(lista, dato, posicion):
    i = 0
    # Recorre la lista hasta encontrar el dato o llegar al final
    while i < len(lista) and lista[i][posicion] != dato:
        i += 1
    # Si el dato se encuentra en la lista, devuelve su índice
    if i < len(lista):
        return i
    # Si no se encuentra, devuelve -1
    else:
        return -1


# Ordena una lista de listas por el valor en el índice especificado
def ordenar_lista(lista, indice):
    return sorted(lista, key=lambda x: x[indice])
