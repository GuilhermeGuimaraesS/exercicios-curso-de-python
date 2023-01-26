import urllib.request

try:
    site_pudim = urllib.request.urlopen('http://pudim.com.br/')
    leitura = site_pudim.read()
except:
    print('\033[0;31mO site Pudim não está acessível! \033[m')
else:
    print('\033[0;32mO site Pudim está acessível! \033[m')
    print(site_pudim.read()) # Sugestão do Prof. Guanabara
 