#任一个英文的纯文本文件，统计其中的单词出现的个数。
#处理大文件是很容易想到的就是将大文件分割成若干小文件处理，处理完每个小文件后释放该部分内存。
#或者利用open()自带方法生成迭代对象，一行一行的读取。

import re
def count_the_words(path):
    with open(path) as f: #打开文件记作f(自动关闭)
        text = f.read()
        words_list = re.findall(r"[^a-zA-Z]",text) #利用正则公式(匹配相应的字符串)分割字符串
        count = len(words_list)
    return count

if __name__ == '__main__':
    nums = count_the_words(r'C:\Users\lenovo\Desktop\0004.txt')
    print(nums)
