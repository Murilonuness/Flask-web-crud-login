from flask import Blueprint, request, session, render_template, redirect, url_for
import mysql.connector
from werkzeug.security import generate_password_hash
from flask import current_app

adm_route = Blueprint('adm_route', __name__)

def verificar_sessao():
    if 'logado' not in session or session.get('users_health') != 'adm':
        current_app.logger.error("Acesso negado! O usuário não está logado como administrador.")
        return False
    return True

@adm_route.route('/adm', methods=['GET'])
def adm_home():
    if not verificar_sessao():
        return redirect(url_for('home.login'))

    pagina_str = request.args.get('pagina', '1')
    termo_pesquisa = request.args.get('pesquisa', '').strip()

    try:
        pagina = int(pagina_str)
    except ValueError:
        pagina = 1

    usuarios_por_pagina = 10
    offset = (pagina - 1) * usuarios_por_pagina

    connection = mysql.connector.connect(
        host='localhost', database='users_health', user='root', password=''
    )
    cursor = connection.cursor(dictionary=True)

    if termo_pesquisa:
        query = "SELECT nome, segundoNome, email FROM users WHERE email LIKE %s"
        cursor.execute(query, (f"%{termo_pesquisa}%",))
    else:
        query = "SELECT nome, segundoNome, email FROM users LIMIT %s OFFSET %s"
        cursor.execute(query, (usuarios_por_pagina, offset))

    usuarios = cursor.fetchall()

    total_paginas = 1
    if not termo_pesquisa:
        cursor.execute("SELECT COUNT(*) AS total FROM users")
        total_usuarios = cursor.fetchone()["total"]
        total_paginas = max((total_usuarios + usuarios_por_pagina - 1) // usuarios_por_pagina, 1)

    cursor.close()
    connection.close()

    return render_template('adm.html', usuarios=usuarios, pagina=pagina, total_paginas=total_paginas, termo_pesquisa=termo_pesquisa)

@adm_route.route('/adm/logout', methods=['POST'])
def logout():
    session.pop('logado', None)
    session.pop('users_health', None)

    return redirect(url_for('home.login'))

@adm_route.route('/adm/cadastrar', methods=['POST'])
def cadastrar_adm():
    if not verificar_sessao():
        return redirect(url_for('home.login'))

    nome = request.form.get('nome')
    segundoNome = request.form.get('segundoNome')
    email = request.form.get('email')
    senhaform = request.form.get('senha')

    if not nome or not segundoNome or not email or not senhaform:
        return redirect(url_for('adm_route.adm_home'))

    connection = mysql.connector.connect(
        host='localhost', database='users_health', user='root', password=''
    )
    cursor = connection.cursor()
    
    try:
        cursor.execute("SELECT COUNT(*) FROM users WHERE email = %s", (email,))
        email_exists = cursor.fetchone()[0]
        if email_exists > 0:
            return redirect(url_for('adm_route.adm_home'))

        senhahash = generate_password_hash(senhaform)
        query = 'INSERT INTO users (nome, segundoNome, email, senha) VALUES (%s, %s, %s, %s)'
        cursor.execute(query, (nome, segundoNome, email, senhahash))
        connection.commit()

    except mysql.connector.Error:
        return redirect(url_for('adm_route.adm_home'))
    finally:
        cursor.close()
        connection.close()

    return redirect(url_for('adm_route.adm_home'))

@adm_route.route('/adm/banir', methods=['POST'])
def banir():
    if not verificar_sessao():
        return redirect(url_for('home.login'))

    email = request.form.get('email')

    if not email:
        return redirect(url_for('adm_route.adm_home'))

    connection = mysql.connector.connect(
        host='localhost', database='users_health', user='root', password=''
    )
    cursor = connection.cursor()
    
    cursor.execute('DELETE FROM users WHERE email = %s', (email,))
    connection.commit()
    cursor.close()
    connection.close()

    return redirect(url_for('adm_route.adm_home'))

@adm_route.route('/adm/listar_usuarios', methods=['GET'])
def listar_usuarios():
    if not verificar_sessao():
        return redirect(url_for('home.login'))

    connection = mysql.connector.connect(
        host='localhost', database='users_health', user='root', password=''
    )
    cursor = connection.cursor(dictionary=True)

    termo_pesquisa = request.args.get("pesquisa", "")

    if termo_pesquisa:
        query = """
        SELECT id, nome, segundoNome, email 
        FROM users 
        WHERE nome LIKE %s OR segundoNome LIKE %s OR email LIKE %s
        """
        cursor.execute(query, (f"%{termo_pesquisa}%", f"%{termo_pesquisa}%", f"%{termo_pesquisa}%"))
    else:
        query = "SELECT id, nome, segundoNome, email FROM users"
        cursor.execute(query)

    usuarios = cursor.fetchall()
    cursor.close()
    connection.close()

    return render_template('adm.html', usuarios=usuarios, pagina=1, total_paginas=1, termo_pesquisa="")
