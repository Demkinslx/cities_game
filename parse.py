import json


def parse(self):  # при помощи этой функции мы достаем из ru_cities.json только города
    with open('ru_cities.json') as jsonCities:
        list_cities = []
        data = jsonCities.read()
        str_data = json.loads(data)
        for i in str_data:
            list_cities.append(i['city'])
        a = open('only_cities.json', 'w')
        print(list_cities)
        a.write(str(list_cities))
# сам по себе данный файл исполняет свою задачу только один раз, чтобы достать
# список городов, но я решил оставить и изначальный ru_cities.json, и файл с методом parse где я спарсил названия городов, быть может кому будет полезно посмотреть как я работал с json форматом
