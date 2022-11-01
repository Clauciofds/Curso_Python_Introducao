class Datas:
    def __init__(self):
        self.dia=''
        self.mes=''
        self.ano=''

    def definir_data(self):
        self.dia=input('Dia:')
        self.mes=input('Mês:')
        self.ano=input('Ano:')

    def formatada(self):
        print(f'{self.dia}/{self.mes}/{self.ano}')

