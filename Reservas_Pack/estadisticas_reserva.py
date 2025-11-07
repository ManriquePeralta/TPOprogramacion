# Estadisticas y reportes del modulo de reservas.

from Reservas_Pack.funciones_aux import reservas
from Clientes_Pack.funciones_aux import cargar_clientes_desde_archivo

def contar_personas_recursiva(reservas,largo=0):

    if len(reservas)==largo:
        return 0
    
    return reservas[largo][4]+contar_personas_recursiva(reservas,largo+1)
    
    


def estadisticas_reservas():
    # Genera reportes consolidados a partir de la lista de reservas.
    if not reservas:
        print("No hay reservas registradas para generar estadisticas.")
        return

    # Calcula cantidades basicas de reservas y personas involucradas.
    total = len(reservas)
    activas = sum(1 for reserva in reservas if reserva[5].lower() == 'activa')
    canceladas = sum(1 for reserva in reservas if reserva[5].lower() == 'cancelada')
    personas_total = contar_personas_recursiva(reservas)
    promedio_personas = personas_total / total if total else 0

    print("=== ESTADISTICAS DE RESERVAS ===")
    print("Reservas")
    print(f"  Total ..........: {total}")
    print(f"  Activas ........: {activas}")
    print(f"  Canceladas .....: {canceladas}")

    print("Personas")
    print(f"  Total Personas En Reservas: {personas_total}")
    print(f"  Promedio por reserva: {promedio_personas:.2f}")

    # Identifica clientes y destinos mas destacados.
    clientes_destacados = top_clientes(reservas)
    print()
    print("Clientes destacados")
    if clientes_destacados:
        indice = 1
        for data in clientes_destacados:
            print(f"  #{indice} {data['nombre']} (ID {data['id']}) - "
                f"{data['reservas']} reservas, {data['personas']} personas"
            )
            indice += 1
    else:
        print("  No hay clientes con reservas registradas.")

    destinos_destacados = top_destinos(reservas)
    print()
    print("Destinos favoritos")
    if destinos_destacados:
        indice = 1
        # Enumera los destinos con mayor cantidad de reservas.
        for data in destinos_destacados:
            print(
                f"  #{indice} {data['destino']} - {data['reservas']} reservas, {data['personas']} personas"
            )
            indice += 1
    else:
        print("  Sin destinos registrados.")

    print()

def top_clientes(reservas_normalizadas, limite=3):
    # Calcula los clientes con mayor cantidad de reservas y personas.
    conteo = {}
    for reserva in reservas_normalizadas:
        id_cliente = reserva[2]
        if id_cliente not in conteo:
            # Inicia el acumulador para el cliente cuando aparece por primera vez.
            conteo[id_cliente] = {'reservas': 0, 'personas': 0}
        conteo[id_cliente]['reservas'] += 1
        conteo[id_cliente]['personas'] += reserva[4]

    clientes_por_id = {cliente['id']: cliente for cliente in cargar_clientes_desde_archivo()}

    ranking = []
    for id_cliente, datos in conteo.items():
        cliente = clientes_por_id.get(id_cliente)
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
    # Determina los destinos mas reservados.
    conteo = recuento_reservas_x_destino(reservas_normalizadas)

    ranking = [
        {
            'destino': destino,
            'reservas': datos['reservas'],
            'personas': datos['personas'],
        }
        for destino, datos in conteo.items()
    ]
    ranking.sort(key=lambda item: (-item['reservas'], -item['personas'], item['destino']))
    return tuple(ranking[:limite])

def recuento_reservas_x_destino(reservas,cont=0):

    if len(reservas)==cont:
        
        return {}

    else:

        recuento=recuento_reservas_x_destino(reservas,cont+1)

        destino=reservas[cont][3]
        if  destino in recuento:

            recuento[destino]["reservas"]+=1
            recuento[destino]["personas"]+=reservas[cont][4]
        
        else:
            recuento[destino]={"reservas":1,"personas":reservas[cont][4]}

        return recuento
    
