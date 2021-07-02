#任一个英文的纯文本文件，统计其中的单词出现的个数。

#打开、读取、关闭文件
file = open(r'C:\Users\lenovo\Desktop\0004.txt') 
new_file = file.read()
file.close()
#以空格分隔单词
word_list = new_file.split(' ')

x = input('Please input the word to be queried：')
i = 0
num = 0
for i in range(len(word_list)):
    if word_list[i] == x:
        num += 1
print('The number of times the word appears is %d .' % num)
