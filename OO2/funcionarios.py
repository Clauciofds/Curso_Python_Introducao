class Funcionario:
    def registra_hora(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

    def __init__(self,nome):
        self.nome=nome

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostraando cursos desse mes')

class Alura(Funcionario):
    #def mostrar_tarefas(self):
    #    print('Fez muita coisa, Alurete')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando Pergunta nao respondidas do forum')

class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'

class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass

class Senior(Alura, Caelum, Hipster):
    pass

jose = Junior()
jose.busca_perguntas_sem_resposta()
jose.mostrar_tarefas()

luan = Pleno()
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()

luan.mostrar_tarefas()

miro=Senior('MIro')
print(miro)
