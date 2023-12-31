# Cреднее  
from bs4 import BeautifulSoup
import requests
import csv

url = 'https://auto312.kg/'

def parsing_data():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    container = soup.find('div', class_='dj-items-rows')
    cars = container.find_all('div', class_='item_row')
    result = []
    for car in cars:
        name = car.find('h3').find('a').text
        img = f'{url}{car.find("img").get("src")}'
      

        price = car.find('div', class_='item_price').text
        desc = car.find('div', class_='item_custom_fields').text
        data = {'title': name, 'desc': desc, 'price': price, 'img': img}
        result.append(data)
        print(data)
        write_to_csv(result)


def write_to_csv(data: list):
    with open('cars.csv', 'w') as file:
        count = 1
        fieldnames = ['№', 'name', 'desc', 'price', 'image']
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow({
            '№': '№',
            'name': 'Name:',
            'desc': 'Description:',
            'price': 'Price:',
            'image': 'Image Url:',
        })
        for car in data:
            writer.writerow({
                '№': count,
                'name': car['title'],
                'desc': car['desc'],
                'price': car['price'],
                'image': car['img'],
            })
            count += 1
parsing_data()
# =============================================================================

# Легкое
# from bs4 import BeautifulSoup
# import requests
# import csv

# url = 'https://www.kivano.kg/mobilnye-telefony'

# def parsing_data():
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text,'html.parser')
#     container = soup.find('div', class_='list-view')
#     mobila = container.find_all('div', class_='item product_listbox oh')
#     result = []
    

#     for mobil in mobila:
#         name = mobil.find('strong').text
#         price = mobil.find('div', class_='listbox_price text-center').find('strong').text
#         img = mobil.find('img').get('src')
        
#         data = {'title': name, 'price': price, 'img': img}
#         result.append(data)
#         print(data)
#         write_to_csv(result)


# def write_to_csv(data: list):
#     with open('cars.csv', 'w') as file:
#         count = 1
#         fieldnames = ['№', 'name', 'price', 'image']
#         writer = csv.DictWriter(file, fieldnames)
#         writer.writerow({
#             '№': '№',
#             'name': 'Name:',
#             'price': 'Price:',
#             'image': 'Image Url:',
#         })
#         for car in data:
#             writer.writerow({
#                 '№': count,
#                 'name': car['title'],
#                 'price': car['price'],
#                 'image': car['img'],
#             })
#             count += 1
# parsing_data()














































