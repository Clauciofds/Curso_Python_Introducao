class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print('Construindo objeto ... {}'. format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self,valor_a_sacar):
        return valor_a_sacar <= self.__saldo+self.__limite

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo-=valor
            print('Saque efetuado. Seu salde é {}.'.format(self.__saldo))
        else:
            print('O valor {} é maior que seu limite!'.format(valor))

    def transfere(self,valor,destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular.title()
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self,limite):
        self.__limite=limite

    @staticmethod
    def codigos():
        dicionario_original={'BB':'001','Caixa':'104','Bradesco':'237'}
        dicionario_novo={}
        for chave, valor in dicionario_original.items():
            dicionario_novo[chave.upper()]=valor
        return dicionario_novo