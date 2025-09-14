import sys
import os
# Agregar la raíz del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


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


# Función principal para mostrar las estadísticas (salida más clara)
def estadisticas_reservas():
    if not reservas:
        print("\nNo hay reservas registradas para calcular estadísticas.\n")
        return

    # Ordenar reservas por destino antes de calcular estadísticas (no afecta resultados)
    reservas_ordenadas = ordenar_lista(reservas, 2)  # Ordenar por destino

    # Resumen desempaquetado (tupla -> variables)
    total, prom, maximo, minimo = resumen_basico()

    print("\n\n=== ESTADÍSTICAS DE RESERVAS ===")
    print(f"Total de reservas: {len(reservas_ordenadas)}")
    print(f"Promedio de personas por reserva: {prom:.2f}")
    print(f"Máximo de personas en una reserva: {maximo}")
    print(f"Mínimo de personas en una reserva: {minimo}")

    # Conteo por destino (orden alfabético)
    print("\nConteo por destino:")
    conteo = conteo_por_categoria()
    for destino in sorted(conteo.keys()):
        print(f"  {destino}: {conteo[destino]} reservas")

    # Porcentajes por destino (orden alfabético)
    print("\nPorcentajes por destino:")
    porcentajes = porcentajes_por_categoria()
    for destino in sorted(porcentajes.keys()):
        print(f"  {destino}: {porcentajes[destino]:.2f}%")

    # Set (destinos únicos) y Tupla (resumen) 
    print("\nDestinos únicos:", destinos_unicos())

    print("\nResumen de reservas:")
    print(f"  Total: {total}")
    print(f"  Promedio: {prom:.2f}")
    print(f"  Máximo: {maximo}")
    print(f"  Mínimo: {minimo}")
    print()


def destinos_unicos():
    """Devuelve lista de destinos sin duplicados (usa set)."""
    s = set()
    i = 0
    while i < len(reservas):
        s.add(reservas[i][2])  # destino en columna 2
        i += 1
    return list(s)


def resumen_basico():
    """Devuelve (total, promedio, max_personas, min_personas) como tupla."""
    t = total_reservas()
    if t == 0:
        return (0, 0.0, 0, 0)
    return (t, promedio_personas(), max_personas(), min_personas())
