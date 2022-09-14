import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import pandas as pd

HEADERS = {
    'User-Agent': 'TrecoBot/1.0'}
MAIN_URL = 'https://tradingeconomics.com/'


def __format_dataframe(dataframe: pd.DataFrame, fmt: str):
    fmt = fmt.to_lower()

    if fmt == 'json':
        return dataframe.to_json()
    elif fmt == 'csv':
        return dataframe.to_csv()
    elif fmt == 'dict':
        return dataframe.to_dict()
    elif fmt == 'html':
        return dataframe.to_html()
    elif fmt == 'numpy' or 'np':
        return dataframe.to_numpy()
    elif fmt == 'pickle':
        return dataframe.to_pickle()
    elif fmt == 'latex':
        return dataframe.to_latex()
    else:
        return dataframe


def get_data_from_tables(url: str) -> list:
    headers = HEADERS

    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    tables = soup.find_all('table', 'table')

    df_tables_list = []

    for table in tables:
        df_table = pd.read_html(str(table))
        df_tables_list.append(df_table[0])

    return df_tables_list


def scrape_specific_data(server_path, format):
    url = MAIN_URL + server_path
    dataframe_list = get_data_from_tables(url)

    for dataframe in dataframe_list:

    return


def get_data_from_lists(url: str, as_list=False):
    headers = HEADERS
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    lists = soup.find_all('ul', {'class': 'list-unstyled'})

    df_return = {}

    for list_ in lists:

        list_contents = list_.find_all('li')
        df_list_contents = {}
        key = ""

        for list_item in list_contents:
            a = list_item.find('a')
            if a is not None:
                df_list_contents[list_item.text] = a.get('href')
            else:
                key = list_item.text
        if as_list == True:
            df_return.append([key, df_list_contents])
        else:
            df_return[key] = df_list_contents

    return df_return
