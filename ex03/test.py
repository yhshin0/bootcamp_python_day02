from csvreader import CsvReader

if __name__ == '__main__':
    with CsvReader('good.csv') as file:
        data = file.getdata()
        header = file.getheader()
    print(header)
    for elem in data:
        print(elem)
    '''
    with CsvReader('bad.csv') as file:
        data = file.getdata()
        header = file.getheader()
    '''
