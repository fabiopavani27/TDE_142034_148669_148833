
class Aluno:

    def __init__(self, codigo_aluno, nome, turma):
        self.codigo_aluno = codigo_aluno
        self.nome = nome
        self.turma = turma

    def get_codigo_aluno(self):
        return self.codigo_aluno

    def get_nome(self):
        return self.nome

    def get_turma(self):
        return self.turma

    def set_nome(self, nome):
        self.nome = nome

    def set_turma(self, turma):
        self.turma = turma

    def __str__(self):
        return self.codigo_aluno + " - " + self.nome + " - " + self.turma
