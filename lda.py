import numpy as np
x1=[4,2,2,3,4]
y1=[1,4,3,6,4]

x2=[9,6,9,8,10]
y2=[10,8,5,7,8]

sumx1=0
sumy1=0
sumx2=0
sumy2=0

for i in x1:
    sumx1+=i
for i in y1:
    sumy1+=i
for i in x2:
    sumx2+=i
for i in y2:
    sumy2+=i
    
meanx1=sumx1/len(x1)
meany1=sumy1/len(y1)
meana1=[meanx1,meany1]
meanx2=sumx2/len(x2)
meany2=sumy2/len(y2)
meana2=[meanx2,meany2]
print("meanx1: ",meanx1," meany1: ",meany1)
print("meanx2: ",meanx2," meany2: ",meany2)

a=[]
b=[]
c=[]
d=[]

for i in range(0,len(x1)):
    a.append(x1[i]-meanx1)
    b.append(y1[i]-meany1)

print("S1")
data = np.array([a,b])
data1=np.transpose(data)
res = np.dot(data,data1)/len(x1)
print(res)
print("S2")
for i in range(0,len(x2)):
    c.append(x2[i]-meanx2)
    d.append(y2[i]-meany2)
data2 = np.array([c,d])
data3=np.transpose(data2)
res2 = np.dot(data2,data3)/len(x2)
print(res2)

print("Sw")
res3=np.add(res,res2)
print(res3)

print("Sb")
res5=[]
res4=np.subtract(meana1,meana2)
list1=[res4[0]*res4[0],res4[0]*res4[1]]
list2=[res4[1]*res4[0],res4[1]*res4[1]]
res5.append(list1)
res5.append(list2)
print(res5)


print("Sw-1*Sb")
res6=np.linalg.inv(res3)
res7=np.dot(res6,res5)
print(res7)

w, v = np.linalg.eig(res7)
print("Eigen Values:\n", w)

print("Eigen Vectors:\n",v)
    

