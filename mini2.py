## Cliente Simple de Chat: Desarrolla un cliente que se conecte a un servidor de sockets y permita al usuario enviar un mensaje simple a través de la terminal. Una vez enviado, el cliente debería cerrar la conexión.

## ScriptChatCliente
import socket

def chat_client(host='localhost', port=65432):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    client_socket.connect((host, port))
    
    try:
        msg = input("Escribe tu mensaje: ")
        
        client_socket.sendall(msg.encode())
    finally:
        client_socket.close()

if __name__ == "__main__":
    chat_client()


## ScrippChatServer

import socket

def chat_server(host='localhost', port=65432):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_socket.bind((host, port))
    
    server_socket.listen()
    print(f"Escuchando en {host}:{port}")
    
    conn, client_address = server_socket.accept()
    try:
        print(f"Conexión establecida con {client_address}")
        
        data = conn.recv(1024)
        print(f"Mensaje recibido: {data.decode()}")
    finally:
        conn.close()

if __name__ == "__main__":
    chat_server()

