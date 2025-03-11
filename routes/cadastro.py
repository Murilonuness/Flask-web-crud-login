from flask import Blueprint, render_template, redirect, request
from werkzeug.security import generate_password_hash
import mysql.connector

cadastro_route = Blueprint('cadastro', __name__)

@cadastro_route.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@cadastro_route.route('/inserir_user', methods=['POST'])
def inserir_user():
    connection = mysql.connector.connect(
        host='localhost', database='users_health', user='root', password=''
    )

    nome = request.form.get('nome')
    segundoNome = request.form.get('segundoNome')
    email = request.form.get('email')
    senhaform = request.form.get('senha')

    if not nome or not segundoNome or not email or not senhaform:
        print('Erro: Todos os dados são obrigatórios!')
        return redirect('/cadastro')

    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
    existing_user = cursor.fetchone()

    if existing_user:
        print('Erro: Email já cadastrado!')
        return redirect('/cadastro')

    senhahash = generate_password_hash(senhaform)
    query = 'INSERT INTO users (nome, segundoNome, email, senha) VALUES (%s, %s, %s, %s)'
    values = (nome, segundoNome, email, senhahash)

    try:
        cursor.execute(query, values)
        connection.commit()
        return redirect('/')
    except mysql.connector.Error as err:
        print(f'Erro ao cadastrar usuário: {err}')
        return redirect('/cadastro')
    finally:
        cursor.close()
        connection.close()
