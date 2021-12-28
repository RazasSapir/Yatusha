import requests as r
import csv
import json
import pandas as pd

def save_csv():
    url = 'https://data.gov.il/api/3/action/datastore_search?resource_id=2d741cd4-9c54-492c-8607-933deddb3094'
    fileobj = r.get(url).content.decode()
    res = json.loads(fileobj)['result']['records']
    keys = res[0].keys()
    with open('pesticides.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(res)

#for later (check if the file if updated)
'''with open('pesticides.csv', 'r', newline='') as read_file:
    dict_reader = csv.DictReader(read_file)
    # get a list of dictionaries from dct_reader
    a = list(dict_reader)
    # print list of dict i.e. rows'''

def main():
    save_csv()


if __name__ == '__main__':
    main()