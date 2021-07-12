#使用容器作为输入，容器中每个元素都是个对象，对象的属性和方法自定义，
#基础属性包括姓名、学号。输入要包括间隔、起始位置。

class student:

    def __init__(self,name,id):
        self.name = name
        self.id = id

def get_josephus(total_num,step,start_id):
    assert total_num > 0
    assert step > 0
    assert 0 < start_id <= total_num
    std_list = []
    for i in range(total_num):
        std = student(id = i+1,name = chr(65+i))
        std_list.append(std)

    L = std_list.copy()
    if total_num == 1:
        return
    else:
        for i in range(len(std_list)):
            if(start_id == std_list[i].id):
                index = i
                break
        for i in range(total_num-1):
            index = (index + step) % len(L) - 1 #L[(上一次出局者的索引+k) % 上一次出局后的剩余人数 - 1]
            print(L[index].name,L[index].id)
            del L[index] #删除列表L中索引值为index的元素
            if index == -1: #只剩一个人(index < 0)
                index = 0
        print(L[0].name,L[0].id)

if __name__ == '__main__':      
    get_josephus(5,2,3)