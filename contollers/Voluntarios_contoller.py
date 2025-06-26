from database.connection import get_connection
from models.Voluntarios import Voluntario

def criar_voluntario(connection):
    nome = input("Nome do voluntário: ")
    email = input("Email: ")
    curso = input("Curso: ")
    matricula = int(input("Matrícula: "))
    sexo = input("Sexo (M/F): ")
    cpf = input("CPF: ")
    data_nascimento = input("Data de nascimento: ")
    ano_voluntariado = input("Ano do voluntariado: ")
    
    voluntario = Voluntario(None, nome, email, curso, matricula, sexo, cpf, data_nascimento, ano_voluntariado)
    voluntario_id = voluntario.create(connection)
    print(f"Voluntário criado com sucesso! ID: {voluntario_id}")

def buscar_voluntario(connection):
    id = int(input("ID do voluntário: "))
    voluntario = Voluntario.read(connection, id)
    if voluntario:
        print(f"ID: {voluntario.id}, Nome: {voluntario.nome}, Email: {voluntario.email}")
        print(f"Curso: {voluntario.curso}, Matrícula: {voluntario.matricula}")
        print(f"Sexo: {voluntario.sexo}, CPF: {voluntario.cpf}")
        print(f"Data Nascimento: {voluntario.data_nascimento}, Ano Voluntariado: {voluntario.ano_voluntariado}")
    else:
        print("Voluntário não encontrado.")

def buscar_todos_voluntarios(connection):
    voluntarios = Voluntario.read_all(connection)
    if voluntarios:
        for voluntario in voluntarios:
            print(f"ID: {voluntario.id}, Nome: {voluntario.nome}, Curso: {voluntario.curso}, Email: {voluntario.email}")
    else:
        print("Nenhum voluntário encontrado.")

def atualizar_voluntario(connection):
    id = int(input("ID do voluntário a atualizar: "))
    voluntario = Voluntario.read(connection, id)
    if voluntario:
        print("Dados atuais:")
        print(f"Nome: {voluntario.nome}")
        print(f"Email: {voluntario.email}")
        print(f"Curso: {voluntario.curso}")
        print(f"Matrícula: {voluntario.matricula}")
        print(f"Sexo: {voluntario.sexo}")
        print(f"CPF: {voluntario.cpf}")
        
        print("\nDigite os novos dados:")
        voluntario.nome = input("Novo nome: ") or voluntario.nome
        voluntario.email = input("Novo email: ") or voluntario.email
        voluntario.curso = input("Novo curso: ") or voluntario.curso
        matricula_input = input("Nova matrícula: ")
        voluntario.matricula = int(matricula_input) if matricula_input else voluntario.matricula
        voluntario.sexo = input("Novo sexo: ") or voluntario.sexo
        voluntario.cpf = input("Novo CPF: ") or voluntario.cpf
        data_input = input("Nova data nascimento (YYYY-MM-DD): ")
        voluntario.data_nascimento = data_input or voluntario.data_nascimento
        ano_input = input("Novo ano voluntariado (YYYY-MM-DD): ")
        voluntario.ano_voluntariado = ano_input or voluntario.ano_voluntariado
        
        voluntario.update(connection)
        print("Voluntário atualizado com sucesso!")
    else:
        print("Voluntário não encontrado.")

def deletar_voluntario(connection):
    id = int(input("ID do voluntário a deletar: "))
    Voluntario.delete(connection, id)
    print("Voluntário deletado com sucesso.")

def buscar_voluntario_por_cpf(connection):
    cpf = input("CPF do voluntário: ")
    voluntario = Voluntario.buscar_por_cpf(connection, cpf)
    if voluntario:
        print(f"ID: {voluntario.id}, Nome: {voluntario.nome}, Curso: {voluntario.curso}")
    else:
        print("Voluntário não encontrado com esse CPF.")