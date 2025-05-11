import pyodbc
from flask import Flask, request, jsonify

app = Flask(__name__)

# Dados da conexão
server = 'DESKTOP-0I1EGPO'        
database = 'Loginsenky'            
username = 'junindev'       
password = '325722'         

# Rota para cadastro de usuário
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    dados = request.json
    nome = dados.get('nome')
    email = dados.get('email')
    usuario = dados.get('usuario')
    senha = dados.get('senha')

    try:
        conexao = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={'DESKTOP-0I1EGPO'};'
            f'DATABASE={'Loginsenky'};'
            f'UID={'junindev'};'
            f'PWD={'325722'}'
        )
        cursor = conexao.cursor()

        # Inserir usuário vindo do front-end
        sql = "INSERT INTO Login (nome, email, usuario, senha) VALUES (?, ?, ?, ?)"
        valores = (nome, email, usuario, senha)
        cursor.execute(sql, valores)
        conexao.commit()

        return jsonify({"mensagem": "Usuário inserido com sucesso!"})

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

    finally:
        cursor.close()
        conexao.close()

if __name__ == '__main__':
    app.run(debug=True)