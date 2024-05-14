#Aqui inportamos a biblioteca flask que ajuda-nos a trabalhar com web
from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

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

#Rota da pagina integrantes
@app.route('/integrantes')
def integrantes():
    return render_template('img.html')

#Rota da pagina do jogo
@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        numero = int(request.form['numero'])
        passos = torrehanoi(numero, 'A', 'B', 'C')
        return render_template('game.html', passos=passos)
    return render_template('game.html', passos=None)

#Rota da pagina da tabela
@app.route('/table', methods=['GET'])
def table():
    # Aqui você pode adicionar código para mostrar uma tabela, se necessário(vamos usar futuramente)
    nome = request.args.get('nome')
    movimentos = request.args.get('movimentos')

    # Render the 'table.html' page with the necessary data
    return render_template('table.html', nome=nome, movimentos=movimentos)

@app.route('/game', methods=['POST'])
def handle_game_submission():
    # Get the form data
    nome = request.form.get('CriaCampoNome')
    movimentos = request.form.get('CriaCampoMovimento')

    # Handle the form data as needed
    # For example, you could store it in a database or perform some other action

    # Redirect the user to the 'table.html' page with the necessary data
    return redirect(url_for('table', nome=nome, movimentos=movimentos))


#Inicia o servidor! Debug fica ativo para atualizar o site assim que mudar algo do codigo 
if __name__ == '__main__':
    app.run(debug=True)#-> Debug