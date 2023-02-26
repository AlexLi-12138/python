import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
import openpyxl
import xlwt  
import pandas as pd

def readcertainline(path, count):
    with open(path, 'r') as f:
        for num, line in enumerate(f):
            if num == count:
                print(line)
                break
    return line


path = 'F:/test/test.out'

a0 = readcertainline(path, 401)
a1 = readcertainline(path, 411)
a2 = readcertainline(path, 412)
a3 = readcertainline(path, 413)

b0 = readcertainline(path, 1384)
b1 = readcertainline(path, 1394)
b2 = readcertainline(path, 1395)
b3 = readcertainline(path, 1396)

data1 = [a0, b0]
with open('time.txt', 'a+', encoding='utf-8') as f:
    for data0 in data1:
        # 添加‘\n’用于换行
        f.write(data0)
    f.close()

data2 = [a1, b1]
with open('Gas Phase.txt', 'a+', encoding='utf-8') as f:
    for data0 in data2:
        # 添加‘\n’用于换行
        f.write(data0)
    f.close()

data3 = [a2, b2]
with open('Aqueous.txt', 'a+', encoding='utf-8') as f:
    for data0 in data3:
        # 添加‘\n’用于换行
        f.write(data0)
    f.close()

data4 = [a3, b3]
with open('Solid salt.txt', 'a+', encoding='utf-8') as f:
    for data0 in data4:
        # 添加‘\n’用于换行
        f.write(data0)
    f.close()



def rline(path, num1, num2):
    f = open(path)
    line = f.readline()
    list1 = []
    while line:
        a = line.split()
        b = a[num1:num2]
        list1.append(b)
        line = f.readline()
    f.close()
    return list1


time = rline('time.txt', 10, 11)
Gas_Phase = rline('Gas Phase.txt', 9, 12)
Aqueous = rline('Aqueous.txt', 8, 11)
Solid_salt = rline('Solid salt.txt', 4, 7)


def tonum(list, num):
    A0 = []
    for i in range(len(list[num])):
        a = list[num]
        b = float(a[i])
        A0.append(b)
        i = i + 1
    return A0


time = [tonum(time, 0), tonum(time, 1)]
Gas_Phase = [tonum(Gas_Phase, 0), tonum(Gas_Phase, 1)]
Aqueous = [tonum(Aqueous, 0), tonum(Aqueous, 1)]
Solid_salt = [tonum(Solid_salt, 0), tonum(Solid_salt, 1)]

biaoti = ['time', 'water', 'salt', 'CO2', 'water', 'salt', 'CO2', 'water', 'salt', 'CO2']

list0 = time[0] + Gas_Phase[0] + Aqueous[0] + Solid_salt[0]
list1 = time[1] + Gas_Phase[1] + Aqueous[1] + Solid_salt[1]
listall = [biaoti, list0, list1]


def deal(list, path):
    df = pd.DataFrame(list, columns=['', '', 'Gas_Phase', '',  '', 'Aqueous', '', '', 'Solid_salt', ''])
    df.to_excel(path, index=False)

deal(listall, 'F:/test/res.xlsx')








