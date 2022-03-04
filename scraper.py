import requests
from bs4 import BeautifulSoup
from csv import writer

url = 'https://www.google.com/search?q=ssd&sxsrf=APq-WBv1oUs97RrFdLj28hzEL8PtBJRirw:1646434062782&source=lnms&tbm=shop&sa=X&ved=2ahUKEwiS9tTrxK32AhVnr5UCHapICP0Q_AUoAXoECAEQAw&biw=2844&bih=1076&dpr=0.9'
headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0'}
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

lista = soup.find_all('div', class_='i0X6df')

with open('aps.csv', 'a', encoding='utf8', newline='') as f:
    escrever = writer(f)
    
    for item in lista:
        NOME = item.find('h4', class_='Xjkr3b').text.replace('\n', '')
        PRECO = item.find('span', class_='a8Pemb OFFNJ').text.replace('\n', '')
        LOJA = item.find('div', class_='aULzUe IuHnof').text.replace('\n', '')
        
        dados = [NOME, PRECO, LOJA]
        escrever.writerow(dados)