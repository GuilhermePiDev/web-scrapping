import pandas as pd


""" Fazend com array, apenas informar o indice da array"""

""" urls = ["https://dadosabertos.rfb.gov.br/CNPJ/Cnaes.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Empresas0.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Empresas1.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Empresas2.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Empresas3.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Empresas4.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Empresas5.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Empresas6.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Empresas7.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Empresas8.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Empresas9.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Estabelecimentos0.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Estabelecimentos1.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Estabelecimentos2.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Estabelecimentos3.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Estabelecimentos4.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Estabelecimentos5.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Estabelecimentos6.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Estabelecimentos7.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Estabelecimentos8.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Estabelecimentos9.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Motivos.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Municipios.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Naturezas.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Paises.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Qualificacoes.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Simples.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Socios0.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Socios1.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Socios2.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Socios3.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Socios4.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Socios5.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Socios6.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Socios7.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Socios8.zip",
       "https://dadosabertos.rfb.gov.br/CNPJ/Socios9.zip",
       ]
tabelaArray = pd.read_csv(urls[0], sep=";", encoding="latin1", low_memory=False) 

print(tabelaArray) """


""" Fazend com uma function, apenas informar o nome do arquivo zipado quando executar o msm """
def webS (arquivo ):
    url = f"https://dadosabertos.rfb.gov.br/CNPJ/{arquivo}.zip"
    tabela = pd.read_csv(url, sep=";", encoding="latin1", low_memory=False)
    print(tabela)

webS("Socios1") 


