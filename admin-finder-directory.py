import requests
import sys
import os


vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'
ciano = '\033[36m'
magenta = '\033[35m'
amarelo = '\033[1;33m'
preto = '\033[30m'
branco = '\033[37m'
original = '\033[0;0m'
reverso = '\033[2m'
default1 = '\033[0m'

os.system("clear")
about = '''
                 ____  _               _                   
                |  _ \(_)_ __ ___  ___| |_ ___  _ __ _   _ 
                | | | | | '__/ _ \/ __| __/ _ \| '__| | | |
                | |_| | | | |  __/ (__| || (_) | |  | |_| |
                |____/|_|_|  \___|\___|\__\___/|_|   \__, |
                                                      |___/                                          

              Coded by: leo_guei ==> github.com/Leo_FuckOff
		'''

print (vermelho+about)


url = raw_input(azul+"[!] Site ==> "+verde)
arq = open(raw_input(azul+"\n[!] Wordlist ==> "+verde))
print ciano+"\n[!] Aguarde ate o programa finalizar os testes!\n"
print ciano+"============[+]============[+]============[+]============\n"
lines = arq.readlines()
arq.close()

def main():
	try:
		for line in lines:
			request = url+"/"+line
			recv = requests.get(request)
			code = recv.status_code
			if code != 404:
				if not "Page not found" in recv:
					print verde+"[+] Pagina encontrada ==> ", request[:-2],"\n"
				else:
					print vermelho+"[-] Pagina nao encontrada ==>", request[:-2],"\n"
			else:
				print vermelho+"[-] Pagina nao encontrada ==>", request[:-2],"\n"
	except:
		pass


if __name__ == "__main__":
	main() 
