'''

Autor: Jhonas Henrique
Github: https://github.com/JhonasHenrique
Contato: jhonascontato@gmail.com

'''

#encoding: utf-8

from os import system
from time import sleep

try:
   system("sudo apt-get install python3 -y")
   system("sudo apt-get update -y")
   system("sudo apt-get install figlet")
   system("clear")
   system("figlet -c Concluido!")
   sleep(1.5)
   system("clear")
   system("figlet -c checktor.py")
   sleep(1.5)
   system("clear")
   system("figlet -c Pronto")
   sleep(1.5)
   system("clear")
   system("figlet -c Para")
   sleep(1.5)
   system("clear")
   system("figlet -c Uso!")
   sleep(1.5)
   system("clear")
except:
   print('\033[31m'+"Ocorreu um erro inesperado ao instalar as dependencias!")
   exit()
else:  
   pass
finally:
   pass

exit()
#Fim
