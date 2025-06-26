from mysql.connector import MySQLConnection
from datetime import date

class Voluntario:
    def __init__(self, id, nome, email, curso, matricula, sexo, cpf, data_nascimento, ano_voluntariado):
        self.id = id
        self.nome = nome
        self.email = email
        self.curso = curso
        self.matricula = matricula
        self.sexo = sexo
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.ano_voluntariado = ano_voluntariado

    def create(self, connection: MySQLConnection):
        cursor = connection.cursor()
        sql = """INSERT INTO Voluntarios (nome, email, curso, matricula, sexo, cpf, dataNascimento, anoDoVoluntariado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (self.nome, self.email, self.curso, self.matricula, self.sexo, self.cpf, self.data_nascimento, self.ano_voluntariado)
        cursor.execute(sql, values)
        connection.commit()
        self.id = cursor.lastrowid
        cursor.close()
        return self.id

    @staticmethod
    def read(connection: MySQLConnection, voluntario_id: int):
        cursor = connection.cursor()
        sql = "SELECT id, nome, email, curso, matricula, sexo, cpf, dataNascimento, anoDoVoluntariado FROM Voluntarios WHERE id = %s"
        cursor.execute(sql, (voluntario_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Voluntario(*row)
        return None

    @staticmethod
    def read_all(connection: MySQLConnection):
        cursor = connection.cursor()
        sql = "SELECT id, nome, email, curso, matricula, sexo, cpf, dataNascimento, anoDoVoluntariado FROM Voluntarios"
        cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        if rows:
            return [Voluntario(*row) for row in rows]
        return []

    def update(self, connection: MySQLConnection):
        cursor = connection.cursor()
        sql = """UPDATE Voluntarios SET nome = %s, email = %s, curso = %s, matricula = %s, sexo = %s, cpf = %s, dataNascimento = %s, anoDoVoluntariado = %s WHERE id = %s"""
        values = (self.nome, self.email, self.curso, self.matricula, self.sexo, self.cpf, self.data_nascimento, self.ano_voluntariado, self.id)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()

    @staticmethod
    def delete(connection: MySQLConnection, voluntario_id: int):
        cursor = connection.cursor()
        sql = "DELETE FROM Voluntarios WHERE id = %s"
        cursor.execute(sql, (voluntario_id,))
        connection.commit()
        cursor.close()

    @staticmethod
    def buscar_por_cpf(connection: MySQLConnection, cpf: str):
        cursor = connection.cursor()
        sql = "SELECT id, nome, email, curso, matricula, sexo, cpf, dataNascimento, anoDoVoluntariado FROM Voluntarios WHERE cpf = %s"
        cursor.execute(sql, (cpf,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Voluntario(*row)
        return None

    @staticmethod
    def buscar_por_curso(connection: MySQLConnection, curso: str):
        cursor = connection.cursor()
        sql = "SELECT id, nome, email, curso, matricula, sexo, cpf, dataNascimento, anoDoVoluntariado FROM Voluntarios WHERE curso LIKE %s"
        cursor.execute(sql, (f"%{curso}%",))
        rows = cursor.fetchall()
        cursor.close()
        if rows:
            return [Voluntario(*row) for row in rows]
        return []

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Email: {self.email}, Curso: {self.curso}, Matrícula: {self.matricula}"