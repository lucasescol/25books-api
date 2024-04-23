import sqlite3

conn = sqlite3.connect('25books.db')
cursor = conn.cursor()

cursor.executescript("""
CREATE TABLE Book (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    isEbook BOOLEAN,
    company TEXT,
    release TEXT,
    author TEXT,
    title TEXT,
    location TEXT,
    borrowed INTEGER
);

CREATE TABLE User (
    email TEXT,
    telephone TEXT,
    cpf TEXT,
    name TEXT,
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    UNIQUE (email, cpf)
);

CREATE TABLE borrow (
    fk_User_id INTEGER,
    fk_Book_id INTEGER,
  	FOREIGN KEY (fk_User_id) REFERENCES User (id) ON DELETE SET NULL,
  	FOREIGN KEY (fk_Book_id) REFERENCES Book (id) ON DELETE RESTRICT
);
""")

print("Tabela criada com sucesso!")

cursor.close()
conn.close()