'''
想要使用csv文件，首先得要导入csv代码库，python3中自带了所以不用导入
但是使用excel文件需要导入，导入办法：
1、pip命令安装：
2、下载安装：
'''
import csv

path = 'C:/Users/51Testing/PycharmProjects/selenium7th/data/data.csv'
file = open(path, 'r')
data_table = csv.reader(file)
#打印dable的数据
for item in data_table:
    print(item)