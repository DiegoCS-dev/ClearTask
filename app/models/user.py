from app.database import get_connection
conexao = get_connection()
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email EMAIL NOT NULL UNIQUE,
                password TEXT NOT NULL,
                create_at TEXT )
                """)
conexao.commit()
conexao.close()