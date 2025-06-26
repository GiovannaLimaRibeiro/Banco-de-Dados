from contollers.Alunos_CasaViva_controller import adicionar_aluno, atualizaraluno, buscar_aluno, buscar_aluno_por_nome, buscar_todos_alunos, deletar_aluno

from contollers.Alunos_CasaViva_has_Materias_controller import matricular_aluno, desmatricular_aluno, listar_alunos_da_materia, listar_materias_do_aluno, listar_todas_matriculas

from contollers.Materias_controller import criar_materia, buscar_materia, atualizar_materia, buscar_materias_por_voluntario, buscar_todas_materias,  deletar_materia

from contollers.Voluntarios_contoller import criar_voluntario,buscar_voluntario,buscar_todos_voluntarios, atualizar_voluntario, buscar_voluntario_por_cpf, deletar_voluntario


from database.connection import get_connection
def menu_principal():
    print("\n=== SISTEMA CASA VIVA ===")
    print("1. Gerenciar Alunos")
    print("2. Gerenciar Voluntários")
    print("3. Gerenciar Matérias")
    print("4. Gerenciar Matrículas")
    print("0. Sair")

def menu_alunos():
    print("\n=== MENU ALUNOS ===")
    print("1. Adicionar aluno")
    print("2. Buscar aluno")
    print("3. Listar todos os alunos")
    print("4. Atualizar aluno")
    print("5. Deletar aluno")
    print("6. Buscar aluno por nome")
    print("0. Voltar")

def menu_voluntarios():
    print("\n=== MENU VOLUNTÁRIOS ===")
    print("1. Criar voluntário")
    print("2. Buscar voluntário por ID")
    print("3. Listar todos os voluntários")
    print("4. Atualizar voluntário")
    print("5. Deletar voluntário")
    print("6. Buscar voluntário por CPF")
    print("0. Voltar")

def menu_materias():
    print("\n=== MENU MATÉRIAS ===")
    print("1. Criar matéria")
    print("2. Buscar matéria por ID")
    print("3. Listar todas as matérias")
    print("4. Atualizar matéria")
    print("5. Deletar matéria")
    print("6. Buscar matérias por voluntário")
    print("0. Voltar")

def menu_matriculas():
    print("\n=== MENU MATRÍCULAS ===")
    print("1. Matricular aluno")
    print("2. Desmatricular aluno")
    print("3. Listar matérias do aluno")
    print("4. Listar alunos da matéria")
    print("5. Listar todas as matrículas")
    print("0. Voltar")

if __name__ == "__main__":
    connection = get_connection()
    
    while True:
        menu_principal()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            while True:
                menu_alunos()
                opcao_aluno = input("Escolha uma opção: ")
                
                if opcao_aluno == "1":
                    adicionar_aluno(connection)
                elif opcao_aluno == "2":
                    buscar_aluno(connection)
                elif opcao_aluno == "3":
                    buscar_todos_alunos(connection)
                elif opcao_aluno == "4":
                    atualizaraluno(connection)
                elif opcao_aluno == "5":
                    deletar_aluno(connection)
                elif opcao_aluno == "6":
                    buscar_aluno_por_nome(connection)
                elif opcao_aluno == "0":
                    break
        
        elif opcao == "2":
            while True:
                menu_voluntarios()
                opcao_voluntario = input("Escolha uma opção: ")
                
                if opcao_voluntario == "1":
                    criar_voluntario(connection)
                elif opcao_voluntario == "2":
                    buscar_voluntario(connection)
                elif opcao_voluntario == "3":
                    buscar_todos_voluntarios(connection)
                elif opcao_voluntario == "4":
                    atualizar_voluntario(connection)
                elif opcao_voluntario == "5":
                    deletar_voluntario(connection)
                elif opcao_voluntario == "6":
                    buscar_voluntario_por_cpf(connection)
                elif opcao_voluntario == "0":
                    break
        
        elif opcao == "3":
            while True:
                menu_materias()
                opcao_materia = input("Escolha uma opção: ")
                
                if opcao_materia == "1":
                    criar_materia(connection)
                elif opcao_materia == "2":
                    buscar_materia(connection)
                elif opcao_materia == "3":
                    buscar_todas_materias(connection)
                elif opcao_materia == "4":
                    atualizar_materia(connection)
                elif opcao_materia == "5":
                    deletar_materia(connection)
                elif opcao_materia == "6":
                    buscar_materias_por_voluntario(connection)
                elif opcao_materia == "0":
                    break
        
        elif opcao == "4":
            while True:
                menu_matriculas()
                opcao_matricula = input("Escolha uma opção: ")
                
                if opcao_matricula == "1":
                    matricular_aluno(connection)
                elif opcao_matricula == "2":
                    desmatricular_aluno(connection)
                elif opcao_matricula == "3":
                    listar_materias_do_aluno(connection)
                elif opcao_matricula == "4":
                    listar_alunos_da_materia(connection)
                elif opcao_matricula == "5":
                    listar_todas_matriculas(connection)
                elif opcao_matricula == "0":
                    break
        
        elif opcao == "0":
            print("Saindo do sistema...")
            break
    
    connection.close()

