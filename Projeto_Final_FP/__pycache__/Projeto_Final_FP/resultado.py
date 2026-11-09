
class Resultado:

    def __init__(self, codigo_aluno, codigo_atividade,
                 estado, classificacao, tempo_gasto_min):

        self.codigo_aluno = codigo_aluno
        self.codigo_atividade = codigo_atividade
        self.estado = estado
        self.classificacao = classificacao
        self.tempo_gasto_min = tempo_gasto_min

    # Métodos para consultar os atributos
    def get_codigo_aluno(self):
        return self.codigo_aluno

    def get_codigo_atividade(self):
        return self.codigo_atividade

    def get_estado(self):
        return self.estado

    def get_classificacao(self):
        return self.classificacao

    def get_tempo_gasto_min(self):
        return self.tempo_gasto_min

    # Métodos para alterar os atributos
    def set_estado(self, estado):
        self.estado = estado

    def set_classificacao(self, classificacao):
        self.classificacao = classificacao

    def set_tempo_gasto_min(self, tempo):
        self.tempo_gasto_min = tempo

    # Representação do resultado
    def __str__(self):

        return (f"Aluno: {self.codigo_aluno} - "
                f"Atividade: {self.codigo_atividade} - "
                f"Estado: {self.estado} - "
                f"Classificação: {self.classificacao} - "
                f"Tempo: {self.tempo_gasto_min} minutos")
