import requests
from bs4 import BeautifulSoup
import csv

baseurl = 'http://www.stoloto.ru/6x45/archive?firstDraw=1&lastDraw=3125&mode=draw'

def get_html(url):
    response = requests.get(url)
    return response.text

def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    divTag = soup.find_all('div', class_='container cleared')
    for b in divTag:
        bTags = b.find('b')
        for b in bTags:
            # return b
            print(b)

def save(numbers):
    with open('numbers.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(('Номер1', 'Номер2', 'Номер3', 'Номер4', 'Номер5', 'Номер6'))


def main():
    numbers = parse(get_html(baseurl))
    # print(numbers)
    save(numbers)


if __name__ == '__main__':
    main()

