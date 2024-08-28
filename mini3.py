## Manejo de Errores de Red: Simula errores comunes como fallos de conexión o interrupciones durante la comunicación (por ejemplo, desconectar manualmente un cliente mientras el servidor intenta enviar un mensaje). Luego, implementa un manejo de excepciones para que el servidor recupere el control de manera segura.

## ScripytErrorHandlingCliente

import socket

def error_handling(host='localhost', port=65432):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_socket.bind((host, port))
    
    server_socket.listen()
    print(f"Escuchando en {host}:{port}")
    
    while True:
        try:
            conn, client_address = server_socket.accept()
            print(f"Conexión establecida con {client_address}")
            
            try:
                msg = "Este es un mensaje del servidor."
                conn.sendall(msg.encode())
            except BrokenPipeError:
                print("Error: La conexión con el cliente se ha interrumpido.")
            except Exception as e:
                print(f"Error al enviar el mensaje: {e}")
            finally:
                conn.close()
        except KeyboardInterrupt:
            print("Servidor detenido por el usuario.")
            break
        except Exception as e:
            print(f"Error en el servidor: {e}")
    
    server_socket.close()

if __name__ == "__main__":
    error_handling()


## ScriptErrorHandlingServidor

import socket

def error_handling_client(host='localhost', port=65432):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect((host, port))
        
        data = client_socket.recv(1024)
        print(f"Mensaje del servidor: {data.decode()}")
    except ConnectionRefusedError:
        print("Error: No se pudo conectar al servidor. Asegúrate de que el servidor esté en ejecución.")
    except ConnectionResetError:
        print("Error: La conexión con el servidor se ha reiniciado.")
    except Exception as e:
        print(f"Error en el cliente: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    error_handling_client()
