from gestor import Gestor

def executar_menu():
    gestor = Gestor()

    while True:
        print("\nACOMPANHAMENTO DA APRENDIZAGEM DIGITAL")
        print("1 Carregar datasets")
        print("2 Listar alunos")
        print("3 Consultar indicadores de um aluno")
        print("4 Comparar indicadores entre dois alunos")
        print("5 Criar meta de aprendizagem")
        print("6 Listar metas")
        print("7 Editar meta")
        print("8 Apagar meta")
        print("9 Visualizar alunos que cumprem uma meta")
        print("0 Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == '1':
            gestor.carregar_datasets()
        elif opcao in ['2', '3', '4', '9']:
            if not gestor.lista_alunos:
                print("Aviso: É necessário carregar os dados primeiro (Opção 1).")
            else:
                if opcao == '2':
                    gestor.listar_alunos()
                elif opcao == '3':
                    gestor.consultar_aluno()
                elif opcao == '4':
                    gestor.comparar_alunos()
                elif opcao == '9':
                    gestor.visualizar_alunos_cumprem_meta()
        elif opcao == '5':
            gestor.criar_meta()
        elif opcao == '6':
            gestor.listar_metas()
        elif opcao == '7':
            gestor.editar_meta()
        elif opcao == '8':
            gestor.apagar_meta()
        elif opcao == '0':
            print("A sair do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    executar_menu()