'''
把读取文件的方法封装起来，这个思想很重要
'''

import csv

class CsvFile:
    @classmethod
    def read(self):
        path = 'C:/Users/51Testing/PycharmProjects/selenium7th/data/data.csv'
        file = open(path, 'r')
        data_table = csv.reader(file)

        for item in data_table:
            print(item)

if __name__ == '__main__':
    # mycsv = CsvFile()
    # mycsv.read()
    #如果是@classmethod方法，就类似于java的static方法，直接可以用类调用，不需要对象
    CsvFile.read()