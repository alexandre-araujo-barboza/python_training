# (Parte 1) Básico do protocolo HTTP (HyperText Transfer Protocol)
# HTTP (HyperText Transfer Protocol) é um protocolo usado enviar e receber
# dados na Internet. Ele funciona no modo cliente/servidor, onde o cliente
# (seu navegador, por exemplo) faz uma requisição ao servidor
# (site, por exemplo), que responde com os dados adequados.
#
# A mensagem de requisição do cliente deve incluir dados como:
# - O método HTTP
#     - leitura (safe) - GET, HEAD (cabeçalhos), OPTIONS (métodos suportados)
#     - escrita - POST, PUT (substitui), PATCH (atualiza), DELETE
# - O endereço do recurso a ser acessado (/users/)
# - Os cabeçalhos HTTP (Content-Type, Authorization)
# - O Corpo da mensagem (caso necessário, de acordo com o método HTTP)
#
# A mensagem de resposta do servidor deve incluir dados como:
# - código de status HTTP (200 success, 404 Not found, 301 Moved Permanently)
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
# - Os cabeçalhos HTTP (Content-Type, Accept)
# - O corpo da mensagem (Pode estar em vazio em alguns casos)
# requests para requisições HTTP
# Tutorial -> https://youtu.be/Qd8JT0bnJGs
# Web Scraping com Python usando requests e bs4 BeautifulSoup
# - Web Scraping é o ato de "raspar a web" buscando informações de forma
# automatizada, com determinada linguagem de programação, para uso posterior.
# - O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
# + Instalação
# - pip install requests types-requests bs4
# - python -m http.server -d C:\Users\Alexandre\Documents\Projetos\Python\Udemy\ 3333
import re

import requests
from bs4 import BeautifulSoup

url = 'https://alexandrebarboza.freevar.com/servicos.php' 
response = requests.get(url)
bytes = response.content
html = BeautifulSoup(bytes, 'html.parser', from_encoding='utf-8')

#if html.title is not None:
#  print(html.title.text)

#h2 = html.select_one('h2')
#if h2 is not None:
#  print(re.sub(r'\s{1,}', ' ', h2.text).strip())
  
h3 = html.select_one('h3')
if h3 is not None:
  print(re.sub(r'\s{1,}', ' ', h3.text).strip())
  next = h3.find_next()
  if next is not None:
    for block in next.select('blockquote'):
      print(re.sub(r'\s{1,}', ' ', block.text).strip())
      