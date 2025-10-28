# Estadisticas y reportes para el modulo de paquetes.

from Paquetes_Pack.funciones_aux import destinos_unicos, cargar_paquete_desde_archivo


def estadisticas_paquetes():
    # Calcula resumenes de disponibilidad y precios de los paquetes.
    paquetes = cargar_paquete_desde_archivo()
    if not paquetes:
        print("\nNo hay paquetes registrados para calcular estadisticas.\n")
        return

    # Inicializa contadores y acumuladores para los indicadores.
    total_paquetes = len(paquetes)
    cupos_totales = 0
    con_cupo = 0
    sin_cupo = 0
    suma_precios = 0.0
    tipo_conteo = {}

    # Conserva referencias a los paquetes que destacan en cada criterio.
    paquete_mas_cupos = None
    paquete_mas_caro = None
    paquete_mas_barato = None

    # Recorre todos los paquetes recopilando informacion relevante.
    for paquete in paquetes:
        cupos = int(paquete.get("cupos", 0))
        precio = float(paquete.get("precio", 0))
        tipo = paquete.get("tipo", "Sin tipo")

        # Acumula cupos y precios para obtener totales y promedios.
        cupos_totales += cupos
        suma_precios += precio

        # Clasifica los paquetes segun tengan o no cupos disponibles.
        if cupos > 0:
            con_cupo += 1
        else:
            sin_cupo += 1

        # Lleva un conteo por tipo para calcular distribuciones.
        if tipo in tipo_conteo:
            tipo_conteo[tipo] += 1
        else:
            tipo_conteo[tipo] = 1

        # Actualiza los paquetes destacados si supera los valores previos.
        if paquete_mas_cupos is None or cupos > int(paquete_mas_cupos.get("cupos", 0)):
            paquete_mas_cupos = paquete
        if paquete_mas_caro is None or precio > float(paquete_mas_caro.get("precio", 0)):
            paquete_mas_caro = paquete
        if paquete_mas_barato is None or precio < float(paquete_mas_barato.get("precio", 0)):
            paquete_mas_barato = paquete

    # Calcula el precio promedio a partir de los acumulados.
    promedio_precio = suma_precios / total_paquetes if total_paquetes else 0.0

    print("\n=== ESTADISTICAS DE PAQUETES ===")
    print("Resumen general")
    print(f"  Total de paquetes .......: {total_paquetes}")
    print(f"  Cupos totales disponibles: {cupos_totales}")
    print(f"  Con cupos ...............: {con_cupo}")
    print(f"  Sin cupos ...............: {sin_cupo}")

    print("\nPrecios")
    print(f"  Promedio ................: ${promedio_precio:.2f}")
    if paquete_mas_caro:
        print(f"  Maximo ..................: ${float(paquete_mas_caro.get('precio', 0)):.2f}")
    if paquete_mas_barato:
        print(f"  Minimo ..................: ${float(paquete_mas_barato.get('precio', 0)):.2f}")
    
    print("\nDistribucion por tipo")
    # ordena y cantidad y porcentaje por tipo de paquete
    for tipo in sorted(tipo_conteo):
        cantidad = tipo_conteo[tipo]
        porcentaje = (cantidad / total_paquetes) * 100
        print(f"  {tipo:<12}: {cantidad} paquetes ({porcentaje:.1f}%)")

    print("\nDestinos disponibles")
    for destino in destinos_unicos(paquetes):
        print(f"  - {destino}")

    # Resume los paquetes que ocupan los primeros lugares segun cada criterio.
    print("\nPaquetes destacados")
    if paquete_mas_cupos:
        print(
            f"  Mayor disponibilidad ..: ID {paquete_mas_cupos['id_paquete']} "
            f"({paquete_mas_cupos['destino']}) - {paquete_mas_cupos['cupos']} cupos"
        )
    if paquete_mas_caro:
        print(
            f"  Precio mas alto ........: ID {paquete_mas_caro['id_paquete']} "
            f"({paquete_mas_caro['destino']}) - ${paquete_mas_caro['precio']}"
        )
    if paquete_mas_barato:
        print(
            f"  Precio mas bajo ........: ID {paquete_mas_barato['id_paquete']} "
            f"({paquete_mas_barato['destino']}) - ${paquete_mas_barato['precio']}"
        )

    print()
