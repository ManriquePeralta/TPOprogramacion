# Importaciones necesarias de otros modulos.
from Paquetes_Pack.mostrar_paquetes import mostrar_paquetes
from Clientes_Pack.mostrar_cliente import mostrar_clientes_activos
from Clientes_Pack.funciones_aux import (
    validar_id as validar_id_cliente,
    normalizar_estado as normalizar_estado_cliente,
    cargar_clientes_desde_archivo,
)
from Reservas_Pack.funciones_aux import (
    reservas,
    guardar_reservas,
    validar_id,
    validar_cantidad_personas,
    generar_nuevo_id,
    busqueda_secuencial,
    obtener_paquete_disponible,
    validar_cupos_disponibles,
)
from Paquetes_Pack.funciones_aux import (
    cargar_paquete_desde_archivo,
    guardar_paquete_en_archivo,
)

# Administra la creacion de una nueva reserva con validaciones.
def agregar_reserva():
    
    print("\n\n=== RESERVAR PAQUETE ===")

    # Muestra y carga los clientes disponibles antes de seleccionar uno.
    clientes_actuales = cargar_clientes_desde_archivo()
    paquetes = cargar_paquete_desde_archivo()
    if not clientes_actuales:
        print("No hay clientes cargados para realizar reservas.")
        return
    if not paquetes:
        print("No hay paquetes cargados para realizar reservas.")
        return

    mostrar_clientes_activos()
    cliente_seleccionado = None
    id_cliente = None

    while cliente_seleccionado is None:
        id_cliente_txt = input("\nIngrese el ID del cliente (0 para salir): ").strip()
        if id_cliente_txt == "0":
            print("Operacion cancelada.")
            return
        if not validar_id_cliente(id_cliente_txt):
            print("ID invalido. Debe ser un numero positivo.")
        else:
            id_cliente = int(id_cliente_txt)
            cliente = busqueda_secuencial(clientes_actuales, "id", id_cliente)
            if cliente is None:
                print("No existe un cliente con ese ID.")
            elif normalizar_estado_cliente(cliente["estado"]) != "activo":
                print("El cliente no esta activo. Seleccione otro cliente.")
            else:
                cliente_seleccionado = cliente

    mostrar_paquetes()
    paquete_seleccionado = None
    id_paquete = None

    while paquete_seleccionado is None:
        id_paquete_txt = input("\nIngrese el ID del paquete a reservar (0 para salir): ").strip()
        if id_paquete_txt == "0":
            print("Operacion cancelada.")
            return
        if not validar_id(id_paquete_txt):
            print("ID invalido. Debe ser un numero positivo.")
        else:
            id_paquete = int(id_paquete_txt)
            paquete, error = obtener_paquete_disponible(paquetes, id_paquete)
            if error:
                print(error)
            else:
                paquete_seleccionado = paquete

    personas = 0
    cantidad_txt = input("Cantidad de personas: ").strip()
    entrada_valida = False
    while entrada_valida is False:
        if not validar_cantidad_personas(cantidad_txt):
            print("La cantidad debe ser un numero entero mayor a 0.")
            cantidad_txt = input("Cantidad de personas: ").strip()
        else:
            personas = int(cantidad_txt)
            if not validar_cupos_disponibles(paquete_seleccionado, personas):
                print("La cantidad supera los cupos disponibles.")
                cantidad_txt = input("Cantidad de personas: ").strip()
            else:
                entrada_valida = True

    # Genera un identificador unico para la nueva reserva.
    nuevo_id = generar_nuevo_id(reservas)
    nueva_reserva = [
        nuevo_id,#"id_reserva"
        id_cliente, #"id_cliente"
        id_paquete, #"id_paquete"
        paquete_seleccionado["destino"], #"destino"
        personas, #"personas"
        "activa",#"estado"
        paquete_seleccionado.get("precio"), #"precio_unitario"
    ]
    # Agrega la reserva a la lista global y ajusta los cupos disponibles.
    reservas.append(nueva_reserva)
    paquete_seleccionado["cupos"] -= personas
    
    # Guardar cambios en TXT
    guardar_reservas()

    nombre_cliente = cliente_seleccionado["nombre"]
    print(f"Reserva creada con exito. ID: {nuevo_id} (Cliente: {nombre_cliente}).")

    guardar_paquete_en_archivo(paquetes)
