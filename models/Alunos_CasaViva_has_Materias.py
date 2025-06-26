from mysql.connector import MySQLConnection

class Alunos_CasaViva_has_Materias:
    def __init__(self, aluno_id, materia_id):
        self.aluno_id = aluno_id
        self.materia_id = materia_id

    # CREATE - Matricular aluno em uma matéria
    def matricular(self, connection: MySQLConnection):
        """Matricula um aluno em uma matéria"""
        cursor = connection.cursor()
        sql = "INSERT INTO Alunos_CasaViva_has_Materias (Alunos_CasaViva_idCasaViva, Materias_idMaterias) VALUES (%s, %s)"
        cursor.execute(sql, (self.aluno_id, self.materia_id))
        connection.commit()
        cursor.close()

    # READ - Verificar se aluno está matriculado em uma matéria
    @staticmethod
    def verificar_matricula(connection: MySQLConnection, aluno_id: int, materia_id: int):
        """Verifica se um aluno está matriculado em uma matéria específica"""
        cursor = connection.cursor()
        sql = "SELECT * FROM Alunos_CasaViva_has_Materias WHERE Alunos_CasaViva_idCasaViva = %s AND Materias_idMaterias = %s"
        cursor.execute(sql, (aluno_id, materia_id))
        row = cursor.fetchone()
        cursor.close()
        return row is not None

    # READ - Buscar todas as matrícula de um aluno
    @staticmethod
    def buscar_materias_do_aluno(connection: MySQLConnection, aluno_id: int):
        """Retorna todas as matérias que um aluno está matriculado"""
        cursor = connection.cursor()
        sql = """
        SELECT m.idMaterias, m.nome, m.horario, m.sala, m.vagas, v.nome as professor
        FROM Materias m 
        JOIN Alunos_CasaViva_has_Materias am ON m.idMaterias = am.Materias_idMaterias 
        JOIN Voluntarios v ON m.Voluntarios_id = v.id
        WHERE am.Alunos_CasaViva_idCasaViva = %s
        """
        cursor.execute(sql, (aluno_id,))
        rows = cursor.fetchall()
        cursor.close()
        return rows

    # READ - Buscar todos os alunos de uma matéria
    @staticmethod
    def buscar_alunos_da_materia(connection: MySQLConnection, materia_id: int):
        """Retorna todos os alunos matriculados em uma matéria"""
        cursor = connection.cursor()
        sql = """
        SELECT a.idCasaViva, a.nome, a.idade, a.sexo, a.celular
        FROM Alunos_CasaViva a 
        JOIN Alunos_CasaViva_has_Materias am ON a.idCasaViva = am.Alunos_CasaViva_idCasaViva 
        WHERE am.Materias_idMaterias = %s
        """
        cursor.execute(sql, (materia_id,))
        rows = cursor.fetchall()
        cursor.close()
        return rows

    # READ - Listar todas as matrículas
    @staticmethod
    def listar_todas_matriculas(connection: MySQLConnection):
        """Lista todas as matrículas com informações do aluno e matéria"""
        cursor = connection.cursor()
        sql = """
        SELECT a.nome as aluno, m.nome as materia, m.horario, v.nome as professor
        FROM Alunos_CasaViva_has_Materias am
        JOIN Alunos_CasaViva a ON am.Alunos_CasaViva_idCasaViva = a.idCasaViva
        JOIN Materias m ON am.Materias_idMaterias = m.idMaterias
        JOIN Voluntarios v ON m.Voluntarios_id = v.id
        ORDER BY a.nome, m.nome
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    # DELETE - Desmatricular aluno de uma matéria
    @staticmethod
    def desmatricular(connection: MySQLConnection, aluno_id: int, materia_id: int):
        """Remove a matrícula de um aluno em uma matéria"""
        cursor = connection.cursor()
        sql = "DELETE FROM Alunos_CasaViva_has_Materias WHERE Alunos_CasaViva_idCasaViva = %s AND Materias_idMaterias = %s"
        cursor.execute(sql, (aluno_id, materia_id))
        connection.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        return affected_rows > 0

    # DELETE - Remover todas as matrículas de um aluno
    @staticmethod
    def remover_todas_matriculas_aluno(connection: MySQLConnection, aluno_id: int):
        """Remove todas as matrículas de um aluno (útil antes de deletar o aluno)"""
        cursor = connection.cursor()
        sql = "DELETE FROM Alunos_CasaViva_has_Materias WHERE Alunos_CasaViva_idCasaViva = %s"
        cursor.execute(sql, (aluno_id,))
        connection.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        return affected_rows

    # DELETE - Remover todas as matrículas de uma matéria
    @staticmethod
    def remover_todas_matriculas_materia(connection: MySQLConnection, materia_id: int):
        """Remove todas as matrículas de uma matéria (útil antes de deletar a matéria)"""
        cursor = connection.cursor()
        sql = "DELETE FROM Alunos_CasaViva_has_Materias WHERE Materias_idMaterias = %s"
        cursor.execute(sql, (materia_id,))
        connection.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        return affected_rows

    # Método para contar alunos em uma matéria
    @staticmethod
    def contar_alunos_materia(connection: MySQLConnection, materia_id: int):
        """Conta quantos alunos estão matriculados em uma matéria"""
        cursor = connection.cursor()
        sql = "SELECT COUNT(*) FROM Alunos_CasaViva_has_Materias WHERE Materias_idMaterias = %s"
        cursor.execute(sql, (materia_id,))
        count = cursor.fetchone()[0]
        cursor.close()
        return count

    # Método para contar matérias de um aluno
    @staticmethod
    def contar_materias_aluno(connection: MySQLConnection, aluno_id: int):
        """Conta quantas matérias um aluno está matriculado"""
        cursor = connection.cursor()
        sql = "SELECT COUNT(*) FROM Alunos_CasaViva_has_Materias WHERE Alunos_CasaViva_idCasaViva = %s"
        cursor.execute(sql, (aluno_id,))
        count = cursor.fetchone()[0]
        cursor.close()
        return count