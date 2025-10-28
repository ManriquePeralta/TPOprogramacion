# importar el modulo json para manejar archivos JSON
import json

# funcion para autenticar al usuario
def autenticar_usuario(intentos=3):
    # Carga las credenciales desde el archivo JSON
    try:
        with open("usuarios.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    # Manejo de excepciones para errores comunes        
    except FileNotFoundError:
        print("\nNo se encontro el archivo de credenciales (usuarios.json).")
        return False
    except json.JSONDecodeError:
        print("\nEl archivo de credenciales esta dañado o tiene formato invalido.")
        return False
    # Extrae las credenciales de usuario y contrasena
    credenciales = [
        {"usuario": registro.get("usuario"), "contrasena": registro.get("contrasena")}
        for registro in datos.get("usuario", [])
        if registro.get("usuario") and registro.get("contrasena")
    ]

    restantes = intentos
    # Bucle para permitir multiples intentos de inicio de sesion
    while restantes > 0:
        # ingreso de usuario y contrasena
        try:
            print(f"\nIniciar sesion (intentos restantes: {restantes})")
            usuario = input("Usuario: ").strip()
            clave = input("Contrasena: ").strip()
            # Validacion de entradas vacias
            if not usuario or not clave:
                raise AssertionError("Usuario y contrasena no pueden estar vacios.")
            # Verificacion de credenciales
            encontrado = False
            for registro in credenciales:
                if registro["usuario"] == usuario and registro["contrasena"] == clave:
                    encontrado = True
                    break
            if encontrado:
                print("\nAcceso concedido.")
                return True

            restantes -= 1
            print("\nCredenciales invalidas. Intentelo nuevamente.")
        # Manejo de excepciones para errores durante la entrada
        except AssertionError as error:
            print(f"\n{error}")
        except KeyboardInterrupt:
            print("\n\nEjecucion interrumpida por el usuario.")
            return False
        except EOFError:
            print("\n\nEntrada finalizada (EOF).")
            return False
        except UnicodeDecodeError:
            print("\n\nError de decodificacion de la entrada.")
            return False

    print("\nSe agotaron los intentos de inicio de sesion.")
    return False
