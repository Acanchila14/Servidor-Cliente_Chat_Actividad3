# Servidor-Cliente_Chat_Actividad3
 Este código implementa una aplicación de chat basada en sockets en Python, compuesta por un cliente y un servidor.
Cliente:
•	Objetivo: El cliente conecta con el servidor para enviar y recibir mensajes de otros usuarios conectados.
•	Operación:
1.	Se crea un socket con socket.socket(socket.AF_INET, socket.SOCK_STREAM) que utiliza IPv4 (AF_INET) y TCP (SOCK_STREAM).
2.	El cliente se conecta al servidor ubicado en 'localhost' y el puerto 8080 con cliente.connect(('localhost', 8080)).
3.	Se ejecutan dos hilos concurrentes:
	Hilo de recepción: Utiliza la función recibir_mensajes, que recibe mensajes continuamente del servidor y los imprime.
	Hilo de envío: Utiliza la función enviar_mensajes, que permite al usuario escribir y enviar mensajes. El formato requerido es usuario_destino: mensaje.

Servidor:
•	Objetivo: El servidor gestiona las conexiones de los clientes y distribuye mensajes entre ellos.
Operación:
1.	Se crea un socket servidor que escucha conexiones en 'localhost' y el puerto 8080.
2.	Se ejecuta en un bucle infinito que acepta nuevas conexiones de clientes usando servidor.accept().
3.	Por cada cliente que se conecta, se lanza un hilo con la función manejar_cliente, que gestiona la interacción con ese cliente.
4.	Dentro de manejar_cliente, se registra a cada cliente por su nombre de usuario. Los mensajes se envían entre usuarios siguiendo el formato usuario_destino: mensaje.
5.	Si ocurre un error o un cliente se desconecta, se cierra la conexión y se elimina del diccionario clientes.

Manejo de mensajes:
•	El cliente(s) envía mensajes que se procesan en el servidor. El servidor verifica si el mensaje sigue el formato correcto (usuario_destino: mensaje). Si el usuario destinatario está conectado, se envía el mensaje; si no, se informa al remitente que el usuario no está disponible.



Montaje y herramientas utilizadas
1.	Python: El código está implementado en Python, utilizando dos bibliotecas estándar:
•	socket: Permite la creación de conexiones de red utilizando TCP.
•	threading: Permite manejar múltiples clientes simultáneamente mediante hilos.
2.	Ejecución:
•	Servidor: Se debe ejecutar primero en la máquina que actuará como servidor (por ejemplo, la misma que la del cliente en un entorno local).
•	Cliente: Después, se puede ejecutar el cliente desde una o más terminales para conectarse al servidor:

Aplicación y objetivo del aplicativo
•	Aplicación: Este código implementa un chat simple de varios clientes con capacidad para enviar mensajes privados entre ellos. Puede utilizarse como base para un sistema de comunicación más avanzado, como una plataforma de mensajería.
•	Objetivo: Facilitar la comunicación entre múltiples usuarios conectados a un servidor centralizado. Cada cliente puede enviar mensajes privados a otros usuarios conectados, lo que lo hace ideal para escenarios donde se requiere mensajería directa y en tiempo real, como en sistemas de soporte técnico o chats grupales privados.
