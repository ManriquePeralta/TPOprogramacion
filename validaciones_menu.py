# validaciones_menu.py
def ingresar_numero(mensaje="Opcion: ", minimo=0, maximo=3):
    # Bucle para solicitar y validar la entrada del usuario   
    try:
        # Solicitar entrada al usuario
        entrada = input(mensaje).strip()
        # Validar que la entrada sea un numero entero dentro del rango especificado
        assert len(entrada) == 1 or not entrada.startswith("0"), "No se permiten ceros a la izquierda."
        opcion = int(entrada)              
        assert minimo <= opcion <= maximo, f"Error, ingrese un numero entre {minimo} y {maximo}."  
        return opcion

    # Manejo de excepciones para errores comunes
    except AssertionError as error: # Captura errores de asercion
        print(f"\n{error}")
    except ValueError as error: # Captura errores de valor
        print(f"\n{error}")
        print("Error valor, ingrese un numero entero.")
    except KeyboardInterrupt: # Captura Ctrl+C
        print("\nEjecución interrumpida por el usuario.")
    except EOFError: # Captura Ctrl+Z y enter
        print("\nEntrada finalizada (EOF).")
    except UnicodeDecodeError: # Captura errores de decodificacion
        print("\nError de decodificación de la entrada.")


