import csv
import glob
import os
import re
from elasticsearch import Elasticsearch

current_path = os.getcwd()
file_path_list = glob.glob(current_path+'/data/*')
es = Elasticsearch()
regexp = re.compile('([^/]*).csv$')

for file_path in file_path_list:
    with open(file_path, 'r') as csvFile:
        print(file_path)
        csvDict = csv.DictReader(csvFile, restkey=None, restval=None)
        json = [obj for obj in csvDict]
        for i, row in enumerate(json):
            es.index(
                    index = "ldgourmet",
                    doc_type = regexp.search(file_path).group(1),
                    id = i if row.get('id') == None else row.pop('id'),
                    body = row
                    )
