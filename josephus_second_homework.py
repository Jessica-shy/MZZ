#使用容器作为输入，容器中每个元素都是个对象，对象的属性和方法自定义，
#基础属性包括姓名、学号。输入要包括间隔、起始位置。

class student:

    def __init__(self,name,id):
        self.name = name
        self.id = id

def get_josephus(total_num,step,start_id):
    std_list = []
    num = 0
    while num <= total_num-1:
        std = student(name = chr(65+num), id = num)
        std_list.append(std)
        num += 1

    L = std_list.copy()
    index = 0
    while L:
        if index == start_id:
            break
        temp = L.pop(0) #删除索引为0的元素
        index += 1
        L.append(temp) #将删除的元素依次加在L列表后
        #print(L)

    index = 0
    while L:
        temp = L.pop(0)
        index += 1
        if index == step:
            index = 0
            continue
        L.append(temp)
        #print(L)
        if len(L) == 1:
            print(L[0].name,L[0].id)
            break

if __name__ == '__main__':
    get_josephus(5,2,2)