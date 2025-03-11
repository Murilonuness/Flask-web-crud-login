from flask import Blueprint, render_template, request, redirect, session
import mysql.connector
from werkzeug.security import check_password_hash

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home():
    return render_template('login.html')

@home_route.route('/login', methods=['POST', 'GET'])
def login():
    emailform = request.form.get('email')
    senhaform = request.form.get('senha')

    if not senhaform or not emailform:
        return redirect('/')

    connection = mysql.connector.connect(
        host='localhost', database='users_health', user='root', password=''
    )
    cursor = connection.cursor()
    cursor.execute('SELECT id, nome, segundoNome, email, senha FROM users WHERE email = %s', (emailform,))
    user = cursor.fetchone()

    if emailform == 'adm' and senhaform == '000':
        session['logado'] = True
        session['users_health'] = 'adm'
        cursor.close()
        connection.close()
        return redirect('/adm')

    if user:
        user_id, nome, segundo_nome, email_db, senha_db = user

        if check_password_hash(senha_db, senhaform) or senhaform.strip() == senha_db:
            session['logado'] = True
            session['users_health'] = email_db
            cursor.close()
            connection.close()
            return redirect(f'/user/{nome}')

    cursor.close()
    connection.close()

    print("Erro: Usuário ou senha inválidos!")
    return redirect('/')
