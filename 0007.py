# 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

import os

def get_all_file(path):
    file_list = []
    files = os.listdir(path)#遍历目录中的所有文件

    for file in files:
            if os.path.splitext(file)[1] == '.py':#判断是否为python文件
                file_list.append(path + '\\' + file)
                print('+' + file)
    return file_list

def get_rows(file):
    with open(file, encoding='utf8') as f:#打开文件（自动关闭），编码格式为UTF-8
        lines = f.readlines()#读取全部组成列表，每行内容为一个元素
        rows = len(lines)#代码总行数
        vuui = 0#注释行数
        space = 0#空行数

        for line in lines:
            if line == '\n':
                space += 1
            if line[0] == '#':
                vuui += 1

        data = {
            'rows': rows,
            'vuui': vuui,
            'space': space
        }
    return data

def run(path):
    file_list = get_all_file(path)
    all_rows = 0     
    all_vuui = 0     
    all_space = 0 

    for file in file_list:
        data = get_rows(file)
        print('count' + file)
        rows = data.get('rows')
        vuui = data.get('vuui')
        space = data.get('space')
        all_rows += rows
        all_vuui += vuui
        all_space += space
    print('代码行数：{%d}\n注释行数：{%d}\n空行数：{%d}' % (all_rows, all_vuui, all_space))

if __name__ == '__main__': 
    path = r'C:\\Users\\lenovo\\Desktop\\0007'
    run(path=path)
