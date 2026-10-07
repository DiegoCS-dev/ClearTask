import sqlite3
from app.database import get_connection

conexao = get_connection()
cursor = conexao.cursor()

# 1. Primeiro garantimos que a tabela existe, já com a coluna 'avatar_url' (para bancos novos)
# Nota: Troquei EMAIL por TEXT, pois o SQLite nativamente trabalha melhor com TEXT.
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        avatar_url TEXT,
        create_at TEXT 
    )
""")

# 2. Tentamos adicionar a coluna (caso seja um banco antigo que ainda não tem ela)
try:
    cursor.execute("ALTER TABLE usuarios ADD COLUMN avatar_url TEXT;")
except sqlite3.OperationalError:
    # Se der erro, é porque a coluna 'avatar_url' já existe no banco. Tudo certo!
    pass

conexao.commit()
conexao.close()

print("Banco atualizado com sucesso!")