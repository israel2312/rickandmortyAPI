import requests
from pprint import pprint
import pandas as pd


baseUrl = 'https://rickandmortyapi.com/api/'
endpoint = 'character'


## In this fucntion we made the request

def main_request(baseUrl, endpoint,x):
    r = requests.get(baseUrl + endpoint + f'?page={x}')
    data = r.json()
    return data


def get_pages(response):
     return response['info']['pages']


def parse_json(response):
    data = []
    for item in response['results']:
        char = {
            'id' : item['id'],
            'name': item['name'],
            'gender' : item['gender'],
            'species': item['species'],
            'origin' : item['origin']['name'],
            'episodes': len(item['episode'])
        }

        data.append(char)
    return data


mainList = []

data = main_request(baseUrl, endpoint,1)

for i in range (1,get_pages(data)+1):
    print(i)
    mainList.extend(parse_json(main_request(baseUrl, endpoint,i)))


df = pd.DataFrame(mainList)
df.to_csv('data.csv' , index = False)


