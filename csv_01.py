# CSV (Comma Separated Values - Valores separados por vírgulas)
# É um formato de arquivo que armazena dados em forma de tabela, onde cada
# linha representa uma linha da tabela e as colunas são separadas por vírgulas.
# Ele é amplamente utilizado para transferir dados entre sistemas de diferentes
# plataformas, como por exemplo, para importar ou exportar dados para uma
# planilha (Google Sheets, Excel, LibreOffice Calc) ou para uma base de dados.
# Um arquivo CSV geralmente tem a extensão ".csv" e pode ser aberto em um
# editor de texto ou em uma planilha eletrônica.
# Um exemplo de um arquivo CSV pode ser:
# Nome,Idade,Endereço
# Luiz Otávio,32,"Av Brasil, 21, Centro"
# João da Silva,55,"Rua 22, 44, Nova Era"
# A primeira linha do arquivo define os nomes das colunas da, enquanto as
# linhas seguintes contêm os valores das linhas, separados por vírgulas.
# Regras simples do CSV
# 1 - Separe os valores das colunas com um delimitador único (,)
# 2 - Cada registro deve estar em uma linha
# 3 - Não deixar linhas ou espaços sobrando
# 4 - Use o caractere de escape (") quando o delimitador aparecer no valor.

# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO = Path(__file__).parent / 'csv_01.csv'

# Lendo
with open(CAMINHO, 'r', encoding='utf-8') as arquivo:
  leitor = csv.DictReader(arquivo)
  for linha in leitor:
    print(linha['Nome'], linha['Telefone'], linha['Endereco'])
  arquivo.close()

#Escrevendo
lista = [
  {'Nome': 'Alexandre Araujo', 'Telefone' : '+55(21)98967-5438', 'Endereco': '"Av Victor Kunder 150, apto 22, Barra da Tijuca"'},
  {'Nome': 'João da Silva',  'Telefone': '+55(21)99634-2396', 'Endereco': '"Rua Timoteo da Costa, 21 apto 204, Leblon"'},
  {'Nome': 'Maria Terra',  'Telefone': '+55(21)23467-8509', 'Endereco': '"Av Brasil, 3100 Apt 1208, Centro"'},
  {'Nome': 'Pedro Rodrigues',  'Telefone': '+55(21)33256-9835', 'Endereco': '"Av Gen. San Martin, 240 Apt 302, Leblon"'},
]
with open(CAMINHO, 'w', encoding='utf-8') as arquivo:
  colunas = lista[0].keys()
  escritor = csv.DictWriter(
    arquivo,
    fieldnames=colunas,
    lineterminator = '\n'
  )
  escritor.writeheader()
  for cliente in lista:
    print(cliente)
    escritor.writerow(cliente)
  arquivo.close()