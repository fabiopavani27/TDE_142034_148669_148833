import csv
import os

from aluno import Aluno
from atividade import Atividade
from resultado import Resultado


class GestorDados:

    def __init__(self):
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        self.pasta_datasets = os.path.join(diretorio_atual, "Datasets")

    def carregar_datasets(self):
        try:
            ficheiro_alunos = open(os.path.join(self.pasta_datasets, "alunos.csv"), "r", encoding="latin-1")
            ficheiro_alunos.close()

            ficheiro_atividades = open(os.path.join(self.pasta_datasets, "atividades.csv"), "r", encoding="latin-1")
            ficheiro_atividades.close()

            ficheiro_resultados = open(os.path.join(self.pasta_datasets, "resultados.csv"), "r", encoding="latin-1")
            ficheiro_resultados.close()

        except OSError:
            print("Erro: Nao foi possivel encontrar ou abrir os ficheiros CSV.")
            return None

        # Carregar os tres conjuntos de dados
        try:
            alunos = self.carregar_alunos()
            atividades = self.carregar_atividades()
            resultados = self.carregar_resultados(alunos, atividades)

            return alunos, atividades, resultados

        except (OSError, UnicodeError, csv.Error) as erro:
            print("Erro na leitura dos ficheiros:", erro)
            return None

    # --------------------------------
    # CARREGAR ALUNOS
    # --------------------------------

    def carregar_alunos(self):
        lista_alunos = []
        codigos = []
        rejeitados = 0

        caminho = os.path.join(self.pasta_datasets, "alunos.csv")
        with open(caminho, "r", encoding="latin-1") as ficheiro:
            leitor = csv.reader(ficheiro, delimiter=";")
            next(leitor, None)

            for linha in leitor:
                try:
                    if len(linha) != 3:
                        raise ValueError()

                    codigo = linha[0].strip()
                    nome = linha[1].strip()
                    turma = linha[2].strip()

                    if codigo == "" or nome == "" or turma == "":
                        raise ValueError()

                    if codigo in codigos:
                        raise ValueError()

                    aluno = Aluno(codigo, nome, turma)
                    lista_alunos.append(aluno)
                    codigos.append(codigo)

                except ValueError:
                    rejeitados += 1
                    print("Aluno rejeitado:", linha)

        print("\n--- ALUNOS ---")
        print("Alunos carregados:", len(lista_alunos))
        print("Alunos rejeitados:", rejeitados)

        return lista_alunos

    # --------------------------------
    # CARREGAR ATIVIDADES
    # --------------------------------

    def carregar_atividades(self):
        lista_atividades = []
        codigos = []
        rejeitados = 0
        tipos_validos = ["quiz", "exercicio", "video", "leitura"]

        caminho = os.path.join(self.pasta_datasets, "atividades.csv")
        with open(caminho, "r", encoding="latin-1") as ficheiro:
            leitor = csv.reader(ficheiro, delimiter=";")
            next(leitor, None)

            for linha in leitor:
                try:
                    if len(linha) != 5:
                        raise ValueError()

                    codigo = linha[0].strip()
                    titulo = linha[1].strip()
                    tema = linha[2].strip()
                    tipo = linha[3].strip()
                    duracao = float(linha[4].strip())

                    if codigo == "" or titulo == "" or tema == "":
                        raise ValueError()

                    if tipo not in tipos_validos:
                        raise ValueError()

                    if duracao <= 0:
                        raise ValueError()

                    if codigo in codigos:
                        raise ValueError()

                    atividade = Atividade(codigo, titulo, tema, tipo, duracao)
                    lista_atividades.append(atividade)
                    codigos.append(codigo)

                except ValueError:
                    rejeitados += 1
                    print("Atividade rejeitada:", linha)

        print("\n--- ATIVIDADES ---")
        print("Atividades carregadas:", len(lista_atividades))
        print("Atividades rejeitadas:", rejeitados)

        return lista_atividades

    # --------------------------------
    # CARREGAR RESULTADOS
    # --------------------------------

    def carregar_resultados(self, lista_alunos, lista_atividades):
        lista_resultados = []
        pares = []
        rejeitados = 0

        codigos_alunos = [aluno.get_codigo_aluno() for aluno in lista_alunos]
        codigos_atividades = [atividade.get_codigo_atividade() for atividade in lista_atividades]

        caminho = os.path.join(self.pasta_datasets, "resultados.csv")
        with open(caminho, "r", encoding="latin-1") as ficheiro:
            leitor = csv.reader(ficheiro, delimiter=";")
            next(leitor, None)

            for linha in leitor:
                try:
                    if len(linha) != 5:
                        raise ValueError()

                    codigo_aluno = linha[0].strip()
                    codigo_atividade = linha[1].strip()
                    estado = linha[2].strip()
                    classificacao_texto = linha[3].strip()
                    tempo = float(linha[4].strip())

                    if codigo_aluno not in codigos_alunos or codigo_atividade not in codigos_atividades:
                        raise ValueError()

                    if estado not in ["em_curso", "concluida"]:
                        raise ValueError()

                    if tempo < 0:
                        raise ValueError()

                    if classificacao_texto == "":
                        classificacao = None
                    else:
                        classificacao = float(classificacao_texto)
                        if classificacao < 0 or classificacao > 100 or estado != "concluida":
                            raise ValueError()

                    par = (codigo_aluno, codigo_atividade)
                    if par in pares:
                        raise ValueError()

                    resultado = Resultado(codigo_aluno, codigo_atividade, estado, classificacao, tempo)
                    lista_resultados.append(resultado)
                    pares.append(par)

                except ValueError:
                    rejeitados += 1
                    print("Resultado rejeitado:", linha)

        print("\n--- RESULTADOS ---")
        print("Resultados carregados:", len(lista_resultados))
        print("Resultados rejeitados:", rejeitados)

        return lista_resultados