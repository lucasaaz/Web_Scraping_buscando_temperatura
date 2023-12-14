# Web Scraping - Buscar Temperatura Atual

Este código em Python realiza a extração de informações da previsão do tempo para Belo Horizonte, MG, a partir do site "Climatempo". Vamos analisar o código passo a passo:

1 - Importação de Bibliotecas:

* import requests
** from bs4 import BeautifulSoup

Aqui, são importadas as bibliotecas requests para fazer requisições HTTP e BeautifulSoup para fazer a análise do HTML.


2 - Definição do Link e Cabeçalhos HTTP:

* link = 'https://www.climatempo.com.br/previsao-do-tempo/15-dias/cidade/107/belohorizonte-mg'
* user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
* headers = {"User-Agent": user_agent}

É definido o link da página da previsão do tempo para Belo Horizonte e um cabeçalho (User-Agent) para simular uma requisição feita por um navegador web.


3 - Realização da Requisição HTTP:

* requisicao = requests.get(link, headers=headers)

O código faz uma requisição HTTP à página da web usando o link e os cabeçalhos definidos.


4 - Análise do Conteúdo HTML:

* site = BeautifulSoup(requisicao.text, 'html.parser')

A biblioteca BeautifulSoup é usada para analisar o conteúdo HTML da página, facilitando a extração de informações específicas.


5 - Extração da Temperatura Mínima e Máxima:

* temp_min = site.find("span", class_='_margin-r-15')
* temperatura = site.find("div", class_='-gray _flex _margin-l-5').get_text().strip().split()

Aqui, o código procura no HTML os elementos que contêm as informações de temperatura mínima e máxima. Essas informações são extraídas e formatadas para exibição.


6 - Exibição dos Resultados:

* print(f'\n BELO HORIZONTE\n')
* print(f' Temperatura mínima: {temperatura[0]} \n Temperatura máxima: {temperatura[1]}\n')

Por fim, o código imprime na tela as informações da temperatura mínima e máxima para Belo Horizonte.

Resumindo, o código realiza scraping na página da previsão do tempo do Climatempo para Belo Horizonte, extrai e exibe as informações de temperatura mínima e máxima.
