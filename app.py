from flask import Flask, render_template, request, url_for
import mysql.connector as my
import os
import dotenv

dotenv.load_dotenv()

user = os.getenv('USER')
password = os.getenv('PASSWORD')
database = os.getenv('DATABASE')
host = os.getenv('HOST')

app = Flask(__name__)

def connectarBanco():
    conexao = my.connect(
        user=user,
        password=password,
        database=database,
        host=host
    )

    return conexao

connectarBanco()

# @app.route('/')
# def home():
#     return render_template('index.html')

@app.route('/', methods = ['GET','POST'])
def login():
    titulo = 'Página inicial'
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        print(f'Email: {email}, senha: {senha}')

        conexao = connectarBanco()
        cursor = conexao.cursor(dictionary=True)
        sql = 'select * from usuarios where email = %s'
        cursor.execute(sql,(email,))
        resultado = cursor.fetchone()
        print(resultado)

        if resultado:
            if senha == resultado['senha']:
                if resultado['tipo'] == 'cliente':
                    return render_template('cliente.html', usuario=resultado)
                elif resultado['tipo'] == 'admin':
                    return render_template('admin.html', usuario=resultado)
            else:
                print('Senha incorreta')

        else: 
            print('Errou o email')
            return render_template('login.html', titulo=titulo)
        
    
    return render_template('login.html', titulo=titulo)

if __name__ == '__main__':
    app.run(debug=True)