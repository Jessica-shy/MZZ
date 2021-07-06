#约瑟夫环问题：已知n个人（以编号1，2，3…n分别表示）围成圈。
#从编号为1的人开始报数，数到k的那个人出圈；他的下一个人又从1开始报数，数到k的那个人又出圈；
#依此规律重复下去，直到圈中只剩最后一个人。

def get_josephus(num,k):
    L = list(range(1,num+1))
    index = 0
    while L:
        temp = L.pop(0) #删除索引为0的元素
        index += 1
        if index == k:
            index = 0
            continue
        L.append(temp) #将剩下的元素依次加在L列表后
        if len(L) == 1:
            print(L)
            break

if __name__ == '__main__':
    josephus(10,6)
