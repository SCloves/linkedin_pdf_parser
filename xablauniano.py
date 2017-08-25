# encoding: utf-8
import re

class Xablauniano():
    
    def __init__(self, lista):
        self.name =  lista[0]
        self.profession = lista[1]
        self.email = lista[2]
        self.summary = ''.join(lista[lista.index('Summary') +1: lista.index('Experience')])
        self.experience = parse_experience(lista[lista.index('Experience') +1: lista.index('Education')])
        self.education = lista[lista.index('Education') +1: ]
    


def parse_experience(lista):
    indexs = get_index_experience(lista)
    titles = [lista[i-1] for i in indexs]
    periods = [lista[i] for i in indexs]
    description = []
    for i in range(len(indexs)):
        if i < len(indexs) - 1:
            description.append(lista[indexs[i]+1 : indexs[i+1]-1])
        else:
            description.append(lista[indexs[i]+1:])

    return  {i:(title, period, ''.join(descr)) for i, title, period, descr 
                  in zip(range(len(titles)),titles, periods, description)}


def get_index_experience(lista):
    return [i for i in range(len(lista)) if re.search(r'[12]\d{3}', lista[i]) 
            and 'de' in lista[i] and '-' in lista[i]]