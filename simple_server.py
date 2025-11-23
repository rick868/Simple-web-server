import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(1)
print("Access the webpage in localhost:8080")

while True:
    client_socket, address = server_socket.accept()
    request = client_socket.recv(1024).decode()

    response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: 125\r\nServer: nginx/1.18.0\r\n<h1>This is a simple web server</h1>"
    client_socket.sendall(response.encode())
    client_socket.close()