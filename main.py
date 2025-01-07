'''testando o código em outra linguagem'''
import tkinter as tk
from tkinter import messagebox

def calcular_rank(vitorias, derrotas):
    saldo_vitorias = vitorias - derrotas
    if vitorias < 10:
        nivel = 'Ferro'
    elif 11 >= vitorias <= 20:
        nivel = 'Bronze'
    elif 21 >= vitorias <= 50:
        nivel = 'Prata'
    elif 51 >= vitorias <= 80:
        nivel = 'Ouro'
    elif 81 >= vitorias <= 90:
        nivel = 'Diamante'
    elif 91 >= vitorias <= 100:
        nivel = 'Lendário'
    else:
        nivel = 'Imortal'

    messagebox.showinfo("Resultado", f"O Herói tem de saldo de {saldo_vitorias} está no nível de {nivel}")

def on_calculate():
    try:
        vitorias = int(entry_vitorias.get())
        derrotas = int(entry_derrotas.get())
        calcular_rank(vitorias, derrotas)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Calculadora de Rank")

tk.Label(root, text="Vitórias:").grid(row=0, column=0)
entry_vitorias = tk.Entry(root)
entry_vitorias.grid(row=0, column=1)

tk.Label(root, text="Derrotas:").grid(row=1, column=0)
entry_derrotas = tk.Entry(root)
entry_derrotas.grid(row=1, column=1)

tk.Button(root, text="Calcular Rank", command=on_calculate).grid(row=2, columnspan=2)

root.mainloop()
