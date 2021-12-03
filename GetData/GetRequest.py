import requests
from bs4 import BeautifulSoup
import re


def get_request(page_number):
    divar = requests.get(
        'https://www.truecar.com/used-cars-for-sale/listings/?page={}', page_number)
    soup = BeautifulSoup(divar.text, 'html.parser')

    name = soup.find_all(
        'span', {"class": 'vehicle-header-make-model text-truncate'})
    model = soup.find_all('span', {"class": 'vehicle-card-year font-size-1'})
    karkard = soup.find_all('div', {"data-test": 'vehicleMileage'})
    price = soup.find_all(
        'div', {"class": 'heading-3 margin-y-1 font-weight-bold'})

    list_name = []
    list_price = []
    list_karkard = []
    List_model = []

    for item in name:
        k = item.get_text()
        k = re.split('\s+', k)
        list_name.append(k[0])

    for item in model:
        k = ''.join([n for n in item.get_text() if n.isdigit()])
        List_model.append(k)

    for item in karkard:
        k = ''.join([n for n in item.get_text() if n.isdigit()])
        list_karkard.append(k)

    for item in price:
        k = ''.join([n for n in item.get_text() if n.isdigit()])
        list_price.append(k)

    result = []
    for i in range(20):
        item = [list_name[i], List_model[i], list_karkard[i], list_price[i]]
        result.append(item)

    return result
