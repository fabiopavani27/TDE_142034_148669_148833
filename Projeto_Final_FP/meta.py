
class Meta:

    def __init__(self, codigo_meta, nome, indicador,
                 valor_objetivo, relacao):

        self.codigo_meta = codigo_meta
        self.nome = nome
        self.indicador = indicador
        self.valor_objetivo = valor_objetivo
        self.relacao = relacao

    # Métodos para consultar os atributos
    def get_codigo_meta(self):
        return self.codigo_meta

    def get_nome(self):
        return self.nome

    def get_indicador(self):
        return self.indicador

    def get_valor_objetivo(self):
        return self.valor_objetivo

    def get_relacao(self):
        return self.relacao

    # Métodos para alterar os atributos
    def set_nome(self, nome):
        self.nome = nome

    def set_indicador(self, indicador):
        self.indicador = indicador

    def set_valor_objetivo(self, valor):
        self.valor_objetivo = valor

    def set_relacao(self, relacao):
        self.relacao = relacao

    # Verificar se um valor cumpre a meta
    def cumprida(self, valor):

        if self.relacao == ">":
            return valor > self.valor_objetivo

        elif self.relacao == "<":
            return valor < self.valor_objetivo

        elif self.relacao == "==":
            return valor == self.valor_objetivo

        elif self.relacao == ">=":
            return valor >= self.valor_objetivo

        elif self.relacao == "<=":
            return valor <= self.valor_objetivo

        else:
            return False

    # Representação da meta
    def __str__(self):
        return f"Código: {self.codigo_meta}, Nome: {self.nome}, Indicador: {self.indicador}, Valor Objetivo: {self.valor_objetivo}, Relação: {self.relacao}"