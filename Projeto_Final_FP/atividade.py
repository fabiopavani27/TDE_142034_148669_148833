
class Atividade:

    def __init__(self, codigo_atividade, titulo, tema, tipo, duracao_prevista_min):
        self.codigo_atividade = codigo_atividade
        self.titulo = titulo
        self.tema = tema
        self.tipo = tipo
        self.duracao_prevista_min = duracao_prevista_min

    # Métodos para consultar os atributos
    def get_codigo_atividade(self):
        return self.codigo_atividade

    def get_titulo(self):
        return self.titulo

    def get_tema(self):
        return self.tema

    def get_tipo(self):
        return self.tipo

    def get_duracao_prevista_min(self):
        return self.duracao_prevista_min

    # Métodos para alterar os atributos
    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_tema(self, tema):
        self.tema = tema

    def set_tipo(self, tipo):
        self.tipo = tipo

    def set_duracao_prevista_min(self, duracao):
        self.duracao_prevista_min = duracao

    # Representação da atividade
    def __str__(self):
        return f"Código: {self.codigo_atividade}, Título: {self.titulo}, Tema: {self.tema}, Tipo: {self.tipo}, Duração Prevista (min): {self.duracao_prevista_min}"
