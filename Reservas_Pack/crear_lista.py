# guarda y lee las reservas en un archivo de texto.
# Archivo de texto donde se persisten las reservas.
ARCHIVO = "reservas.txt"

# Guarda todas las reservas en un archivo TXT.
def guardar_reservas_txt(reservas):
    
   
    # Escribe las reservas en el archivo especificado.
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        # Recorre cada reserva y escribe sus datos en una linea
        for reserva in reservas:
            
            linea = (
                f"{reserva[0]};{reserva[1]};{reserva[2]};"
                f"{reserva[3]};{reserva[4]};{reserva[5]};{reserva[6]}"
            )
            archivo.write(linea + "\n")


# Lee todas las reservas desde un archivo TXT.
def leer_reservas_txt():
    reservas = []
    # Lee las reservas desde el archivo especificado
    try:
        with open("reservas.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
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
    
    ## AGREGAR EXCEPCION
    except ValueError:
        print("se trato de convertir un valor erroñamente")

    return reservas


