#livro -> nome, autor, edição, ano, editora, alugado, id

from regex import X
import sqlite3

class Livros():
    def __init__(self, id, nome, autor, edição, ano, editora, alugado):
        self.id = id
        self.nome = nome
        self.autor = autor
        self.edição = edição
        self.ano = ano
        self.editora = editora
        self.alugado = alugado
    
    def set_x(self, x, nome = False, autor = False, edição = False, ano = False, editora = False, alugado = False):
        if nome:
            self.nome = x
        elif autor:
            self.autor = x
        elif edição:
            self.edição = x
        elif ano:
            self.ano = x
        elif editora:
            self.editora = x
        elif alugado:
            self.alugado = x
        else:
            print("Não foi possível alterar o valor")
    
    def insert(self):
        sql_insert = 'insert into livros values(?,?,?,?,?,?,?)'
        conn, cursor = create_table()
        rec = (self.id, self.nome, self.autor, self.edição, self.ano, self.editora, self.alugado)
        cursor.execute(sql_insert, rec)
        conn.commit()

def create_table():
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()
    sql_creat_table = 'create table if not exists livros (id integer primary key, nome text, autor text, edição text, ano text, editora text, alugado text)'
    cursor.execute(sql_creat_table)
    return (conn,cursor)

def main():
    percy_jackson = Livros(1, "Percy Jackson", "Rick Riordan", "1", "2000", "Harper", "Não")
    percy_jackson.insert()

main()