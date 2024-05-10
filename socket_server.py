import socket
 
server = socket.socket()            # создаем объект сокета сервера
hostname = socket.gethostname()     # получаем имя хоста локальной машины
port = 12345                        # устанавливаем порт сервера
server.bind((hostname, port))       # привязываем сокет сервера к хосту и порту
server.listen(5)                    # начинаем прослушиваение входящих подключений
 
print("Server running")
while True:
    con, _ = server.accept()     # принимаем клиента
    data = con.recv(1024)           # получаем данные от клиента
    message = data.decode('utf-8')         # преобразуем байты в строку
    print(f"Client sent: {message}")
    message = message[::-1]         # инвертируем строку
    con.send(message.encode('utf-8'))      # отправляем сообщение клиенту
    con.close()    