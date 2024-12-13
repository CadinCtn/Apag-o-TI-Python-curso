import Conta as c
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

contas = {
    "1234": c.ContaBancaria("Cristyan"),
    "4321": c.ContaBancaria("Anderson")
}

#Criando funções
def sacar():
    valor = int(field_valor.get())
    conta = contas.get(field_conta.get())
    if(conta != None):
        if(conta.sacar(valor)):
            messagebox.showinfo("Sucesso", "Valor retirado com sucesso!")
        else:
            messagebox.showinfo("ERRO", "Saldo insuficiente!")
    else:
        messagebox.showinfo("ERRO", "Conta não encontrada")


def depositar():
    valor = int(field_valor.get())
    conta = contas.get(field_conta.get())
    if(conta != None):
        conta.depositar(valor)
        messagebox.showinfo("Sucesso", "Valor inserido com sucesso!")
    else:
        messagebox.showinfo("ERRO", "Conta não encontrada")

def consultar():
    conta = contas.get(field_conta.get())
    if(conta != None):
        messagebox.showinfo("Saldo", f"Saldo: {conta.get_saldo()}")
    else:
        messagebox.showinfo("ERRO", "Conta não encontrada")

def nova_conta():
    popup = tk.Toplevel(root)
    popup.title("Nova conta")
    popup.grab_set() # Força interação

    ttk.Label(popup, text="Numero da conta: ").grid(row=0, column=0)
    ttk.Label(popup, text="Titular: ").grid(row=0, column=1)
    
    entrada_numero = ttk.Entry(popup)
    entrada_numero.grid(row=1, column=0)

    entrada_titular = ttk.Entry(popup)
    entrada_titular.grid(row=1, column=1)

    def confirmar():
        numero = str(entrada_numero.get())
        for numero_conta in contas.keys():
            if numero_conta == numero:
                messagebox.showwarning("AVISO", "Conta já inserida!")
                return
        contas[numero] = c.ContaBancaria(entrada_titular.get())
        popup.destroy()
        messagebox.showinfo("Sucesso", "Conta cadastrada com sucesso")

    #Inserindo botões
    ttk.Button(popup, text="Cancelar", command=popup.destroy).grid(row=2, column=0) #Encerra tela
    ttk.Button(popup, text="Confirmar", command=confirmar).grid(row=2, column=1)


#Criando tela
root = tk.Tk()
root.title("Caixa Eletrônico")
root.geometry("700x500")

#Criando campos
ttk.Label(root, text="N° Conta: ").grid(row = 0, column = 0)
field_conta = tk.Entry(root)
field_conta.grid(row = 0, column = 1)

ttk.Label(root, text="Valor: ").grid(row = 1, column = 0 )
field_valor = tk.Entry(root)
field_valor.grid(row = 1, column = 1)

#Inserindo botões
ttk.Button(root, text="Depositar", command = depositar).grid(row=2, column=0)
ttk.Button(root, text="Sacar", command= sacar).grid(row=3, column=0)
ttk.Button(root, text="Consultar", command= consultar).grid(row=4, column=0)
ttk.Button(root, text="Inserir nova conta", command=nova_conta).grid(row=5, column=0)


root.mainloop()