## Uso de Argumentos en la CLI: Crea un script simple en Python o Bash que acepte un argumento de ubicación desde la línea de comandos e imprima un mensaje de bienvenida personalizado para esa ubicación (ejemplo: "Bienvenido a [Ciudad]").

import sys

def main():
    if len(sys.argv) != 2:
        print("Uso: python welcome.py <ubicación>")
        sys.exit(1)

    location = sys.argv[1]
    print(f"¡Bienvenido a {location}!")

if __name__ == "__main__":
    main()
