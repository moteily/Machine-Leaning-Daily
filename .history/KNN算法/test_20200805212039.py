import numpy as np
inx = [1,2,3]
a = np.array(inx)   #array函数用于构建各种维度及形态的数组
print(a)
print(np.tile(a,(3,1))) #将array进行复制，三行一列 或
b = np.tile(a,(3,1))
b2 = b**2
print(b2)
print(b2.sum(axis=0)) #axis表示从那个维度求和 axis = 1表示横向求和
