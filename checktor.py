'''

Autor: Jhonas Henrique
Github: https://github.com/JhonasHenrique
Contato: jhonascontato@gmail.com

'''
#encoding: utf-8

#importando bibliotecas
from lxml import html
from requests import get
from time import sleep
import os

#Boas vindas 
os.system("figlet -c CheckTor")

#Em quanto meu loop for verdadeiro
while(True):
     #Tente fazer 2 requisições
     try:
        #Uma no site oficial da Tor 
        requisicao = get('https://check.torproject.org')
        #Outra nessa api -> Fonerce serviço para verificar endereço ip(internet protocol)
        traz_ip = get('https://api.ipify.org').text
    #Se ambas as requisições falharem
     except:
        #Retorne ao usuário que o mesmo está sem conexão com a internet 
        print('\033[31m'+"Sem conexão com a internet!")
        sleep(5)
   #Caso as requisições sejam efetuadas
     else:
        #Da lib lxml use o modulo html conjunto com a função fromstring()
        documento = html.fromstring(requisicao.content)
        #Coletando dados do site oficial
        dados = documento.xpath('//h1[@class="not"]/text()')
        #Contando retorno do meu list
        conta_retorno = len(dados)
        #Se meu list retornar vazio
        if conta_retorno  == 0:
             #Exiba para o usuário que ele não estabeleceu um circuito tor
             print('\033[31m'+"Não conectado a rede tor! Ip:",traz_ip)
             #Intervalo de looping
             sleep(5)
        #Caso o meu list não retorne vazio
        else:
            #Exiba para o usuário que o mesmo possui uma conexão junto a rede tor
            print('\033[32m'+"Conectado a rede tor! Ip:",traz_ip)
            #intervalo de looping
            sleep(5)

#Fim 




