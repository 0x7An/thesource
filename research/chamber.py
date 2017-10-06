import requests
from bs4 import BeautifulSoup
import pandas as pd

URL_BASE = "http://www.camara.gov.br/proposicoesWeb/fichadetramitacao?idProposicao="
PROPOSAL = "961710"

page = requests.get(URL_BASE + PROPOSAL)
soup = BeautifulSoup(page.content, 'html.parser')

#Load the csv file with proposals, and interate over cod_proposal to get the ementa description.

#Clusterize the temas proposal over partidos, parlamentares trough the years.
#

txtIndex = soup.find_all(id="textoIndexacao")
txtNomeProposal = soup.find_all(class_="nomeProposicao")
txtAutor = soup.find_all(id="colunaPrimeiroAutor")
txtEmenta = soup.find_all('strong', class_='textoJustificado')

print("Nome :" + txtNomeProposal[0].get_text())
print(txtAutor[0].get_text())
print("Indexação :")
print(txtIndex[0].get_text().split(","))
print(txtEmenta)
