from database.connection import get_connection
from models.Alunos_CasaViva import Alunos_CasaViva

def adicionar_aluno(connection):
    con = get_connection()
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo: ")
    endereco = input("Endereço: ")
    nome_responsavel = input("Nome do responsável: ")
    cpf_responsavel = input("CPF do responsável: ")
    celular = input("Celular: ")

    aluno = Alunos_CasaViva(None, nome, idade, sexo, endereco, nome_responsavel, cpf_responsavel, celular)
    aluno_id = aluno.create(con)
    print(f"Aluno criado com sucesso! ID: {aluno_id}")
    con.close()

def buscar_aluno(connection):
    id = int(input("ID do aluno: "))
    aluno = Alunos_CasaViva.read(connection, id)
    if aluno:
        print(f"ID: {aluno.idCasaViva}, Nome: {aluno.nome}, Idade: {aluno.idade}, Sexo: {aluno.sexo}")
        print(f"Endereço: {aluno.endereco}, Responsável: {aluno.nome_responsavel}")
        print(f"CPF Responsável: {aluno.cpf_responsavel}, Celular: {aluno.celular}")
    else:
        print("Aluno não encontrado.")
    
def buscar_todos_alunos(connection):
    alunos = Alunos_CasaViva.read_all(connection)
    if alunos:
        for aluno in alunos:
            print(f"ID: {aluno.idCasaViva}, Nome: {aluno.nome}, Idade: {aluno.idade}, Sexo: {aluno.sexo}")
    else:
        print("Nenhum aluno encontrado.")

def atualizaraluno(connection):
    id = int(input("ID do aluno a atualizar: "))
    aluno = Alunos_CasaViva.read(connection, id)
    if aluno:
        print("Dados atuais:")
        print(f"Nome: {aluno.nome}")
        print(f"Idade: {aluno.idade}")
        print(f"Sexo: {aluno.sexo}")
        print(f"Endereço: {aluno.endereco}")
        print(f"Responsável: {aluno.nome_responsavel}")
        print(f"CPF Responsável: {aluno.cpf_responsavel}")
        print(f"Celular: {aluno.celular}")
        
        print("\nDigite os novos dados:")
        aluno.nome = input("Novo nome: ") or aluno.nome
        aluno.idade = int(input("Nova idade: ") or aluno.idade)
        aluno.sexo = input("Novo sexo: ") or aluno.sexo
        aluno.endereco = input("Novo endereço: ") or aluno.endereco
        aluno.nome_responsavel = input("Novo responsável: ") or aluno.nome_responsavel
        aluno.cpf_responsavel = input("Novo CPF responsável: ") or aluno.cpf_responsavel
        aluno.celular = input("Novo celular: ") or aluno.celular
        
        aluno.update(connection)
        print("Aluno atualizado com sucesso!")
    else:
        print("Aluno não encontrado.")

def deletar_aluno(connection):
    id = int(input("ID do aluno a deletar: "))
    sucesso = Alunos_CasaViva.delete(connection, id)
    if sucesso:
        print("Aluno deletado com sucesso.")
    else:
        print("Aluno não encontrado.")

def buscar_aluno_por_nome(connection):
    nome = input("Nome do aluno: ")
    alunos = Alunos_CasaViva.buscar_por_nome(connection, nome)
    if alunos:
        for aluno in alunos:
            print(f"ID: {aluno.idCasaViva}, Nome: {aluno.nome}, Idade: {aluno.idade}")
    else:
        print("Nenhum aluno encontrado com esse nome.")
