# Estadisticas y reportes del modulo de reservas.

from Reservas_Pack.funciones_aux import reservas
from Clientes_Pack.funciones_aux import cargar_clientes_desde_archivo


def contar_personas_recursiva(reservas,largo=0):
    # Cuenta recursivamente la cantidad de personas en las reservas

    # Si no hay reservas, retorna 0 
    if len(reservas)==largo:
        return 0
    # Suma la cantidad de personas en la reserva actual y llama a la siguiente reserva
    return contar_personas_recursiva(reservas,largo+1)



def estadisticas_reservas():
    # Genera reportes consolidados a partir de la lista de reservas.
    if not reservas:
        print("No hay reservas registradas para generar estadisticas.")
        return

    # Calcula cantidades basicas de reservas y personas involucradas.
    total = len(reservas)
    # Cuentas reservas activas y canceladas
    activas = sum(1 for reserva in reservas if reserva[5].lower() == 'activa')
    canceladas = sum(1 for reserva in reservas if reserva[5].lower() == 'cancelada')
    # Cuenta total de personas en las reservas 
    personas_total = contar_personas_recursiva(reservas)
    # Calcula el promedio de personas por reserva 
    promedio_personas = personas_total / total if total else 0

    print("=== ESTADISTICAS DE RESERVAS ===")
    print("Reservas")
    print(f"  Total ..........: {total}")
    print(f"  Activas ........: {activas}")
    print(f"  Canceladas .....: {canceladas}")

    print("Personas")
    print(f"  Total Personas En Reservas..........: {personas_total}")
    print(f"  Promedio por reserva: {promedio_personas:.2f}")

    # Identifica clientes y destinos mas destacados.
    clientes_destacados = top_clientes(reservas)
    print()
    print("Clientes destacados")
    if clientes_destacados:
        indice = 1
        # Enumera los clientes con mayor cantidad de reservas 
        for data in clientes_destacados:
            # Muestra los datos del cliente destacado 
            print(f"  #{indice} {data['nombre']} (ID {data['id']}) - "
                f"{data['reservas']} reservas, {data['personas']} personas"
            )
            indice += 1
    else:
        print("  No hay clientes con reservas registradas.")
    # Identifica los destinos mas populares 
    destinos_destacados = top_destinos(reservas)
    print()
    print("Destinos favoritos")
    if destinos_destacados:
        indice = 1
        # Enumera los destinos con mayor cantidad de reservas.
        for data in destinos_destacados:
            # Muestra los datos del destino destacado
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
        # Extrae el ID del cliente de la reserva 
        id_cliente = reserva[2]
        if id_cliente not in conteo:
            # Inicia el acumulador para el cliente cuando aparece por primera vez.
            conteo[id_cliente] = {'reservas': 0, 'personas': 0}
        conteo[id_cliente]['reservas'] += 1
        conteo[id_cliente]['personas'] += reserva[4]
    # Carga los datos de los clientes para obtener nombres y otros detalles 
    clientes_por_id = {cliente['id']: cliente for cliente in cargar_clientes_desde_archivo()}

    ranking = []
    # Construye la lista de clientes con sus datos y conteos 
    for id_cliente, datos in conteo.items():
        # Buscar los datos del cliente por su ID 
        cliente = clientes_por_id.get(id_cliente)
        if not cliente:
            continue
        # Agrega el cliente al ranking con sus datos
        ranking.append({
            'id': cliente['id'],
            'nombre': cliente['nombre'],
            'reservas': datos['reservas'],
            'personas': datos['personas'],
        })
    # Ordena el ranking por cantidad de reservas, personas, y nombre del cliente 
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
    # Ordena el ranking por cantidada de resrevas, personas y nombre del destino
    ranking.sort(key=lambda item: (-item['reservas'], -item['personas'], item['destino']))
    # Retorna los destinos mas populares hasta el limite especificado 
    return tuple(ranking[:limite])

def recuento_reservas_x_destino(reservas,cont=0):
    # Cuenta recursivamente las reservas y personas por destino
    if len(reservas)==cont:
        # Si no hay mas reservas, retorna un diccionario vacio 
        return {}

    else:
        # Llama la siguiente reserva
        recuento={"mar del plata":{"reservas":1,"personas":5}} 
        # Obtiene el destino de la reserva actual
        destino=reservas[cont][3]
        if  destino in recuento:
            # Actualiza el conteo existente para el destino 
            recuento[destino]["reservas"]+=1
            recuento[destino]["personas"]+=reservas[cont][4]
        
        else:
            # Inicia el conteo para un nuevo destino
            recuento[destino]={"reservas":1,"personas":reservas[cont][4]}
            {"mar del plata":{"reservas":1,"personas":5},"villa gessel":{"reservas":1,"personas":12}} 
        return recuento

