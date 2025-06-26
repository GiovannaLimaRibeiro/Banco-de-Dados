from database.connection import get_connection
from models.Materias import Materia

def criar_materia(connection):
    nome = input("Nome da matéria: ")
    horario = input("Horário: ")
    sala = input("Sala: ")
    vagas = input("Vagas: ")
    voluntario_id = int(input("ID do voluntário responsável: "))
    
    materia = Materia(None, nome, horario, sala, vagas, voluntario_id)
    materia_id = materia.create(connection)
    print(f"Matéria criada com sucesso! ID: {materia_id}")

def buscar_materia(connection):
    id = int(input("ID da matéria: "))
    materia = Materia.read(connection, id)
    if materia:
        print(f"ID: {materia.id_materias}, Nome: {materia.nome}, Horário: {materia.horario}")
        print(f"Sala: {materia.sala}, Vagas: {materia.vagas}, Voluntário ID: {materia.voluntario_id}")
    else:
        print("Matéria não encontrada.")

def buscar_todas_materias(connection):
    materias = Materia.read_all(connection)
    if materias:
        for materia in materias:
            print(f"ID: {materia.id_materias}, Nome: {materia.nome}, Horário: {materia.horario}, Sala: {materia.sala}")
    else:
        print("Nenhuma matéria encontrada.")

def atualizar_materia(connection):
    id = int(input("ID da matéria a atualizar: "))
    materia = Materia.read(connection, id)
    if materia:
        print("Dados atuais:")
        print(f"Nome: {materia.nome}")
        print(f"Horário: {materia.horario}")
        print(f"Sala: {materia.sala}")
        print(f"Vagas: {materia.vagas}")
        print(f"Voluntário ID: {materia.voluntario_id}")
        
        print("\nDigite os novos dados:")
        materia.nome = input("Novo nome: ") or materia.nome
        materia.horario = input("Novo horário: ") or materia.horario
        materia.sala = input("Nova sala: ") or materia.sala
        materia.vagas = input("Novas vagas: ") or materia.vagas
        voluntario_input = input("Novo voluntário ID: ")
        materia.voluntario_id = int(voluntario_input) if voluntario_input else materia.voluntario_id
        
        materia.update(connection)
        print("Matéria atualizada com sucesso!")
    else:
        print("Matéria não encontrada.")

def deletar_materia(connection):
    id = int(input("ID da matéria a deletar: "))
    sucesso = Materia.delete(connection, id)
    if sucesso:
        print("Matéria deletada com sucesso.")
    else:
        print("Matéria não encontrada.")

def buscar_materias_por_voluntario(connection):
    voluntario_id = int(input("ID do voluntário: "))
    materias = Materia.buscar_por_voluntario(connection, voluntario_id)
    if materias:
        print(f"Matérias do voluntário {voluntario_id}:")
        for materia in materias:
            print(f"- ID: {materia.id_materias}, Nome: {materia.nome}, Horário: {materia.horario}")
    else:
        print("Nenhuma matéria encontrada para este voluntário.")
