"""Estadisticas y reportes para el modulo de paquetes."""

from Paquetes_Pack.lista_paquetes import paquetes
from Paquetes_Pack.funciones_aux import (
    conteo_por_tipo,
    total_cupos,
    promedio_precio,
    max_precio,
    min_precio,
    paquetes_disponibles,
    paquetes_sin_cupo,
    destinos_unicos,
    ordenar_paquetes,
)


def estadisticas_paquetes():
    if not paquetes:
        print("\nNo hay paquetes registrados para calcular estadisticas.\n")
        return

    total = len(paquetes)
    disponibles = paquetes_disponibles(paquetes)
    sin_cupo = paquetes_sin_cupo(paquetes)

    precio_promedio = promedio_precio(paquetes)
    precio_maximo = max_precio(paquetes)
    precio_minimo = min_precio(paquetes)

    print("\n=== ESTADISTICAS DE PAQUETES ===")
    print("Resumen general")
    print(f"  Total de paquetes .......: {total}")
    print(f"  Cupos totales disponibles: {total_cupos(paquetes)}")
    print(f"  Con cupos ...............: {len(disponibles)}")
    print(f"  Sin cupos ...............: {len(sin_cupo)}")

    print("\nPrecios")
    print(f"  Promedio ................: ${precio_promedio:.2f}")
    print(f"  Maximo ..................: ${precio_maximo:.2f}")
    print(f"  Minimo ..................: ${precio_minimo:.2f}")

    print("\nDistribucion por tipo")
    tipos = conteo_por_tipo(paquetes)
    for tipo in sorted(tipos):
        cantidad = tipos[tipo]
        porcentaje = (cantidad / total) * 100
        print(f"  {tipo:<12}: {cantidad} paquetes ({porcentaje:.1f}%)")

    print("\nDestinos disponibles")
    for destino in destinos_unicos(paquetes):
        print(f"  - {destino}")

    print("\nPaquetes destacados")
    mas_cupos = max(paquetes, key=lambda p: int(p.get("cupos", 0)))
    mas_caro = max(paquetes, key=lambda p: float(p.get("precio", 0)))
    mas_barato = min(paquetes, key=lambda p: float(p.get("precio", 0)))

    print(
        f"  Mayor disponibilidad ..: ID {mas_cupos['id_paquete']} ({mas_cupos['destino']}) - {mas_cupos['cupos']} cupos"
    )
    print(
        f"  Precio mas alto ........: ID {mas_caro['id_paquete']} ({mas_caro['destino']}) - ${mas_caro['precio']}"
    )
    print(
        f"  Precio mas bajo ........: ID {mas_barato['id_paquete']} ({mas_barato['destino']}) - ${mas_barato['precio']}"
    )

    print()
