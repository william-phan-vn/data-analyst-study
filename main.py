import pandas as pd
import requests


dataset_url = 'https://github.com/fivethirtyeight/data/blob/master/nba-elo/nbaallelo.csv'
file_name = 'nba_all_elo.csv'


def save_data(data):
    with open(file_name, 'wb') as f:
        f.write(data)

if __name__ == '__main__':
    data_response = requests.get(dataset_url)
    if data_response.status_code == 200:
        save_data(data_response.content)
