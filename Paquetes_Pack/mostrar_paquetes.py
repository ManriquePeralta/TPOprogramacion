from Paquetes_Pack.lista_paquetes import paquetes

def mostrar_paquetes():
    ancho_destino = 20
    ancho_precio = 10
    ancho_fecha = 12
    ancho_cupos = 6
    ancho_tipo = 10
    ancho_desc = 40

    # Header
    print(f'{"Destino":<{ancho_destino}} {"Precio":>{ancho_precio}} {"Desde":^{ancho_fecha}} {"Hasta":^{ancho_fecha}} {"Cupos":>{ancho_cupos}} {"Tipo":<{ancho_tipo}} {"Descripcion":<{ancho_desc}}')
    print("-" * (ancho_destino + ancho_precio + 2 * ancho_fecha + ancho_cupos + ancho_tipo + ancho_desc + 6))

    if not paquetes:
        print("No hay paquetes disponibles.")
        return
    # Filas
    for paquete in paquetes:
        print(f'{paquete["destino"]:<{ancho_destino}} ${paquete["precio"]:>{ancho_precio - 1}} {paquete["fecha_inicio"]:^{ancho_fecha}} {paquete["fecha_fin"]:^{ancho_fecha}} {paquete["cupos"]:>{ancho_cupos}} {paquete["tipo"]:<{ancho_tipo}} {paquete["descripcion"]:<{ancho_desc}}')
