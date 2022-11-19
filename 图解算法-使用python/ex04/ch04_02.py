def showdata (data):
    for i in range(8):
        print("%3d" %data[i],end='')

def select (data):
    for i in range(7):
        smallest=data[i]
        index=i
        for j in range(i+1,8):   # 由i+1开始比较
            if smallest>data[j]: # 找出最小元素
                smallest=data[j]
                index=j
		
        tmp=data[i]
        data[i]=data[index]
        data[index]=tmp
        print("\n第%d次排序结果为：" %(i+1),end='')
        showdata (data)

data=[16,25,39,27,12,8,45,63]
print("原始数据为：", end='')
for i in range(8):
    print("%3d" %data[i],end='')
print("\n-------------------------------------")
select (data)
print("\n-------------------------------------")
print("排序后的数据为：", end='')
for i in range(8):
    print("%3d" %data[i], end='')