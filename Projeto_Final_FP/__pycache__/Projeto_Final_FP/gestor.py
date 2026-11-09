
class Gestor:

    def __init__(self, alunos, atividades, resultados):
        self.alunos = alunos
        self.atividades = atividades
        self.resultados = resultados
        self.metas = []

    # Devolver a lista de alunos
    def get_alunos(self):
        return self.alunos

    # Devolver a lista de atividades
    def get_atividades(self):
        return self.atividades

    # Devolver a lista de resultados
    def get_resultados(self):
        return self.resultados

    # Devolver a lista de metas
    def get_metas(self):
        return self.metas

    # Listar todos os alunos
    def listar_alunos(self):
        for aluno in self.alunos:
            print(aluno)

    # Listar alunos de uma turma
    def listar_alunos_turma(self, turma):
        encontrados = 0

        for aluno in self.alunos:
            if aluno.get_turma() == turma:
                print(aluno)
                encontrados += 1

        if encontrados == 0:
            print("Não existem alunos nessa turma.")

    # Procurar um aluno pelo código
    def procurar_aluno(self, codigo):
        for aluno in self.alunos:
            if aluno.get_codigo_aluno() == codigo:
                return aluno

        return None

    # Calcular os indicadores de um aluno
    def calcular_indicadores(self, codigo_aluno):

        aluno = self.procurar_aluno(codigo_aluno)

        if aluno is None:
            print("Aluno não encontrado.")
            return None

        total_atividades = len(self.atividades)
        concluidas = 0
        classificacoes = []
        tempo_total = 0

        for resultado in self.resultados:

            if resultado.get_codigo_aluno() == codigo_aluno:

                tempo_total += resultado.get_tempo_gasto_min()

                if resultado.get_estado() == "concluida":
                    concluidas += 1

                    classificacao = resultado.get_classificacao()

                    if classificacao is not None:
                        classificacoes.append(classificacao)

        # Taxa de conclusão
        if total_atividades > 0:
            taxa_conclusao = (concluidas / total_atividades) * 100
        else:
            taxa_conclusao = None

        # Classificação média
        if len(classificacoes) > 0:
            classificacao_media = sum(classificacoes) / len(classificacoes)
        else:
            classificacao_media = None

        return {
            "taxa_conclusao": taxa_conclusao,
            "classificacao_media": classificacao_media,
            "tempo_total": tempo_total
        }

    # Consultar indicadores de um aluno
    def consultar_aluno(self, codigo_aluno):

        indicadores = self.calcular_indicadores(codigo_aluno)

        if indicadores is None:
            return

        print("\n--- INDICADORES DO ALUNO ---")
        print("Taxa de conclusão:", indicadores["taxa_conclusao"])
        print("Classificação média:", indicadores["classificacao_media"])
        print("Tempo total:", indicadores["tempo_total"], "minutos")

    # Comparar dois alunos
    def comparar_alunos(self, codigo1, codigo2):

        indicadores1 = self.calcular_indicadores(codigo1)
        indicadores2 = self.calcular_indicadores(codigo2)

        if indicadores1 is None or indicadores2 is None:
            return

        print("\n--- COMPARAÇÃO DE ALUNOS ---")

        print("\nAluno 1:", codigo1)
        print(indicadores1)

        print("\nAluno 2:", codigo2)
        print(indicadores2)
