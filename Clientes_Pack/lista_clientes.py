"""Datos base del modulo de clientes."""

# Estructura de cada cliente (dict):
# {
#     "id": int,
#     "nombre": str,
#     "dni": str (8 digitos),
#     "email": str,
#     "estado": str (activo/inactivo/suspendido)
# }
clientes = [
    {"id": 1, "nombre": "Juan Perez", "dni": "12345678", "email": "juan.p@gmail.com", "estado": "activo"},
    {"id": 2, "nombre": "Maria Gomez", "dni": "87654321", "email": "maria.gomez@hotmail.com", "estado": "inactivo"},
    {"id": 3, "nombre": "Pedro Lopez", "dni": "45678912", "email": "pedro.lopez@yahoo.com", "estado": "activo"},
    {"id": 4, "nombre": "Sofia Martinez", "dni": "32165498", "email": "sofia.martinez@example.com", "estado": "activo"},
    {"id": 5, "nombre": "Luciano Ortega", "dni": "78912345", "email": "luciano.ortega@example.com", "estado": "suspendido"},
]
