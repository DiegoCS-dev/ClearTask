from app.database import get_connection

conexao = get_connection()

cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS task (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                status TEXT NOT NULL,
                priority TEXT NOT NULL,
                due_date TEXT,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT,
                user_id INTEGER NOT NULL)""")
conexao.commit()
conexao.close()