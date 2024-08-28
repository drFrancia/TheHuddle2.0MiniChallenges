## Script de Automatización para Instalación de Dependencias: Escribe un script Bash que instale una o dos dependencias comunes (como requests en Python) y luego ejecute un mensaje de éxito. Esto te permite practicar la automatización de tareas repetitivas en la terminal.

#!/bin/bash

function success_message {
    echo "Las dependencias se han instalado correctamente."
}

# Actualizar el índice de paquetes (para sistemas basados en Debian/Ubuntu)
echo "Actualizando el índice de paquetes..."
sudo apt-get update -y

# Instalar pip si no está instalado (para sistemas basados en Debian/Ubuntu)
echo "Verificando la instalación de pip..."
if ! command -v pip3 &> /dev/null; then
    echo "pip no encontrado. Instalando pip..."
    sudo apt-get install python3-pip -y
fi

# Instalar las dependencias
echo "Instalando dependencias..."
pip3 install requests

# Mostrar mensaje de éxito
success_message
