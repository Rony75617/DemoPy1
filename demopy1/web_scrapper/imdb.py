import pandas as pd
import requests
from bs4 import BeautifulSoup
from typing import List
from pandas import DataFrame


def cast_scrap(_url: str) -> List:
    """Create a list of list containing actor name and its corresponding character """
    cast = []
    page = requests.get(_url)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, features='html.parser')
        table = soup.find('table', class_ = 'cast_list')
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            rel_td = cols[1:]
            if rel_td:
                cast_list = []
                actor_td = rel_td[0]
                charc = rel_td[2]
                actor = actor_td.find('a').text
                cast_list.append(actor.strip())
                if charc.has_attr('a'):
                    character = charc.find('a').text
                else:
                    character = charc.text
                cast_list.append(character.strip())          
                cast.append(cast_list)
    return cast

def create_cast_dataframe(data: List[List[str]]) -> DataFrame:
    """Create a dataframe"""
    col_nms = ['Actor', 'Character']
    df = pd.DataFrame(data, columns=col_nms)
    return df


def main():
    joker_imdb_url = 'https://www.imdb.com/title/tt7286456/'
    joker_characters = cast_scrap(joker_imdb_url)
    df = create_cast_dataframe(joker_characters)
    print(df)

if __name__ == '__main__':
    main()
