import requests
from bs4 import BeautifulSoup
import config

def get_response():
    url = config.url
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

    # Теперь вы можете использовать BeautifulSoup для извлечения информации из HTML-кода
    # Например, вы можете извлечь заголовки объявлений:
        titles = soup.find_all('a', class_='marginright5 link linkWithHash detailsLink')

        for title in titles:
            print(title.text.strip())
    else:
        print(f"Ошибка запроса: {response.status_code}")

