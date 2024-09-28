import socket
import threading

# Diccionario para almacenar los clientes conectados
clientes = {}

# Función para manejar las conexiones de los clientes
def manejar_cliente(conexion, direccion):
    try:
        # Registrar al usuario con su nombre de usuario
        conexion.send("Por favor, ingresa tu nombre de usuario: ".encode('utf-8'))
        nombre_usuario = conexion.recv(1024).decode('utf-8').strip()

        # Verificar si el usuario ya existe
        if nombre_usuario in clientes:
            conexion.send("Este nombre de usuario ya está en uso. Desconectando...".encode('utf-8'))
            conexion.close()
            return

        # Agregar al cliente a la lista de clientes
        clientes[nombre_usuario] = conexion
        print(f"{nombre_usuario} se ha conectado desde {direccion}")

        conexion.send(f"Bienvenido al chat, {nombre_usuario}! Puedes enviar mensajes usando el formato 'usuario_destino: mensaje'.\n".encode('utf-8'))

        while True:
            try:
                mensaje = conexion.recv(1024).decode('utf-8').strip()
                if mensaje:
                    # Verificar si el mensaje está en el formato correcto
                    if ":" in mensaje:
                        usuario_destino, contenido_mensaje = mensaje.split(":", 1)
                        enviar_a_usuario(nombre_usuario, usuario_destino.strip(), contenido_mensaje.strip())
                    else:
                        conexion.send("Formato incorrecto. Usa 'usuario_destino: mensaje'.\n".encode('utf-8'))
                else:
                    # Si no hay mensaje, desconectar al usuario
                    eliminar_cliente(nombre_usuario)
                    break
            except ConnectionResetError:
                print(f"{nombre_usuario} se ha desconectado abruptamente.")
                eliminar_cliente(nombre_usuario)
                break
            except Exception as e:
                print(f"Error manejando el mensaje de {nombre_usuario}: {str(e)}")
                eliminar_cliente(nombre_usuario)
                break
    except Exception as e:
        print(f"Error durante el registro del cliente: {str(e)}")
        conexion.close()

# Función para enviar el mensaje a un usuario específico
def enviar_a_usuario(nombre_remitente, usuario_destino, mensaje):
    if usuario_destino in clientes:
        try:
            mensaje_modificado = f"{nombre_remitente}: {mensaje}"
            clientes[usuario_destino].send(mensaje_modificado.encode('utf-8'))
        except Exception as e:
            print(f"Error enviando mensaje a {usuario_destino}: {str(e)}")
            eliminar_cliente(usuario_destino)
    else:
        if nombre_remitente in clientes:
            clientes[nombre_remitente].send(f"El usuario {usuario_destino} no está conectado.\n".encode('utf-8'))

# Función para eliminar a un cliente de la lista y cerrar la conexión
def eliminar_cliente(nombre_usuario):
    if nombre_usuario in clientes:
        print(f"{nombre_usuario} se ha desconectado.")
        clientes[nombre_usuario].close()
        del clientes[nombre_usuario]

# Configurar el servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('localhost', 8080))
servidor.listen()

print("Servidor de chat iniciado y esperando conexiones...")

# Aceptar conexiones continuamente
while True:
    conexion, direccion = servidor.accept()
    thread = threading.Thread(target=manejar_cliente, args=(conexion, direccion))
    thread.start()
