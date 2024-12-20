from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import tkinter
from tkinter import ttk

app = Flask(__name__)
#app.config['SECRET_KEY']
socketio = SocketIO(app, cors_allowed_origins='*')
CORS(app)

#Base de dados local
clients = {} # Lista id(nome) dos clientes
messages = []# Lista mensagens do chat

#Simula banco de dados
users = []

#Rota CRUD: criar e listar usuários
@app.route('/users', methods=['GET', 'POST']) 
def manege_users():
    #POST
    #Salva a informação na lista users com o formato json
    if request.method == 'POST':
        data = request.get_json
        users.append(data)
        return jsonify({"message": "Usuário cadastrado com sucesso!"}), 201
    #GET
    #Retorna para o client toda a lista de users no formato json
    return jsonify(users), 200

@socketio.on('connect')
def handle_connect():
    client_id = request.sid
    clients[client_id] = "User00"
    emit('update_clients', list(clients.values()), broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    client_id = request.sid
    if client_id in clients:
        clients.pop(client_id)
        emit("update_clients", list(clients.values()), broadcast=True)

@socketio.on('set_username')
def set_username(data):
    client_id = request.sid
    clients[client_id] = data['username']
    emit('update_clients', list(clients.values()), broadcast=True)

@socketio.on('send_message')
def handle_send_message(data):
    messages.append(data)
    emit('receive_message', data, broadcast=True)


if __name__ == "__main__":
    socketio.run(app, debug=True)    