import Conta as c
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

contas = {
    "1234": c.ContaBancaria("Cristyan"),
    "4321": c.ContaBancaria("Anderson")
}


root = tk.Tk()
root.title("Caixa Eletrônico")
root.geometry("700x500")

ttk.Label(root, text="N° Conta: ").grid(row = 0, column = 0)
field_conta = tk.Entry(root)
field_conta.grid(row = 0, column = 1)

ttk.Label(root, text="Valor: ").grid(row = 1, column = 0 )
field_valor = tk.Entry(root)
field_valor.grid(row = 1, column = 1)


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



ttk.Button(root, text="Depositar", command = depositar).grid(row=2, column=0)
ttk.Button(root, text="Sacar", command= sacar).grid(row=3, column=0)
ttk.Button(root, text="Consultar", command= consultar).grid(row=4, column=0)


root.mainloop()