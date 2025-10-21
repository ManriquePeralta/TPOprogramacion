"""Manejo de credenciales de acceso al programa."""
from lista_usuarios import CREDENCIALES

""" Solicita usuario y contrasena hasta que se ingresen credenciales validas
    o se agoten los intentos. Retorna True si la autenticacion tiene exito.
    """
def autenticar_usuario(intentos=3):
    restantes = intentos
    while restantes > 0:
        try:
            print(f"\nIniciar sesion (intentos restantes: {restantes})")
            usuario = input("Usuario: ").strip()
            clave = input("Contrasena: ").strip()

            if not usuario or not clave:
                raise AssertionError("Usuario y contrasena no pueden estar vacios.")

            usuarios_registrados = CREDENCIALES.get("usuario", [])

            credenciales = {
                (registro.get("usuario"), registro.get("contrasena"))
                for registro in usuarios_registrados
            }

            if (usuario, clave) in credenciales:
                print("\nAcceso concedido.")
                return True

            restantes -= 1
            print("\nCredenciales invalidas. Intentelo nuevamente.")

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
