"""Estadisticas y reportes del modulo de reservas."""

from Reservas_Pack.lista_reservas import reservas
from Reservas_Pack.funciones_aux import ordenar_reservas, reservas_por_estado
from Clientes_Pack.lista_clientes import clientes
from Clientes_Pack.funciones_aux import formatear_estado as formatear_estado_cliente
from Paquetes_Pack.lista_paquetes import paquetes


def estadisticas_reservas():
    if not reservas:
        print("No hay reservas registradas para generar estadisticas.")
        return

    normalizadas = [normalizar_reserva(reserva) for reserva in reservas]

    total = len(normalizadas)
    activas = sum(1 for r in normalizadas if r['estado'] == 'activa')
    canceladas = sum(1 for r in normalizadas if r['estado'] == 'cancelada')

    personas_total = sum(r['personas'] for r in normalizadas)
    promedio_personas = personas_total / total if total else 0

    print("=== ESTADISTICAS DE RESERVAS ===")
    print("Reservas")
    print(f"  Total ..........: {total}")
    print(f"  Activas ........: {activas}")
    print(f"  Canceladas .....: {canceladas}")

    print("Personas")
    print(f"  Total ..........: {personas_total}")
    print(f"  Promedio por reserva: {promedio_personas:.2f}")

    resumen_estados = personas_por_estado(normalizadas)
    if resumen_estados:
        for estado, info in resumen_estados.items():
            print(f"  {estado:<10} -> {info['reservas']} reservas / {info['personas']} personas")

    clientes_destacados = top_clientes(normalizadas)
    print()
    print("Clientes destacados")
    if clientes_destacados:
        idx = 1
        for data in clientes_destacados:
            print(
                f"  #{idx} {data['nombre']} (ID {data['id']}) - "
                f"{data['reservas']} reservas, {data['personas']} personas"
            )
            idx += 1
    else:
        print("  No hay clientes con reservas registradas.")

    destinos_destacados = top_destinos(normalizadas)
    print()
    print("Destinos favoritos")
    if destinos_destacados:
        idx = 1
        for data in destinos_destacados:
            print(
                f"  #{idx} {data['destino']} - {data['reservas']} reservas, {data['personas']} personas"
            )
            idx += 1
    else:
        print("  Sin destinos registrados.")

    paquetes_destacados = top_paquetes(normalizadas)
    print()
    print("Paquetes con mayor demanda")
    if paquetes_destacados:
        idx = 1
        for data in paquetes_destacados:
            linea = (
                f"  #{idx} ID {data['id']} - {data['destino']} | {data['reservas']} reservas"
            )
            if data['ingresos'] is not None:
                linea += f" | Ingreso estimado: ${data['ingresos']:.2f}"
            print(linea)
            idx += 1
    else:
        print("  No hay paquetes asociados a reservas.")

    print()
    print("Reservas recientes")
    for reserva in ordenar_reservas(normalizadas)[-3:]:
        cliente = buscar_cliente(reserva['id_cliente'])
        nombre_cliente = cliente['nombre'] if cliente else "Desconocido"
        print(
            f"  ID {reserva['id_reserva']:>3} | Cliente {nombre_cliente:<20} | "
            f"Destino {reserva['destino']:<18} | Estado {reserva['estado'].capitalize()}"
        )

    print()


def normalizar_reserva(reserva):
    if type(reserva) is dict:
        destino = reserva.get('destino')
        paquete = buscar_paquete(reserva.get('id_paquete'))
        if destino is None and paquete:
            destino = paquete.get('destino')
        precio_unitario = reserva.get('precio_unitario')
        if precio_unitario is None and paquete:
            precio_unitario = paquete.get('precio')
        return {
            'id_reserva': reserva.get('id_reserva'),
            'id_cliente': reserva.get('id_cliente'),
            'id_paquete': reserva.get('id_paquete'),
            'destino': destino or 'Sin datos',
            'personas': to_int(reserva.get('personas', 0)),
            'estado': reserva.get('estado', 'activa').lower(),
            'precio_unitario': precio_unitario,
        }

    destino = reserva[2] if len(reserva) > 2 else 'Sin datos'
    paquete = buscar_paquete_por_destino(destino)
    precio_unitario = paquete.get('precio') if paquete else None
    return {
        'id_reserva': reserva[0],
        'id_cliente': reserva[1] if len(reserva) > 1 else None,
        'id_paquete': paquete.get('id_paquete') if paquete else None,
        'destino': destino,
        'personas': to_int(reserva[3]) if len(reserva) > 3 else 0,
        'estado': 'activa',
        'precio_unitario': precio_unitario,
    }

def personas_por_estado(reservas_normalizadas):
    resumen = {}
    for reserva in reservas_normalizadas:
        estado = reserva['estado']
        if estado not in resumen:
            resumen[estado] = {'reservas': 0, 'personas': 0}
        resumen[estado]['reservas'] += 1
        resumen[estado]['personas'] += reserva['personas']
    return {
        estado.capitalize(): datos for estado, datos in resumen.items()
    }


def top_clientes(reservas_normalizadas, limite=3):
    conteo = {}
    for reserva in reservas_normalizadas:
        cid = reserva['id_cliente']
        if cid not in conteo:
            conteo[cid] = {'reservas': 0, 'personas': 0}
        conteo[cid]['reservas'] += 1
        conteo[cid]['personas'] += reserva['personas']

    ranking = []
    for cid, datos in conteo.items():
        cliente = buscar_cliente(cid)
        if not cliente:
            continue
        ranking.append({
            'id': cliente['id'],
            'nombre': cliente['nombre'],
            'reservas': datos['reservas'],
            'personas': datos['personas'],
        })

    ranking.sort(key=lambda item: (-item['reservas'], -item['personas'], item['nombre']))
    return ranking[:limite]


def top_destinos(reservas_normalizadas, limite=3):
    conteo = {}
    for reserva in reservas_normalizadas:
        destino = reserva['destino']
        if destino not in conteo:
            conteo[destino] = {'reservas': 0, 'personas': 0}
        conteo[destino]['reservas'] += 1
        conteo[destino]['personas'] += reserva['personas']

    ranking = [
        {
            'destino': destino,
            'reservas': datos['reservas'],
            'personas': datos['personas'],
        }
        for destino, datos in conteo.items()
    ]
    ranking.sort(key=lambda item: (-item['reservas'], -item['personas'], item['destino']))
    return ranking[:limite]


def top_paquetes(reservas_normalizadas, limite=3):
    conteo = {}
    for reserva in reservas_normalizadas:
        paquete = buscar_paquete(reserva['id_paquete'])
        if not paquete:
            continue
        pid = paquete['id_paquete']
        if pid not in conteo:
            conteo[pid] = {
                'reservas': 0,
                'personas': 0,
                'ingresos': 0.0,
                'destino': 'Sin datos',
            }
        conteo[pid]['reservas'] += 1
        conteo[pid]['personas'] += reserva['personas']
        conteo[pid]['destino'] = paquete['destino']
        precio_unitario = reserva.get('precio_unitario')
        if precio_unitario is None:
            precio_unitario = paquete.get('precio')
        if conteo[pid]['ingresos'] is not None and precio_unitario is not None:
            try:
                conteo[pid]['ingresos'] += float(precio_unitario) * reserva['personas']
            except (TypeError, ValueError):
                conteo[pid]['ingresos'] = None

    ranking = []
    for pid, datos in conteo.items():
        ranking.append({
            'id': pid,
            'destino': datos['destino'],
            'reservas': datos['reservas'],
            'personas': datos['personas'],
            'ingresos': datos['ingresos'],
        })
    ranking.sort(key=lambda item: (-item['reservas'], -item['personas']))
    return ranking[:limite]


    ranking = []
    for pid, datos in conteo.items():
        ranking.append({
            'id': pid,
            'destino': datos['destino'],
            'reservas': datos['reservas'],
            'personas': datos['personas'],
            'ingresos': datos['ingresos'],
        })
    ranking.sort(key=lambda item: (-item['reservas'], -item['personas']))
    return ranking[:limite]


def buscar_cliente(id_cliente):
    for cliente in clientes:
        if cliente.get('id') == id_cliente:
            return cliente
    return None


def buscar_paquete(id_paquete):
    if id_paquete is None:
        return None
    for paquete in paquetes:
        if paquete.get('id_paquete') == id_paquete:
            return paquete
    return None


def buscar_paquete_por_destino(destino):
    for paquete in paquetes:
        if paquete.get('destino', '').lower() == (destino or '').lower():
            return paquete
    return None


def to_int(valor):
    try:
        return int(valor)
    except (TypeError, ValueError):
        return 0

