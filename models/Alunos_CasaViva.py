'''CRUD Alunos_CasaViva '''
from mysql.connector import MySQLConnection

class Alunos_CasaViva:
    
    def __init__(self, idCasaViva, nome, idade, sexo, endereco, nome_responsavel, cpf_responsavel, celular):
        self.idCasaViva = idCasaViva
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.endereco = endereco
        self.nome_responsavel = nome_responsavel
        self.cpf_responsavel = cpf_responsavel
        self.celular = celular

    def create(self, connection: MySQLConnection):
        cursor = connection.cursor()  # Indentação corrigida
        sql = """
        INSERT INTO Alunos_CasaViva (nome, idade, sexo, endereco, nomeDoResponsavel, cpfDoResponsavel, celular)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (self.nome, self.idade, self.sexo, self.endereco, self.nome_responsavel, self.cpf_responsavel, self.celular)
        cursor.execute(sql, values)
        connection.commit()
        self.idCasaViva = cursor.lastrowid
        cursor.close()
        return self.idCasaViva

    @staticmethod  # Decorator @staticmethod adicionado
    def read(connection: MySQLConnection, aluno_id: int):
        cursor = connection.cursor()
        sql = "SELECT idCasaViva, nome, idade, sexo, endereco, nomeDoResponsavel, cpfDoResponsavel, celular FROM Alunos_CasaViva WHERE idCasaViva = %s"
        cursor.execute(sql, (aluno_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Alunos_CasaViva(*row)
        return None
    
    @staticmethod
    def read_all(connection: MySQLConnection):
        cursor = connection.cursor()
        sql = "SELECT idCasaViva, nome, idade, sexo, endereco, nomeDoResponsavel, cpfDoResponsavel, celular FROM Alunos_CasaViva ORDER BY nome"
        cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        if rows:
            return [Alunos_CasaViva(*row) for row in rows]
        return []

    def update(self, connection: MySQLConnection):
        cursor = connection.cursor()
        sql = """UPDATE Alunos_CasaViva SET nome = %s, idade = %s, sexo = %s, endereco = %s, 
        nomeDoResponsavel = %s, cpfDoResponsavel = %s, celular = %s WHERE idCasaViva = %s"""
        values = (self.nome, self.idade, self.sexo, self.endereco, self.nome_responsavel, self.cpf_responsavel, self.celular, self.idCasaViva)  # self.idCasaViva adicionado
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()

    @staticmethod
    def delete(connection: MySQLConnection, aluno_id: int):
        # Primeiro, remover todas as matrículas do aluno
        from models.Alunos_CasaViva_has_Materias import AlunoMateria
        AlunoMateria.remover_todas_matriculas_aluno(connection, aluno_id)
        
        # Depois, deletar o aluno
        cursor = connection.cursor()
        sql = "DELETE FROM Alunos_CasaViva WHERE idCasaViva = %s"
        cursor.execute(sql, (aluno_id,))
        connection.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        return affected_rows > 0
    
    @staticmethod
    def buscar_por_nome(connection: MySQLConnection, nome: str):
        cursor = connection.cursor()
        sql = "SELECT idCasaViva, nome, idade, sexo, endereco, nomeDoResponsavel, cpfDoResponsavel, celular FROM Alunos_CasaViva WHERE nome LIKE %s"
        cursor.execute(sql, (f"%{nome}%",))
        rows = cursor.fetchall()
        cursor.close()
        if rows:
            return [Alunos_CasaViva(*row) for row in rows]
        return []


from database.connection import get_connection