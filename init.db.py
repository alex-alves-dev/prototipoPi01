import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (nome, bairro, cidade, email) VALUES (?, ?, ?, ?)",
            ('Alex da Silva Alves', 'Oziel', 'Campinas', '2000860@aluno.univesp.br')
            )
cur.execute("INSERT INTO posts (nome, bairro, cidade, email) VALUES (?, ?, ?, ?)",
            ('Gabriel Marques', 'Monte Cristo', 'Araras', '2000800@123.com')
            )

connection.commit()
connection.close()