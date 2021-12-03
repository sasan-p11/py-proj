from GetRequest import get_request


def sum_data():
    full_list_cars = []
    list_test=[]
    for i in range(200):
        item_test = get_request(i)
        full_list_cars=full_list_cars+item_test

    for item in list_test:
        full_list_cars.append(item)

    return full_list_cars