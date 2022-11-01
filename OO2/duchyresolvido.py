class MinhaLista:
    def __init__(self, *items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return self.items.__iter__()

    def __str__(self):
        return f'{list(self.items)}'

    def __getitem__(self, key):
        return self.items[key]

lista = MinhaLista(1, 2, 3, 4)
print(lista)
for tes in lista:
    print(tes)
