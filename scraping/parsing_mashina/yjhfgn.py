from bs4 import BeautifulSoup
import requests
import csv

url = 'https://kolesa.kz/cars/'

def parsing_data():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    container = soup.find('div', class_='a-list')
    cars = container.find_all('div', class_='a-list__item')
    result = []

    for car in cars:
        img = car.find('div',class_='thumb-gallery')
        print(img)
parsing_data()