# https://www.americanas.com.br/busca/s22
import requests
from bs4 import BeautifulSoup
import smtplib
import email.message

def send_email():
    email_content = f'''
    <p> Olá <b>Lucas</b>, tudo bem? </p>
    <p> {texto} </p>
    <p> <b>Celular:</b> {objeto} </p>
    <p> <b>Valor:</b> {preco} </p>
    '''

    msg = email.message.Message()
    msg['Subject'] = 'E-mail enviado com sucesso'
    #'dev.work.az@gmail.com'
    msg['From'] = 'dev.work.az@gmail.com'
    msg['To'] = 'dev.work.az@gmail.com'
    password = 'ymkbompqrnozjrni'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_content)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

    print('Enviado com sucesso!')

link = "https://www.americanas.com.br/busca/s22?limit=24&offset=0"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}

requisicao = requests.get(link, headers=headers)

site = BeautifulSoup(requisicao.content, 'html.parser')

num_tot_prod = site.find("span", class_="emvQCy").get_text().split()[0]
num_tot_prod = num_tot_prod.replace(',', '')
num_tot_prod = int(num_tot_prod)

contar = 0

for i in range(0, 120, 24):

    link = f"https://www.americanas.com.br/busca/s22?limit=24&offset={i}"

    requisicao = requests.get(link, headers=headers)

    site = BeautifulSoup(requisicao.content, 'html.parser')
        
    blocos = site.find_all("div", class_="iRvjrG")

    print(f'{contar}')
    contar = contar + 1

    with open ('precos_s22.csv', 'a', newline='', encoding='UTF-8') as f:

        for bloco in blocos:

            try:
                objeto = bloco.find("h3", class_="gUjFDF").get_text().upper()
                preco = bloco.find("span", class_="liXDNM").get_text().split()[1]
                preco = preco.replace('.', '')
                preco = int(preco[:4])
                link_prod = bloco.find("a", class_="JOEpk").get_text()
            except:
                objeto = bloco.find("h3", class_="gUjFDF").get_text()
                preco = 0

            texto = f'Produto: {objeto} \nValor: {preco}\n'

            if 'S22' in objeto and preco > 1000:

                if preco < 2500:
                    send_email()

                f.write(texto)

print('Análise de dados feita com sucesso!')

    