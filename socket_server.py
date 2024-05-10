import socket
 
server = socket.socket()            # ������� ������ ������ �������
hostname = socket.gethostname()     # �������� ��� ����� ��������� ������
port = 12345                        # ������������� ���� �������
server.bind((hostname, port))       # ����������� ����� ������� � ����� � �����
server.listen(5)                    # �������� �������������� �������� �����������
 
print("Server running")
while True:
    con, _ = server.accept()     # ��������� �������
    data = con.recv(1024)           # �������� ������ �� �������
    message = data.decode('utf-8')         # ����������� ����� � ������
    print(f"Client sent: {message}")
    message = message[::-1]         # ����������� ������
    con.send(message.encode('utf-8'))      # ���������� ��������� �������
    con.close()    