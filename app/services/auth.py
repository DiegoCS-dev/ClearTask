from app.database import get_connection
import bcrypt
from app.utils.security import criar_token
import sqlite3
def verificar_user(body):
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email = ? ", (body.email,))
    if cursor.fetchone():
        conexao.close()
        return "usuario_existe"
    conexao.close()
    return "email_disponivel" 
def verificar_password(body):
        conexao = get_connection()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = ?", (body.email,))
        password = cursor.fetchone()
        id_user = password[0]
        password = password[3]
        print(password, id_user)
        body.password = body.password.encode('utf-8')
        print(body.password)
        return bcrypt.checkpw(body.password, password), id_user

def create_User(body):
    if verificar_user(body) == "email_disponivel":
        conexao = get_connection()
        cursor = conexao.cursor()
        body.password = body.password.encode('utf-8')
        salt = bcrypt.gensalt(rounds=12)
        body.password = bcrypt.hashpw(body.password, salt)
        cursor.execute("INSERT INTO usuarios (name, email, password) VALUES (?,?,?)", (body.name, body.email, body.password))
        conexao.commit()
        conexao.close()
        return True
    return False
def login(body):
    if verificar_user(body) == "usuario_existe":
        verificacao, id_user = verificar_password(body)
        if verificacao:
            access_token = criar_token(id_user)
            print(access_token)
            return access_token
    return False

def me(user_id):
    conexao = get_connection()
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()
    cursor.execute("SELECT id,name,email FROM usuarios WHERE id = ?", (user_id,))
    dados = cursor.fetchone()
    conexao.close()
    return dict(dados)