import Conta as c
import tkinter as tk
import sv_ttk
from tkinter import ttk
from tkinter import messagebox

#Aplicando tema
sv_ttk.set_theme("dark")

#Contas cadastradas
contas = {}

#Funções
def criar_conta():
    popup = tk.Toplevel(root)
    popup.title("Nova conta")
    popup.geometry("380x100")
    popup.grab_set() # Força interação
    
    #Componentes
    ttk.Label(popup, text="Numero da conta: ").grid(row=0, column=0)
    ttk.Label(popup, text="Titular: ").grid(row=0, column=1)
    ttk.Label(popup, text="Saldo inicial: ").grid(row=0, column=2)
    
    entrada_numero = ttk.Entry(popup)
    entrada_numero.grid(row=1, column=0)

    entrada_titular = ttk.Entry(popup)
    entrada_titular.grid(row=1, column=1)

    entrada_saldo_inicial = ttk.Entry(popup)
    entrada_saldo_inicial.grid(row=1, column=2)


    def confirmar():
        numero = str(entrada_numero.get())
        for numero_conta in contas.keys():
            if numero_conta == numero:
                messagebox.showwarning("AVISO", "Conta já inserida!")
                return
        contas[numero] = c.Conta(numero, str(entrada_titular.get()), float(entrada_saldo_inicial.get()))
        popup.destroy()
        print(contas)
        messagebox.showinfo("Sucesso", "Conta cadastrada com sucesso")

    #Inserindo botões
    ttk.Button(popup, text="Cancelar", command=popup.destroy).grid(row=2, column=0) #Encerra tela
    ttk.Button(popup, text="Confirmar", command=confirmar).grid(row=2, column=1)

def tela_principal():
    root.withdraw() #Oculta tela
    mainwindow = tk.Toplevel()
    mainwindow.geometry("400x400")
    
    #Funções
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
        valor = float(field_valor.get())
        conta = contas.get(field_conta.get())
        if(conta != None):
            conta.depositar(valor)
            messagebox.showinfo("Sucesso", "Valor inserido com sucesso!")
        else:
            messagebox.showinfo("ERRO", "Conta não encontrada")

    def consultar():
        conta = contas.get(field_conta.get())
        if(conta != None):
            messagebox.showinfo("Saldo", f"Saldo: {conta.consultar_saldo()}")
        else:
            messagebox.showinfo("ERRO", "Conta não encontrada")

    #Criando campos
    ttk.Label(mainwindow, text="N° Conta: ").grid(row = 0, column = 0)
    field_conta = tk.Entry(mainwindow)
    field_conta.grid(row = 0, column = 1)

    ttk.Label(mainwindow, text="Valor: ").grid(row = 1, column = 0 )
    field_valor = tk.Entry(mainwindow)
    field_valor.grid(row = 1, column = 1)

    #Inserindo botões
    ttk.Button(mainwindow, text="Depositar", command = depositar).grid(row=2, column=0)
    ttk.Button(mainwindow, text="Sacar", command= sacar).grid(row=3, column=0)
    ttk.Button(mainwindow, text="Consultar", command= consultar).grid(row=4, column=0)
    ttk.Button(mainwindow, text="Inserir nova conta", command=criar_conta).grid(row=5, column=0)



def login():
    for conta in contas.values():
        numero = str(entry_conta.get())
        titular = str(entry_titular.get())
        if conta.get_numero() == numero and conta.get_titular() == titular:
            tela_principal()
        else:
            messagebox.showwarning("AVISO", "Conta não encontrada!")


#Componentes
root = tk.Tk() 
root.title("Sistema Gestão Bancária")
root.geometry("400x400")

#Campos para efetuar login
#Texto
ttk.Label(root, text="Número da Conta:").grid(row=0, column=0)
ttk.Label(root, text="Titular da conta:").grid(row=0, column=1)
#Entrada de dados
entry_conta = tk.Entry(root)
entry_titular = tk.Entry(root)
entry_conta.grid(row=1, column=0)
entry_titular.grid(row=1, column=1)

#Botões
ttk.Button(root, text="Entrar", command=login).grid(row=3, column=0)
ttk.Button(root, text="Criar nova conta", command=criar_conta).grid(row=4, column=0)

if __name__ == "__main__":
    root.mainloop()