import pandas as pd
from urllib.request import urlretrieve

#http://www.camara.gov.br/internet/arquivosDadosAbertos/proposicoes.csv
#local_filename, headers = urllib.request.urlretrieve('http://www.camara.gov.br/internet/arquivosDadosAbertos/proposicoes.csv')

#data = pd.read_csv('proposicoes.csv', sep=';',error_bad_lines=False)
#print(data.readline())

with open('proposicoes.csv', 'r') as file:
    print(file.readline()) 
    print(file.readline())