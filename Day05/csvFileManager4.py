# encoding=utf-8
import csv
import os


class CsvFileManager4:
    #def read(self):
    def read(self, filename):
        list = []

#       path = r"C:/Users/51Testing/PycharmProjects/selenium7th/data/data.csv"
#       os.path.dirname(__file__)  获取当前文件的目录

        basepath = os.path.dirname(__file__)
#        path = basepath.replace('Day05', 'data/data.csv')
        path = basepath.replace('Day05', filename)

        with open(path, 'r') as file:
            data_table = csv.reader(file)
            for item in data_table:
                print(item)
#       生命一个二维列表，保存data_table中的所有数据
                list.append(item)
#       我们不可能为每一个测试用例单独写类似的方法读取csv文件，就需要设计一个类，将csv文件名作为参数
#         办法是在read()参数列表中加参数 filename  def  read(self, filename)
        return list


if __name__ == '__main__':
    list = CsvFileManager4().read('data/data.csv')