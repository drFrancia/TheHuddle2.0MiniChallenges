# Configuración Básica de Sockets: Implementa un servidor de sockets básico que escuche en un puerto específico y acepte conexiones de un solo cliente. El servidor debería enviar un mensaje de bienvenida al cliente y luego cerrar la conexión.

## ScriptServidor
import socket

def start_server(host='localhost', port=65432):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_socket.bind((host, port))
    
    server_socket.listen()
    print(f"Escuchando en {host}:{port}")
    
    connection, client_address = server_socket.accept()
    try:
        print(f"Conexión establecida con {client_address}")
        
        msg_bienvenida = "¡Bienvenido al servidor de sockets!"
        connection.sendall(msg_bienvenida.encode())
    finally:
        connection.close()

if __name__ == "__main__":
    start_server()

## ScriptCliente
import socket

def connect_to_server(host='localhost', port=65432):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    client_socket.connect((host, port))
    
    data = client_socket.recv(1024)
    print(f"Mensaje del servidor: {data.decode()}")
    
    client_socket.close()

if __name__ == "__main__":
    connect_to_server()
