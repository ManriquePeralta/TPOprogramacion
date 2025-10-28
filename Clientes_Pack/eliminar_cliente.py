# importa las todas las funciones necesarias
from Clientes_Pack.funciones_aux import (
    validar_id,
    buscar_indice_por_id,
    normalizar_estado,
    formatear_estado,
    cargar_clientes_desde_archivo,
    guardar_clientes_en_archivo,
)
from Clientes_Pack.mostrar_cliente import mostrar_clientes
from Reservas_Pack.funciones_aux import reservas
from Reservas_Pack.funciones_aux import normalizar_estado as normalizar_estado_reserva
from Paquetes_Pack.funciones_aux import (
    cargar_paquete_desde_archivo,
    guardar_paquete_en_archivo,
)

# Elimina (inactiva) un cliente y cancela sus reservas activas.
def eliminar_cliente():
    print("\n=== ELIMINAR CLIENTE ===")
    # Muestra el listado de clientes
    listado = mostrar_clientes()
    if not listado:
        return
    # carga los datos necesarios
    clientes_actuales = cargar_clientes_desde_archivo()
    paquetes = cargar_paquete_desde_archivo()
    # solicita el ID del cliente a inactivar
    id_cliente = input("\nIngrese el ID del cliente a inactivar (0 para salir): ").strip()
    # permite salir de la operacion
    if id_cliente == "0":
        print("Operacion cancelada. No se modifico ningun cliente.")
        return
    # valida el ID ingresado
    while not validar_id(id_cliente):
        print("ID invalido. Debe ser un numero positivo.")
        id_cliente = input("Ingrese el ID del cliente a inactivar (0 para salir): ").strip()
        if id_cliente == "0":
            print("Operacion cancelada. No se modifico ningun cliente.")
            return
    # convierte el ID a entero y busca el cliente
    id_cliente = int(id_cliente)
    indice = buscar_indice_por_id(clientes_actuales, id_cliente)
    if indice == -1:
        print(f"No se encontro un cliente con ID {id_cliente}.")
        return
    # obtiene el cliente a inactivar
    cliente = clientes_actuales[indice]
    estado_actual = normalizar_estado(cliente.get("estado", ""))
    # verifica si ya esta inactivo
    if estado_actual == "inactivo":
        print(f"El cliente {cliente['nombre']} ya se encuentra inactivo.")
        return
    # solicita confirmacion para inactivar
    confirmar = input(f"Confirma marcar como inactivo a {cliente['nombre']}? (s/n): ").strip().lower()
    while confirmar not in ("s", "n"):
        confirmar = input("Respuesta invalida. Confirma marcar como inactivo? (s/n): ").strip().lower()
    if confirmar == "n":
        print("Operacion cancelada por el usuario.")
        return
    # marca el cliente como inactivo
    cliente["estado"] = "inactivo"
    # cancela las reservas asociadas al cliente
    canceladas = 0
    total_reservas = len(reservas)
    indice_reserva = 0
    # recorre las reservas para cancelar las asociadas al cliente
    while indice_reserva < total_reservas:
        reserva = reservas[indice_reserva]
        # verifica si la reserva pertenece al cliente
        if type(reserva) is dict and reserva.get("id_cliente") == id_cliente:
            paquete = buscar_paquete(paquetes, reserva.get("id_paquete"))
            estado_reserva = normalizar_estado_reserva(reserva.get("estado", ""))
            # si la reserva esta activa, libera los cupos en el paquete
            if estado_reserva == "activa":
                if paquete is not None:
                    paquete["cupos"] += reserva.get("personas", 0)
            # guarda el precio unitario si no esta guardado
            if paquete is not None:
                precio_guardado = reserva.get("precio_unitario")
                if precio_guardado is None:
                    reserva["precio_unitario"] = paquete.get("precio")

            reserva["estado"] = "cancelada"
            canceladas += 1
        indice_reserva += 1
    if canceladas:
        print(f"Reservas asociadas canceladas: {canceladas}")

    # guarda los cambios en los archivos
    if guardar_clientes_en_archivo(clientes_actuales):
        print(f"El cliente {cliente['nombre']} ahora figura con estado {formatear_estado(cliente['estado'])}.")
    else:
        print("No se pudo actualizar el estado del cliente en el archivo.")
    
    if not guardar_paquete_en_archivo(paquetes):
        print("No se pudieron guardar los cambios en los paquetes.")

# Busca un paquete por su ID y lo devuelve.
def buscar_paquete(paquetes, id_paquete):
    # Recorre la lista de paquetes
    for paquete in paquetes:
        if paquete["id_paquete"] == id_paquete:
            return paquete
    return None
