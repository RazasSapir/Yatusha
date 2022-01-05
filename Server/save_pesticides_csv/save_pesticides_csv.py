import requests as r
import csv
import json
import os

PATH = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'pesticides.csv'))


def save_csv() -> None:
    url = 'https://data.gov.il/api/3/action/datastore_search?resource_id=2d741cd4-9c54-492c-8607-933deddb3094'
    res = json.loads(r.get(url).content.decode())['result']['records']
    keys = res[0].keys()
    with open(PATH, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(res)

"""
 for later (check if the file is updated)
 with open('pesticides.csv', 'r', newline='') as read_file:
    dict_reader = csv.DictReader(read_file)
    # get a list of dictionaries from dct_reader
    a = list(dict_reader)
    # print list of dict i.e. rows"""
