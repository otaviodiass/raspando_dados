from bs4 import BeautifulSoup
import requests

URL = "https://investidor10.com.br/acoes/"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'https://www.referencia.com',
    'Accept-Language': 'pt-BR',
}

def main():
    conteudo = requests.get(url=URL, headers=HEADERS).content

    soup = BeautifulSoup(conteudo, "html.parser")

    dados = soup.find_all('div', class_="actions-card")

    acoes = []

    for i in dados:
        acoes.append(
            {
                'nome': i.find('h3', {'class': 'actions-title'}).text,
                'P/L': i.find_all('span')[1].text.strip(),
                'P/V': i.find_all('span')[3].text.strip(),
                'D/Y': i.find_all('span')[5].text.strip(),
                'ROE': i.find_all('span')[7].text.strip()
            }
        )

    for acao in acoes:
        print(acao)

if __name__ == "__main__":
    main()
