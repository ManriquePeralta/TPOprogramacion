from Paquetes_Pack.lista_paquetes import paquetes

def mostrar_paquetes():
    ancho_destino = 20
    ancho_precio = 10
    ancho_fecha = 12
    ancho_cupos = 6
    ancho_tipo = 10
    ancho_desc = 40

    # Header
    print(f'{"Destino":<{ancho_destino}} {"Precio":>{ancho_precio}} {"Desde":^{ancho_fecha}} {"Hasta":^{ancho_fecha}} {"Stock":>{ancho_cupos}} {"Tipo":<{ancho_tipo}} {"Descripcion":<{ancho_desc}}')
    print("-" * (ancho_destino + ancho_precio + 2 * ancho_fecha + ancho_cupos + ancho_tipo + ancho_desc + 6))

    if not paquetes:
        print("No hay paquetes disponibles.")
        return
    # Filas
    for paquete in paquetes:
        destino, precio, fecha_desde, fecha_hasta, cupos, tipo, descripcion = paquete
        print(f'{destino:<{ancho_destino}} ${precio:>{ancho_precio - 1}} {fecha_desde:^{ancho_fecha}} {fecha_hasta:^{ancho_fecha}} {cupos:>{ancho_cupos}} {tipo:<{ancho_tipo}} {descripcion:<{ancho_desc}}')
