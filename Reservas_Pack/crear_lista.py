# guarda y lee las reservas en un archivo de texto.
# Archivo de texto donde se persisten las reservas.
ARCHIVO = "reservas.txt"

def get_precio_unitario(lista):

    if len(lista)==7:
        return lista[6]
    
    return 0


# Guarda todas las reservas en un archivo TXT.
def guardar_reservas_txt(reservas):
    print(reservas)
    # Escribe las reservas en el archivo especificado.
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        # Recorre cada reserva y escribe sus datos en una linea
        for r in reservas:
            linea = (
                f"{r[0]};{r[1]};{r[2]};"
                f"{r[3]};{r[4]};{r[5]};{get_precio_unitario(r)}"
            )
            f.write(linea + "\n")


# Lee todas las reservas desde un archivo TXT.
def leer_reservas_txt():
    reservas = []
    # Lee las reservas desde el archivo especificado
    try:
        with open("reservas.txt", "r", encoding="utf-8") as f:
            for linea in f:
                posicion = linea.strip().split(";")
                # Convierte cada linea en un diccionario con los campos esperados.
                reserva = [
                    int(posicion[0]), #"id_reserva"
                    int(posicion[1]), #"id_cliente"
                    int(posicion[2]), #"id_paquete"
                    posicion[3], #"destino"
                    int(posicion[4]), #"personas"
                    posicion[5], #"estado"
                    float(posicion[6]), #"precio_unitario"
                ]
                reservas.append(reserva)
    # Si ocurre un error al leer el archivo, se maneja la excepcion
    except FileNotFoundError:
        print("El archivo de reservas no se encontro.")
    return reservas
