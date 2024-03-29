# -*- coding: utf-8 -*-
"""
Spyder Editor

lista relação de arquivos na página de dados públicos da receita federal
"""


def lista_url():
    url = 'https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj'
    url = 'http://200.152.38.155/CNPJ/'
    from bs4 import BeautifulSoup, SoupStrainer
    import requests

    page = requests.get(url)
    data = page.text
    soup = BeautifulSoup(data)

    for link in soup.find_all('a'):
        if str(link.get('href')).endswith('.zip'):
            cam = link.get('href')
            # if cam.startswith('http://http'):
            #     cam = 'http://' + cam[len('http://http//'):]
            if not cam.startswith('http'):
                print(url+cam)
            else:
                print(cam)

    '''
    http://200.152.38.155/CNPJ/F.K03200$W.SIMPLES.CSV.D10814.zip
    http://200.152.38.155/CNPJ/F.K03200$Z.D10814.CNAECSV.zip
    http://200.152.38.155/CNPJ/F.K03200$Z.D10814.MOTICSV.zip
    http://200.152.38.155/CNPJ/F.K03200$Z.D10814.MUNICCSV.zip
    http://200.152.38.155/CNPJ/F.K03200$Z.D10814.NATJUCSV.zip
    http://200.152.38.155/CNPJ/F.K03200$Z.D10814.PAISCSV.zip
    http://200.152.38.155/CNPJ/F.K03200$Z.D10814.QUALSCSV.zip
    http://200.152.38.155/CNPJ/K3241.K03200Y0.D10814.EMPRECSV.zip
    http://200.152.38.155/CNPJ/K3241.K03200Y0.D10814.ESTABELE.zip
    http://200.152.38.155/CNPJ/K3241.K03200Y0.D10814.SOCIOCSV.zip
    http://200.152.38.155/CNPJ/K3241.K03200Y1.D10814.EMPRECSV.zip
    http://200.152.38.155/CNPJ/K3241.K03200Y1.D10814.ESTABELE.zip
    http://200.152.38.155/CNPJ/K3241.K03200Y1.D10814.SOCIOCSV.zip
    http://200.152.38.155/CNPJ/K3241.K03200Y2.D10814.EMPRECSV.zip
    http://200.152.38.155/CNPJ/K3241.K03200Y2.D10814.ESTABELE.zip
    http://200.152.38.155/CNPJ/K3241.K03200Y2.D10814.SOCIOCSV.zip
    http://200.152.38.155/CNPJ/K3241.K03200Y3.D10814.EMPRECSV.zip
    http://200.152.38.155/CNPJ/K3241.K03200Y3.D10814.ESTABELE.zip
    http://200.152.38.155/CNPJ/K3241.K03200Y3.D10814.SOCIOCSV.zip
    http://200.152.38.155/CNPJ/K3241.K03200Y4.D10814.EMPRECSV.zip
    http://200.152.38.155/CNPJ/K3241.K03200Y4.D10814.ESTABELE.zip
    http://200.152.38.155/CNPJ/K3241.K03200Y4.D10814.SOCIOCSV.zip
    http://200.152.38.155/CNPJ/K3241.K03200Y5.D10814.EMPRECSV.zip
    http://200.152.38.155/CNPJ/K3241.K03200Y5.D10814.ESTABELE.zip
    http://200.152.38.155/CNPJ/K3241.K03200Y5.D10814.SOCIOCSV.zip
    http://200.152.38.155/CNPJ/K3241.K03200Y6.D10814.EMPRECSV.zip
    http://200.152.38.155/CNPJ/K3241.K03200Y6.D10814.ESTABELE.zip
    http://200.152.38.155/CNPJ/K3241.K03200Y6.D10814.SOCIOCSV.zip
    http://200.152.38.155/CNPJ/K3241.K03200Y7.D10814.EMPRECSV.zip
    http://200.152.38.155/CNPJ/K3241.K03200Y7.D10814.ESTABELE.zip
    http://200.152.38.155/CNPJ/K3241.K03200Y7.D10814.SOCIOCSV.zip
    http://200.152.38.155/CNPJ/K3241.K03200Y8.D10814.EMPRECSV.zip
    http://200.152.38.155/CNPJ/K3241.K03200Y8.D10814.ESTABELE.zip
    http://200.152.38.155/CNPJ/K3241.K03200Y8.D10814.SOCIOCSV.zip
    http://200.152.38.155/CNPJ/K3241.K03200Y9.D10814.EMPRECSV.zip
    http://200.152.38.155/CNPJ/K3241.K03200Y9.D10814.ESTABELE.zip
    http://200.152.38.155/CNPJ/K3241.K03200Y9.D10814.SOCIOCSV.zip
    '''


# lista_url()
