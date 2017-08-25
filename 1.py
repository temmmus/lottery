import requests
from bs4 import BeautifulSoup
import csv

def get_html(url): # 3. Результат функции - HTML-код страницы
    response = requests.get(url)
    return response.text #3.1. Возвращает HTML-код страницы

def parse(html): #5. Результат функции - возвращает данные из HTML-тэга <b>, находящегося в тэге <div class='container cleared'>
    soup = BeautifulSoup(html, 'lxml')
    divTag = soup.find_all('div', class_='container cleared')
    for b in divTag:
        bTags = b.find('b')
        for b in bTags:
            print(b)
            # return b

def save(b): #7. Результат функции - сохранение в csv-файл
    with open('numbers.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(('Номер1', 'Номер2', 'Номер3', 'Номер4', 'Номер5', 'Номер6'))


def main():
    url = 'http://www.stoloto.ru/6x45/archive?firstDraw=1&lastDraw=3125&mode=draw' #1. Взяли адрес страницы и записали в переменную url

    all_numbers = parse(get_html(url)) #2. Передали url в функцию get_html 4. Передали код страницы в функицию parse



if __name__ == '__main__':
    main()

