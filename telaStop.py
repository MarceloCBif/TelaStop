import tkinter as tk
from PIL import ImageTk, Image


def calcularValorTotal(stopLossFixo, stop):
    valorTotal = (stopLossFixo / stop) * 100
    return valorTotal

def calcularGanho(valorTotal, porcentagemGanho):
    ganho = valorTotal * (porcentagemGanho / 100)
    return ganho

def calcular():
    stopLossFixo = float(entry_stop_loss_fixo.get())
    stop = float(entry_stop.get())
    porcentagemGanho = float(entry_porcentagem_ganho.get())

    valorTotal = calcularValorTotal(stopLossFixo, stop)
    ganho = calcularGanho(valorTotal, porcentagemGanho)

    label_valor_total["text"] = f"Valor Total da Margem: ${valorTotal:.2f}"
    label_ganho["text"] = f"Ganho: ${ganho:.2f}"
    label_stop["text"] = f"Stop: ${stopLossFixo:.2f}"

# Criação da janela
janela = tk.Tk()
janela.title("Calculadora de Trade - Value Capital")

#Logo
##logo = Image.open("logo.png")
#logo = logo.resize((50, 50), Image.ANTIALIAS)

#logo_tk = ImageTk.PhotoImage(logo)
# Labels
#label_logo = tk.Label(janela, image=logo_tk)
#label_logo.grid(row=0, column=0, padx=10, pady=5)
label_stop_loss_fixo = tk.Label(janela, text="Stop Loss Fixo (USD)")
label_stop_loss_fixo.grid(row=1, column=0, padx=10, pady=5)
label_stop = tk.Label(janela, text="Stop (%)")
label_stop.grid(row=2, column=0, padx=10, pady=5)
label_porcentagem_ganho = tk.Label(janela, text="Ganho (%)")
label_porcentagem_ganho.grid(row=3, column=0, padx=10, pady=5)




# Campos de entrada
entry_stop_loss_fixo = tk.Entry(janela)
entry_stop_loss_fixo.grid(row=1, column=1, padx=10, pady=5)
entry_stop = tk.Entry(janela)
entry_stop.grid(row=2, column=1, padx=10, pady=5)
entry_porcentagem_ganho = tk.Entry(janela)
entry_porcentagem_ganho.grid(row=3, column=1, padx=10, pady=5)

# Botão de cálculo
button_calcular = tk.Button(janela, text="Calcular", command=calcular)
button_calcular.grid(row=4, column=1, padx=10, pady=5)

# Resultados
label_valor_total = tk.Label(janela, text="Valor Total da Margem: $0.00")
label_valor_total.grid(row=5, column=0, padx=10, pady=5)
label_ganho = tk.Label(janela, text="Ganho: $0.00")
label_ganho.grid(row=6, column=0, padx=10, pady=5)
label_stop = tk.Label(janela, text="Stop: $0.00")
label_stop.grid(row=7, column=0, padx=10, pady=5)

# Loop principal da janela
janela.mainloop()
