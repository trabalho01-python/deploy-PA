from flask import Flask, render_template, request, url_for
import mysql.connector as my
import os
import dotenv

dotenv.load_dotenv()

user = os.getenv('USER')
password = os.getenv('PASSWORD')
database = os.getenv('DATABASE')
host = os.getenv('HOST')

def connectarBanco():
    conexao = my.connect(
        user=user,
        password=password,
        database=database,
        host=host
    )

    return conexao

connectarBanco()

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def index():
    titulo = 'Página inicial'
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        print(f'Email: {email}, senha: {senha}')

        return render_template('index.html', titulo=titulo)
    
    return render_template('index.html', titulo=titulo)

if __name__ == '__main__':
    app.run(debug=True)