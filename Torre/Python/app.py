#Aqui inportamos a biblioteca flask que ajuda-nos a trabalhar com web
from flask import Flask, render_template, request, jsonify
import tkinter
from tkinter import *
from tkinter import ttk
app = Flask(__name__)


#Configuração do jogo
def torrehanoi(numero, inicio, auxiliar, fim):
    if numero == 1:
        return [('Muda o disco 1 da coluna {} para a coluna {}'.format(inicio, fim))]
    else:
        passos = torrehanoi(numero - 1, inicio, fim, auxiliar)
        passos.append('Muda o disco {} da coluna {} para a coluna {} \n'.format(numero, inicio, fim))
        passos.extend(torrehanoi(numero - 1, auxiliar, inicio, fim))
        return passos

#Rota da pagina inicial
@app.route('/')
def home():
    return render_template('home.html')

#Rota da pagina do jogo
@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        numero = int(request.form['numero'])
        passos = torrehanoi(numero, 'A', 'B', 'C')
        return render_template('game.html', passos=passos)
    return render_template('game.html', passos=None)

#Rota da pagina da tabela
@app.route('/table')
def table():
    # Aqui você pode adicionar código para mostrar uma tabela, se necessário(vamos usar futuramente)
    return render_template('table.html')

@app.route('/endgame', methods=['POST'])
def endgame():
    data = request.json
    if data.get('towers') and len(data['towers'][2]) == 5:

        def somar():
            valor1 = int(entry1.get())
            valor2 = int(entry2.get())
            resultado = valor1 + valor2
            label_resultado.config(text="Resultado: " + str(resultado))

        # interface gráfica
        janela = Tk()
        frame = ttk.Frame(janela, padding=10)
        frame.pack()
        janela.geometry("400x200")

        # instruções na tela
        ttk.Label(frame, text="Digite Seu nome").pack()
        label_resultado = ttk.Label(frame, text="Resultado: ")
        label_resultado.pack(side=tkinter.BOTTOM)


        # as duas caixas de entrada

        entry1 = ttk.Entry(frame)
        entry1.pack(pady=5)

        entry2 = ttk.Entry(frame)
        entry2.pack(pady=5)

        # botões de somar e quitar
        ttk.Button(frame, text="Quit", command=janela.destroy).pack(side=tkinter.LEFT, padx=10)
        ttk.Button(frame, text="Somar", command=somar).pack(side=tkinter.RIGHT, padx=10)

        janela.mainloop()


#Inicia o servidor! Debug fica ativo para atualizar o site assim que mudar algo do codigo 
if __name__ == '__main__':
    app.run(debug=True)#-> Debug