import socket
import subprocess

HOST = '127.0.0.1'
PORT = 12345

while True:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    conn, addr = server.accept()

    try:
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break

            w = list(data.split())

            if "download" in w:
                with open(w[1], 'rb') as file:
                    data = file.read(1024)
                    while data:
                        conn.send(data)
                        data = file.read(1024)
            else:
                cmd = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                output, error = cmd.communicate()
                if output:

                    if output == b'' and error == b'':
                        conn.send(b'Success')
                    else:
                        conn.send(output)
                else:
                    if output == b'' and error == b'':
                        conn.send(b'Success')
                    else:
                        conn.send(error)
    except ConnectionResetError:
        conn.close()
