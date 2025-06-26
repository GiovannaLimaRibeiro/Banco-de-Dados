from mysql.connector import MySQLConnection

class Materia:
    def __init__(self, id_materias, nome, horario, sala, vagas, voluntario_id):
        self.id_materias = id_materias
        self.nome = nome
        self.horario = horario
        self.sala = sala
        self.vagas = vagas
        self.voluntario_id = voluntario_id

    def create(self, connection: MySQLConnection):
        # Verificar se o voluntário existe antes de criar a matéria
        if not self._verificar_voluntario_existe(connection, self.voluntario_id):
            raise ValueError(f"Voluntário com ID {self.voluntario_id} não existe")
        
        cursor = connection.cursor()
        sql = """INSERT INTO Materias (nome, horario, sala, vagas, Voluntarios_id) VALUES (%s, %s, %s, %s, %s)"""
        values = (self.nome, self.horario, self.sala, self.vagas, self.voluntario_id)
        cursor.execute(sql, values)
        connection.commit()
        self.id_materias = cursor.lastrowid
        cursor.close()
        return self.id_materias

    @staticmethod
    def read(connection: MySQLConnection, materia_id: int):
        cursor = connection.cursor()
        sql = "SELECT idMaterias, nome, horario, sala, vagas, Voluntarios_id FROM Materias WHERE idMaterias = %s"
        cursor.execute(sql, (materia_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Materia(*row)
        return None

    @staticmethod
    def read_all(connection: MySQLConnection):
        cursor = connection.cursor()
        sql = "SELECT idMaterias, nome, horario, sala, vagas, Voluntarios_id FROM Materias ORDER BY nome"
        cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        if rows:
            return [Materia(*row) for row in rows]
        return []

    def update(self, connection: MySQLConnection):
        # Verificar se o voluntário existe antes de atualizar
        if not self._verificar_voluntario_existe(connection, self.voluntario_id):
            raise ValueError(f"Voluntário com ID {self.voluntario_id} não existe")
        
        cursor = connection.cursor()
        sql = """UPDATE Materias SET nome = %s, horario = %s, sala = %s, vagas = %s, Voluntarios_id = %s WHERE idMaterias = %s"""
        values = (self.nome, self.horario, self.sala, self.vagas, self.voluntario_id, self.id_materias)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()

    @staticmethod
    def delete(connection: MySQLConnection, materia_id: int):
        # Primeiro, remover todas as matrículas da matéria
        from models.Alunos_CasaViva_has_Materias import Alunos_CasaViva_has_Materias
        Alunos_CasaViva_has_Materias.remover_todas_matriculas_materia(connection, materia_id)
        
        # Depois, deletar a matéria
        cursor = connection.cursor()
        sql = "DELETE FROM Materias WHERE idMaterias = %s"
        cursor.execute(sql, (materia_id,))
        connection.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        return affected_rows > 0

    @staticmethod
    def buscar_por_nome(connection: MySQLConnection, nome: str):
        cursor = connection.cursor()
        sql = "SELECT idMaterias, nome, horario, sala, vagas, Voluntarios_id FROM Materias WHERE nome LIKE %s"
        cursor.execute(sql, (f"%{nome}%",))
        rows = cursor.fetchall()
        cursor.close()
        if rows:
            return [Materia(*row) for row in rows]
        return []

    @staticmethod
    def buscar_por_voluntario(connection: MySQLConnection, voluntario_id: int):
        cursor = connection.cursor()
        sql = "SELECT idMaterias, nome, horario, sala, vagas, Voluntarios_id FROM Materias WHERE Voluntarios_id = %s"
        cursor.execute(sql, (voluntario_id,))
        rows = cursor.fetchall()
        cursor.close()
        if rows:
            return [Materia(*row) for row in rows]
        return []
    
    @staticmethod
    def buscar_por_sala(connection: MySQLConnection, sala: str):
        cursor = connection.cursor()
        sql = "SELECT idMaterias, nome, horario, sala, vagas, Voluntarios_id FROM Materias WHERE sala = %s"
        cursor.execute(sql, (sala,))
        rows = cursor.fetchall()
        cursor.close()
        if rows:
            return [Materia(*row) for row in rows]
        return []
    
    def _verificar_voluntario_existe(self, connection: MySQLConnection, voluntario_id: int):
        """Método privado para verificar se um voluntário existe"""
        cursor = connection.cursor()
        sql = "SELECT id FROM Voluntarios WHERE id = %s"
        cursor.execute(sql, (voluntario_id,))
        result = cursor.fetchone()
        cursor.close()
        return result is not None


