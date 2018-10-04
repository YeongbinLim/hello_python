

import os


def parser(a,b):
    f = open('C:\\Users\\YeongBin\\Desktop\\big_data\\%s\\%s.txt'%(b, a), 'r')
    while True:
     line = f.readline()
     if not line: break

     line=line.replace("\t",",")
     f_1 = open('C:\\Users\\YeongBin\\Desktop\\big_data\\%s\\%s_copy.txt'%(b, a), 'a')
     f_1.write(line)

     f_1.close()

    f.close()

b=input()
a=input()

parser(a,b)