# Importando a biblioteca
from flask import Flask, url_for, redirect, request, render_template
from bd_simulado import get_verify
from bd_materia import get_notas, get_materias
# Inicializando o flask
app = Flask(__name__)


# criando uma rota para /
@app.route('/')
def principal():
    return render_template('index.html')

def get_resposta(chave, valor):
    resposta = get_verify(chave, valor)
    return resposta

def get_disciplinas(chave):
    resposta = get_materias(chave)
    return resposta

def get_mensao(chave):
    resposta = get_notas(chave)
    return resposta

# rota para login
@app.route('/login', methods=['GET', 'POST'])
def login():

    # verificando o metodo
    if request.method == 'POST':

        #requisição para quendo o metodo é POST
        login = request.form['login']
        senha = request.form['senha']

        # verificar a senha:
        resposta = get_resposta(login, senha)

        if resposta == True:

            disciplinas = get_disciplinas(login)
            mensao = get_mensao(login)

            return render_template('tabela.html', materia1=disciplinas[0], materia2=disciplinas[1], materia3 =disciplinas[2], m1_1=mensao[0][0][0], m2_1=mensao[1][0][0], m3_1=mensao[2][0][0]\
                                   ,m1_2=mensao[0][0][1], m2_2=mensao[1][0][1], m3_2=mensao[2][0][1], m1_3=mensao[0][0][2], m2_3=mensao[1][0][2], m3_3=mensao[2][0][2])


        else:
            return render_template('index.html', erro='Login/Senha incorretos')
    else:
        return render_template('index.html', erro='Método Incorreto, Use POST!')



# rodando o app
if __name__ == '__main__':
    app.run(debug=True)


