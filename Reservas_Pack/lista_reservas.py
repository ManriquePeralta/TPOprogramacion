"""Datos iniciales del modulo de reservas."""

# Cada reserva se representa con un diccionario para facilitar el acceso por clave.
# Campos: id_reserva, id_cliente, id_paquete, destino, personas, estado
reservas = [
    {"id_reserva": 1, "id_cliente": 1, "id_paquete": 1, "destino": "Bariloche", "personas": 2, "estado": "activa", "precio_unitario": 150000},
    {"id_reserva": 2, "id_cliente": 2, "id_paquete": 3, "destino": "Salta", "personas": 3, "estado": "activa", "precio_unitario": 95000},
    {"id_reserva": 3, "id_cliente": 3, "id_paquete": 2, "destino": "Cataratas del Iguazu", "personas": 1, "estado": "cancelada", "precio_unitario": 120000},
]
