class Jogo:
    def __init__(self,nome,vezes_quejoguei):
        print(f'Objto construido {self}')
        self.__nome=nome
        self.__vezes_quejoguei=vezes_quejoguei

    def set_nome(self,nome):
        self.__nome=nome
    def set_vezer_quejoguei(self,vezes_quejoguei):
        self.__vezes_quejoguei=vezes_quejoguei

    def get_nome(self):
        return self.__nome
    def get_vezes_quejoguei(self):
        return self.__vezes_quejoguei