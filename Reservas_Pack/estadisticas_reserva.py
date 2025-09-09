# Importar la lista de reservas
from Reservas_Pack.lista_reservas import reservas

# Importar la función ordenar_lista
from Reservas_Pack.funciones_aux import ordenar_lista


# Función para calcular el total de reservas
def total_reservas():
    return len(reservas)


# Función para calcular el promedio de personas por reserva
def promedio_personas():
    if not reservas:
        return 0
    return sum(reserva[3] for reserva in reservas) / total_reservas()


# Función para encontrar el máximo de personas por reserva
def max_personas():
    if not reservas:
        return 0
    return max(reservas, key=lambda x: x[3])[3]


# Función para encontrar el mínimo de personas por reserva
def min_personas():
    if not reservas:
        return 0
    return min(reservas, key=lambda x: x[3])[3]


# Función para calcular el conteo por categoría (destino)
def conteo_por_categoria():
    conteo_categorias = {}
    for reserva in reservas:
        destino = reserva[2]
        if destino in conteo_categorias:
            conteo_categorias[destino] += 1
        else:
            conteo_categorias[destino] = 1
    return conteo_categorias


# Función para calcular los porcentajes por categoría
def porcentajes_por_categoria():
    conteo_categorias = conteo_por_categoria()
    total = total_reservas()
    return {
        destino: (conteo / total) * 100 for destino, conteo in conteo_categorias.items()
    }


# Función principal para mostrar las estadísticas
def estadisticas_reservas():
    if not reservas:
        print("\nNo hay reservas registradas para calcular estadísticas.\n")
        return

    # Ordenar reservas por destino antes de calcular estadísticas
    reservas_ordenadas = ordenar_lista(reservas, 2)  # Ordenar por destino

    print("\n\n=== ESTADÍSTICAS DE RESERVAS ===")
    print(f"Total de reservas: {len(reservas_ordenadas)}")
    print(f"Promedio de personas por reserva: {promedio_personas():.2f}")
    print(f"Máximo de personas en una reserva: {max_personas()}")
    print(f"Mínimo de personas en una reserva: {min_personas()}")

    print("\nConteo por destino:")
    for destino, conteo in conteo_por_categoria().items():
        print(f"  {destino}: {conteo} reservas")

    print("\nPorcentajes por destino:")
    for destino, porcentaje in porcentajes_por_categoria().items():
        print(f"  {destino}: {porcentaje:.2f}%")

    print()
