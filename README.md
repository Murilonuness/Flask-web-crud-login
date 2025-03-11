# HealthProject

## 🏥 Sobre o Projeto

O **HealthProject** é um sistema web desenvolvido com **Flask** e **MySQL**, oferecendo um ambiente seguro para login, cadastro e gerenciamento de usuários. O projeto inclui um painel administrativo com autenticação baseada em sessão, onde administradores podem visualizar, buscar, cadastrar e excluir usuários.

---

## 📌 Funcionalidades

- **Login e Cadastro** de usuários com hashing de senha.
- **Autenticação por sessão** para proteção de áreas restritas.
- **Painel Administrativo**:
  - Busca de usuários por e-mail.
  - Paginação dos resultados.
  - Cadastro e exclusão de usuários.
- **Sistema de logout** seguro para encerrar sessões de administradores.

---

## 📂 Estrutura do Projeto

```
HealthProject/
  ├── main.py (Flask)
  ├── routes/
  │   ├── home.py (Login e sessão)
  │   ├── cadastro.py (Cadastro de usuários)
  │   ├── adm.py (Gerenciamento de usuários)
  │   └── user.py (Página Inicial)
  ├── templates/
  │   ├── login.html
  │   ├── cadastro.html
  │   ├── home.html
  │   ├── adm.html
  ├── static/
  │   ├── css/
  │   │   ├── adm.css
  │   │   ├── cadastro.css
  │   │   ├── login.css
  │   │   └── user.css
  │   └── media/
  │       ├── login.jpg
  │       ├── cadastro.jpg
  │       ├── pag_inicial.jpg
  │       └── pag_adm.jpg
  ├── README.md
  └── requirements.txt
```

---

## 🖥️ Preview do Projeto

### 🔹 Página de Login
![Login](static/media/login.jpg)

### 🔹 Página de Cadastro
![Cadastro](static/media/cadastro.jpg)

### 🔹 Página Inicial
![Home](static/media/pag_inicial.jpg)

### 🔹 Painel Administrativo
![Admin](static/media/pag_adm.jpg)

---

## 🛠️ Tecnologias Utilizadas

- **Backend:** Flask (Python)
- **Banco de Dados:** MySQL
- **Frontend:** HTML + CSS
- **Segurança:** Werkzeug Security (Hashing de Senhas) e Flask Session

---

## 🚀 Como Rodar o Projeto

### 🔹 1. Clone o Repositório
```bash
git clone https://github.com/seu-usuario/HealthProject.git
cd HealthProject
```

### 🔹 2. Configure o Ambiente Virtual
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 🔹 3. Instale as Dependências
```bash
pip install -r requirements.txt
```

### 🔹 4. Configure o Banco de Dados
Crie o banco de dados `users_health` e a tabela de usuários:
```sql
CREATE DATABASE users_health;
USE users_health;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    segundoNome VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    senha VARCHAR(255)
);
```

### 🔹 5. Execute a Aplicação
```bash
python main.py
```
O servidor estará rodando em **http://127.0.0.1:5000/**.

---

## 🔒 Segurança Implementada

- Hashing de senha utilizando `generate_password_hash()`.
- Proteção de páginas administrativas com **Flask Session**.
- Logout seguro para encerrar sessões do administrador.

---

## 🐝 Licença

Este projeto está sob a licença **MIT**.

---

## 🤝 Contribuição

Sinta-se à vontade para contribuir com melhorias! Abra um **Pull Request** ou relatar **Issues** no repositório.

🔗 **Autor:** [Murilo](https://github.com/Murilonuness)
