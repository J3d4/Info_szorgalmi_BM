import csv
from tqdm import tqdm


class Dict:
    def __init__(self, row, header):
        self.__dict__ = dict(zip(header, row))

class DictReader:
    def read(self, input):
        print('Reading ->')
        data = [Dict(i, input[0]) for i in tqdm(input[1:])]
        return data

class Read:
    def dataFrame(self, file, encoding, delimiter):
        return list(csv.reader(open(file, 'r', encoding = encoding), delimiter = delimiter))

class Write:
    def header(self, data):
        value = list()
        for i in data[1].__dict__:
            value.append(i)
        return value
# basic data frame writer
    def writer(self, file, header, data, encoding, delimiter):
        write = csv.DictWriter(
            open(file, 'w', encoding = encoding), delimiter = delimiter, fieldnames = header)
        write.writeheader()
        for i in tqdm(range(len(data))):
            write.writerow(data[i].__dict__)
# custom data frame writer
    def dataWriter(self, file, header, data, encoding, delimiter):
        write = csv.DictWriter(
            open(file, 'w', encoding = encoding), delimiter = delimiter, fieldnames = header)
        write.writeheader()
        for i in tqdm(data):
            write.writerow(i)
