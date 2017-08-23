# README

### Objetivo:
 Extrair infromações do corrículo em pdf obtido no linkedin de um Xablauniano
 
### Como rodar:

```
mkvirtualenv -p python2.7 .env
source ./.env/bin/activate
pip install -r requirements.txt
```

### Como usar:

No arquivo main.py há uma função chamada expert() que pode ser exportada. Essa função recebe o path onde se encontra o arquivo em pdf e retorna uma objeto Xablauniano que tem os seguintes atributos:

- name
- profession
- summary
- experience
- education