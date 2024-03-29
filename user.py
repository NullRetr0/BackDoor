import socket

HOST = '127.0.0.1'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print('\033[31m' + """
  ____             _    ____                   
 | __ )  __ _  ___| | _|  _ \\  ___   ___  _ __ 
 |  _ \\ / _` |/ __| |/ / | | |/ _ \\ / _ \\| '__|
 | |_) | (_| | (__|   <| |_| | (_) | (_) | |   
 |____/ \\__,_|\\___|_|\\_\\____/ \\___/ \\___/|_|   
 """)

while True:
    command = input('\033[31m' + '//=> ' + '\033[32m')
    if command != '':
        if command.lower() == 'exit':
            break

        client.send(command.encode())

        response = client.recv(1024)

        try:
            decoded_response = response.decode()
            for line in decoded_response.splitlines():
                print(line)

        except UnicodeDecodeError:
            for line in response.splitlines():
                print(line.decode('windows-1251'))
client.close()
