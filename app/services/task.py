from app.database import get_connection
import sqlite3
def create_task(body, user_id):
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO task (title,description,status,priority,due_date,user_id) VALUES (?,?,?,?,?,?)",
                    (body.title, body.description, body.status.value, body.priority.value, body.due_date, user_id))
    conexao.commit()
    conexao.close()

async def view_all_task(user_id):
    conexao = get_connection()
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM task WHERE user_id = ?", (user_id,))
    dados = cursor.fetchall()
    conexao.close()
    return [dict(linha) for linha in dados]
def view_task_id(user_id, id):
    conexao = get_connection()
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()
    cursor.execute("SELECT id,title,description,status,priority,due_date,created_at,updated_at FROM task WHERE id = ? AND user_id = ?", (id, user_id))
    dados = cursor.fetchone()
    conexao.close()
    if dados is None:
        return None
    return dict(dados)
def updateTask(id, body, user_id):
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute(
    """
    UPDATE task
    SET
        title = ?,
        description = ?,
        status = ?,
        priority = ?,
        due_date = ?
    WHERE id = ? AND user_id = ?
    """,
    (
        body.title,
        body.description,
        body.status.value,
        body.priority.value,
        body.due_date,
        id,
        user_id,
    )
)
    conexao.commit()
    linha = cursor.rowcount
    conexao.close()
    return linha

def delete_task(id, user_id):
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM task WHERE id = ? AND user_id = ?",(id, user_id))
    conexao.commit()
    linha = cursor.rowcount
    conexao.close()
    return linha
def concluir_task(id, user_id):
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("UPDATE task SET status = ? WHERE id = ? AND user_id = ?", ("completed", id, user_id))
    conexao.commit()
    linha = cursor.rowcount
    conexao.close()
    return linha