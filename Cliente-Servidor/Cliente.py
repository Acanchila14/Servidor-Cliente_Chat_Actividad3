import socket
import threading

# Función para recibir mensajes del servidor
def recibir_mensajes(cliente):
    while True:
        try:
            mensaje = cliente.recv(1024).decode('utf-8')
            if mensaje:
                print(mensaje)
        except:
            print("Error al recibir el mensaje.")
            cliente.close()
            break

# Función para enviar mensajes al servidor
def enviar_mensajes(cliente):
    while True:
        mensaje = input("")  # Enviar en formato 'usuario_destino: mensaje'
        cliente.send(mensaje.encode('utf-8'))

# Configurar el cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('localhost', 8080))

# Crear un hilo para escuchar los mensajes del servidor
recibir_thread = threading.Thread(target=recibir_mensajes, args=(cliente,))
recibir_thread.start()

# Crear un hilo para enviar mensajes al servidor
enviar_thread = threading.Thread(target=enviar_mensajes, args=(cliente,))
enviar_thread.start()
