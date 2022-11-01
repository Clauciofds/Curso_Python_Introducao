class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._like = 0

    @property
    def like(self):
        return self._like

    def dar_like(self):
        self._like += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._like} Likes'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    def __str__(self):
        return (f'{self._nome} - {self.ano} - {self.duracao} '
                f'min {self._like} Like(s)')


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
       super().__init__(nome, ano)
       self.temporadas = temporadas
    def __str__(self):
        return (f'{self._nome} - {self.ano} - {self.temporadas} '
                f'temporadas - {self._like} Like(s)')

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

    @property
    def listagem(self):
        return self._programas

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico',1999,100)
demolidor = Serie('Demolidor',2016,3)

vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series=[vingadores,atlanta,demolidor,tmep]
play_fim_de_semana = Playlist('Play List do fim de semana',
                            filmes_e_series)
print(f'Tamanho do playlist: {len(play_fim_de_semana)}')
print(play_fim_de_semana[1])

for programa in play_fim_de_semana:
    print(programa)

print(f'Demolidor est a na lista? {demolidor in play_fim_de_semana.listagem}')