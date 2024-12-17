import socket
import threading
import main

HOST = '127.0.0.1'
PORT = 8080

class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST, PORT))
        print(f"Conectado ao servidor IPV4: {HOST} - PORTA: {PORT}")

    def start(self):
        threading.Thread(target=recive_messages, args=(self.client,), daemon=True).start()

    def send_message(self, message):
         self.client.send(message.encode())
    
    def recive_messages(self):
        while True:
            try:
                message = self.client.recv(1024).decode()
                
            except:
                self.client.close()
                break



def recive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            print("Conexão encerrada!")
            client.close()
            break


def send_messages(client):
    while True:
        try:
            if message != "":
                client.send(message.encode())
                message = ""
        except:
            break


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print(f"Conectado ao servidor IPV4: {HOST} - PORTA: {PORT}")

    threading.Thread(target=recive_messages, args=(client,), daemon=True).start()

    send_messages(client)


if __name__ == "__main__":
    main()