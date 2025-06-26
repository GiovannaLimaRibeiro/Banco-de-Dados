from database.connection import get_connection
from models.Alunos_CasaViva_has_Materias import Alunos_CasaViva_has_Materias

def matricular_aluno(connection):
    aluno_id = int(input("ID do aluno: "))
    materia_id = int(input("ID da matéria: "))
    
    # Verificar se já está matriculado
    if Alunos_CasaViva_has_Materias.verificar_matricula(connection, aluno_id, materia_id):
        print("Aluno já está matriculado nesta matéria!")
        return
    
    matricula = Alunos_CasaViva_has_Materias(aluno_id, materia_id)
    matricula.matricular(connection)
    print("Aluno matriculado com sucesso!")

def desmatricular_aluno(connection):
    aluno_id = int(input("ID do aluno: "))
    materia_id = int(input("ID da matéria: "))
    
    sucesso = Alunos_CasaViva_has_Materias.desmatricular(connection, aluno_id, materia_id)
    if sucesso:
        print("Aluno desmatriculado com sucesso!")
    else:
        print("Matrícula não encontrada.")

def listar_materias_do_aluno(connection):
    aluno_id = int(input("ID do aluno: "))
    materias = Alunos_CasaViva_has_Materias.buscar_materias_do_aluno(connection, aluno_id)
    if materias:
        print(f"Matérias do aluno {aluno_id}:")
        for materia in materias:
            print(f"- {materia[1]} ({materia[2]}) - Professor: {materia[5]}")
    else:
        print("Aluno não tem matérias matriculadas.")

def listar_alunos_da_materia(connection):
    materia_id = int(input("ID da matéria: "))
    alunos = Alunos_CasaViva_has_Materias.buscar_alunos_da_materia(connection, materia_id)
    if alunos:
        print(f"Alunos da matéria {materia_id}:")
        for aluno in alunos:
            print(f"- {aluno[1]} (Idade: {aluno[2]})")
    else:
        print("Nenhum aluno matriculado nesta matéria.")

def listar_todas_matriculas(connection):
    matriculas = Alunos_CasaViva_has_Materias.listar_todas_matriculas(connection)
    if matriculas:
        print("Todas as matrículas:")
        for matricula in matriculas:
            print(f"Aluno: {matricula[0]} - Matéria: {matricula[1]} - Horário: {matricula[2]} - Professor: {matricula[3]}")
    else:
        print("Nenhuma matrícula encontrada.")