# guarda y lee las reservas en un archivo de texto.
# Archivo de texto donde se persisten las reservas.
ARCHIVO = "reservas.txt"
# Guarda todas las reservas en un archivo TXT.
def guardar_reservas_txt(reservas):
    # Escribe las reservas en el archivo especificado.
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        # Recorre cada reserva y escribe sus datos en una linea
        for r in reservas:
            linea = f"{r['id_reserva']};{r['id_cliente']};{r['id_paquete']};{r['destino']};{r['personas']};{r['estado']};{r.get('precio_unitario',0)}"
            f.write(linea + "\n")

# Lee todas las reservas desde un archivo TXT.
def leer_reservas_txt():
    reservas = []
    # Lee las reservas desde el archivo especificado
    try:
        with open('reservas.txt', "r", encoding="utf-8") as f:
            for linea in f:
                posicion = linea.strip().split(";")
                # Convierte cada linea en un diccionario con los campos esperados.
                reserva = {
                    "id_reserva": int(posicion[0]),
                    "id_cliente": int(posicion[1]),
                    "id_paquete": int(posicion[2]),
                    "destino": posicion[3],
                    "personas": int(posicion[4]),
                    "estado": posicion[5],
                    "precio_unitario": float(posicion[6])
                }
                reservas.append(reserva)
    # Si ocurre un error al leer el archivo, se maneja la excepcion
    except FileNotFoundError:
        print("El archivo de reservas no se encontro.") 
    return reservas
