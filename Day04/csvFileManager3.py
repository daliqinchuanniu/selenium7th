"""
如果每个测试用例对应不同的csv文件，那每条测试用例都会打开一个csv文件，所以每次也应该关闭该文件
"""
import csv

class CsvFile:
    @classmethod
    def read(cls):
        path = 'C:/Users/51Testing/PycharmProjects/selenium7th/data/data.csv'
        file = open(path, 'r')
        """
        try:  语句1...语句n                finally:语句1，语句n
        尝试进行操作，不论try语句不论执行是否出错，那么也得要执行finally后边的语句
        """
        try:
            data_table = csv.reader(file)
            for item in data_table:
                print(item)

        finally:
            print("file.close() method is executed")
            file.close()


if __name__ == '__main__':
    # 如果是@classmethod方法，就类似于java的static方法，直接可以用类调用，不需要对象
    CsvFile.read()
