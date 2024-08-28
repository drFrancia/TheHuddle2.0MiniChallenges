## Simulación de Logs Generados por un Servicio: Crea un script que genere logs simulados en formato JSON, incluyendo la fecha, nombre del servicio, nivel de severidad y un mensaje descriptivo. Haz que los logs se impriman en la terminal cada 5 segundos.

import json
import time
from datetime import datetime
import random

def generate_log():
    severity_levels = ["INFO", 
                        "WARNING", 
                        "ERROR", 
                        "CRITICAL"]
    
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "service_name": "ExampleService",
        "severity": random.choice(severity_levels),
        "message": "Mensaje de log random simulado."
    }
    
    return log_entry

def main():
    while True:
        log_entry = generate_log()
        print(json.dumps(log_entry, indent=4))
        
        time.sleep(5)

if __name__ == "__main__":
    main()
