import requests
from bs4 import BeautifulSoup
import csv

baseurl = 'http://www.stoloto.ru/6x45/archive?firstDraw=1&lastDraw=3125&mode=draw'

def get_html(url):
    response = requests.get(url)
    return response.text

def parser(html):
    soup = BeautifulSoup(html, 'lxml')
    body = soup.find('body')
    for div in body.find_all('div', class_='container cleared'):
        b1 = div.find_all('b')[0].text.strip()
        b2 = div.find_all('b')[1].text.strip()
        b3 = div.find_all('b')[2].text.strip()
        b4 = div.find_all('b')[3].text.strip()
        b5 = div.find_all('b')[4].text.strip()
        b6 = div.find_all('b')[5].text.strip()
        data = {'Number1':b1,
                'Number2':b2,
                'Number3':b3,
                'Number4':b4,
                'Number5':b5,
                'Numberр6':b6}
        save(data)
        # print(data)

def save(data):
    with open('numbers.csv', 'a', newline='') as csvfile: #a – значит append, т.е. запись идет в конце файла numbers.csv
        writer = csv.writer(csvfile) #Объект писателя с модулем csv, у к
        writer.writerow( (data['Number1'],
                         data['Number2'],
                         data['Number3'],
                         data['Number4'],
                         data['Number5'],
                         data['Numberр6']) )

if __name__ == '__main__':
    parser(get_html(baseurl))

