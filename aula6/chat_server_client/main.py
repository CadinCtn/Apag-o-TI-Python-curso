import socket
import threading
import tkinter as tk
import sv_ttk
from tkinter.scrolledtext import ScrolledText


HOST = '127.0.0.1'
PORT = 8080


class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST, PORT))
        print(f"Conectado ao servidor IPV4: {HOST} - PORTA: {PORT}")
        threading.Thread(target=self.recive_messages, daemon=True).start()

    def send_message(self, message):
        self.client.send(message.encode()) #Envia Mensagem

    def recive_messages(self):
        while True:
            try:
                message = self.client.recv(1024).decode()
                if message:
                    scroll_text.insert(tk.END, f"{message}\n") #Insere mensagem recebida na area de texto
            except:
                self.client.close()
                break


#Cria client
client = Client()

#Função do botão
def send_message():
    message = str(field_entry.get())
    if message:
        client.send_message(message)
        field_entry.delete(0, tk.END)

#Criando tela principal
main_screen = tk.Tk()
main_screen.title("Chat Server Client")

#Criando área de texto
scroll_text = ScrolledText(main_screen, height=30, width=100)

#Campo para digitar
field_entry = tk.Entry(main_screen)

#Botão para enviar mensagens
button = tk.Button(main_screen, text="Send", command=send_message)

#Posicionando componentes
scroll_text.pack(padx=10, pady=10)
field_entry.pack()
button.pack()


if __name__ == "__main__":
    main_screen.mainloop()
