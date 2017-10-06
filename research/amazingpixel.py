import requests
from bs4 import BeautifulSoup

URL_BASE = "http://www.camara.gov.br/proposicoesWeb/fichadetramitacao?idProposicao="
PROPOSAL = "961710"

page = requests.get("http://amazingpixel.blogspot.com.br/2002_03_10_archive.html?m=1")
soup = BeautifulSoup(page.content, 'html.parser')

txtIndex = soup.find_all(class_="post-body entry-content")
# txtNomeProposal = soup.find_all(class_="nomeProposicao")
# txtAutor = soup.find_all(id="colunaPrimeiroAutor")
# txtEmenta = soup.find_all('strong', class_='textoJustificado')

# print("Nome :" + txtNomeProposal[0].get_text())
# print(txtAutor[0].get_text())
# print("Indexação :")
# print(txtIndex[0].get_text().split(","))
print(txtIndex)