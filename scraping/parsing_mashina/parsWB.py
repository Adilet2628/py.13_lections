from bs4 import BeautifulSoup
import requests
import csv

url = 'https://lalafo.kg/'
def parsing_data():
    response = requests.get(url)
    # print(response.text)
    soup = BeautifulSoup(response.text,'html.parser')
    container = soup.find('div', class_="main-feed__container")
    tovars = container.find_all('article', class_='adTile-wrap')
 
    result = []



    for tovar in tovars:
        price = tovar.find('p', class_='adTile-price').text
        tov = tovar.find('a',class_='adTile-title').text
        img = tovar.find('img')
        if img is not None:
           img = img.get('data-src')

        ava =tovar.find('img', class_= 'userAvatar-photo')
        if ava is not None:
           ava = ava.get('data-src')
        result.append(data)
        print(data)


write_to_csv(result)


def write_to_csv(data: list):
    with open('cars.csv', 'w') as file:
        count = 1
        fieldnames = ['№', 'tov', 'price','img' 'ava']
        writer = csv.DictWriter(file, fieldnames)
       
        for tovar in data:
            writer.writerow({
                '№': count,
                'name': car['tov'],
                'price': car['price'],
                'avatar': car['ava'],
                'image': car['img'],
            })
            count += 1


parsing_data()


















