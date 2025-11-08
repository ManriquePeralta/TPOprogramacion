# Buscador de reservas por distintos criterios.

from Reservas_Pack.funciones_aux import (
    reservas,
    validar_id,
    reservas_por_cliente,
    busqueda_secuencial,
    busqueda_secuencial_reservas
)
from Reservas_Pack.mostrar_reservas import mostrar_detalle_reserva
from Clientes_Pack.funciones_aux import cargar_clientes_desde_archivo
from Paquetes_Pack.funciones_aux import cargar_paquete_desde_archivo


def buscar_reserva():
    # Gestiona el menu de busqueda para localizar reservas.
    while True:
        print("\n=== BUSCAR RESERVA ===")
        print("1. Por ID de reserva")
        print("2. Por ID de cliente")
        print("3. Por destino")
        print("0. Volver")
        opcion = input("Opcion: ").strip()

        if opcion == "0":
            return
        elif opcion == "1":
            # Consulta por un identificador unico de reserva.
            buscar_por_id()
        elif opcion == "2":
            # Muestra todas las reservas asociadas a un cliente.
            buscar_por_cliente()
        elif opcion == "3":
            # Filtra reservas por coincidencia con un destino.
            buscar_por_destino()
        else:
            print("Opcion invalida.")


def buscar_por_id():
    # Busca una reserva con un ID especifico y muestra un resumen.
    id_txt = input("Ingrese el ID de la reserva: ").strip()
    # Validar ID de la reserva
    if not validar_id(id_txt):
        print("ID invalido. Debe ser numerico positivo.")
        return
    
    reserva = busqueda_secuencial_reservas(reservas, 0, id_txt)
    
    
    if reserva==-1:
        print("no se encontro el id de la reserva")
        return

    if reserva is None:
        print("No se encontro una reserva con ese ID.")
        return
    
    # Mostrar resumen de la reserva encontrada
    imprimir_resumen_recursivo([reserva])

def buscar_por_cliente():
    # Reune todas las reservas asociadas a un cliente particular.
    id_txt = input("Ingrese el ID del cliente: ").strip()
    # Validar ID del cliente
    if not validar_id(id_txt):
        print("ID invalido. Debe ser numerico positivo.")
        return
    id_cliente = int(id_txt)
    # Obtener reservas del cliente
    coincidencias = reservas_por_cliente(reservas, id_cliente)
    if not coincidencias:
        print("El cliente no posee reservas registradas.")
        return
    
    # Mostrar reservas encontradas 
    clientes = cargar_clientes_desde_archivo()
    # Buscar nombre del cliente 
    cliente = busqueda_secuencial(clientes, "id", id_cliente)
    # Obtener nombre del cliente
    nombre = cliente["nombre"] if cliente else "Desconocido"
    # Mostrar las reservas del cliente 
    print(f"\nReservas del cliente {nombre}:")
    imprimir_resumen_recursivo(coincidencias)

def buscar_por_destino():
    # Filtra reservas que coinciden parcialmente con un destino.
    termino = input("Ingrese parte del destino a buscar: ").strip().lower()
    if not termino:
        print("Debe ingresar al menos una letra.")
        return

    coincidencias = []
    paquetes = cargar_paquete_desde_archivo()
    # Busca coincidencias comparando contra el destino del paquete.
    for reserva in reservas:
        # Obtener paquete asociado a la reserva 
        if termino in reserva[3].lower():
            print("coicidencia: ",termino, "destino: ",reserva[3])
            coincidencias.append(reserva)

    if not coincidencias:
        print("No se encontraron reservas para ese destino.")
        return

    print("\nReservas encontradas:")
    imprimir_resumen_recursivo(coincidencias)
    


def imprimir_resumen_recursivo(listado,cont=-99):
    # Imprime un resumen tabulado de las reservas 
    if cont==-1:
        encabezado = f"{'ID':<4} | {'Cliente':<18} | {'Destino':<24} | {'Personas':<8} | {'Estado':<10}"
        print(encabezado)
        print("-" * len(encabezado))
        clientes = cargar_clientes_desde_archivo()
      
        return clientes
    
    else:
        # Recursividad para imprimir cada reserva 
        if cont==-99:
            cont=len(listado)-1
        # Obtener lista de clientes para buscar nombres 
        clientes=imprimir_resumen_recursivo(listado,cont-1)
        # Imprimir reserva actual 
        reserva=listado[cont]
        # Buscar nombre del cliente 
        cliente = busqueda_secuencial(clientes, "id", reserva[1])
       
        nombre = cliente["nombre"] if cliente else "Desconocido"
        # Imprimir fila de la reserva 
        print(
            f"{reserva[0]:<4} | {nombre:<18} | {reserva[3]:<24} | {reserva[4]:<8} | {reserva[5].capitalize():<10}"
        )
        return clientes







