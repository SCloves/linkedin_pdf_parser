# encoding: utf-8


class Xablauniano():
    
    def __init__(self, lista):
        self.name =  lista[0]
        self.profession = lista[1]
        self.summary = ''.join(lista[lista.index('Summary') +1: lista.index('Experience')])
        self.experience = ''.join(lista[lista.index('Experience') +1: lista.index('Education')])
        self.education = lista[lista.index('Education') +1]
    