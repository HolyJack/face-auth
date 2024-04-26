import os
import psycopg
from pgvector.psycopg import register_vector


class DataBase:

    def __init__(self):
        get_env = os.environ.get
        self.conn = psycopg.connect(
                user=get_env("POSTGRES_USER"),
                password=get_env("POSTGRES_PASSWORD"),
                host=get_env("POSTGRES_HOST"),
                dbname=get_env("POSTGRES_DB")
        )
        register_vector(self.conn)

    def add_user(self, login, embedding):
        try:
            cur = self.conn.cursor()
            cur.execute(
                    "INSERT INTO embeddings (login, embedding) VALUES (%s, %s)",
                    [login, embedding]
            )
            self.conn.commit()
        except Exception:
            self.conn.rollback()

    def delete_user(self, login):
        self.cur.execute(
            "DELETE FROM embeddings WHERE login = %s",
            (login)
        )

    def get_user(self, embedding):
        try:
            cur = self.conn.cursor()
            res = cur.execute('SELECT login FROM embeddings ORDER BY embedding <-> %s LIMIT 1', (embedding,)).fetchone()
            self.conn.commit()
        except Exception:
            self.conn.rollback()
        return res[0]

    def count(self):

        self.cur.execute("SELECT COUNT(*) FROM embeddings")
        return self.cur.fetchone()[0]
