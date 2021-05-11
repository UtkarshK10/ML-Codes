import numpy as np

x = [3,4,6]
y = [2,2,1]


A=[]
B=[]
AB=[]
A2=[]
B2=[]

sumx=0;
sumy=0;
for i in x:
    sumx+=i;
for i in y:
    sumy+=i;

meanx=sumx/len(x);
meany=sumy/len(y);

print("meanx: ",meanx);
print("meany: ",meany);


for i in range(0, len(x)):
    A.append(x[i]-meanx)
    B.append(y[i]-meany)
    AB.append(A[i]*B[i])
    A2.append(A[i]*A[i])
    B2.append(B[i]*B[i])
print("x      y       A        B          AB           A2            B2")
for i in range(0, len(x)):
    print(x[i],"    ",y[i],"    ",A[i],"    ",B[i],"    ",AB[i],"   ",A2[i],"   ",B2[i])    

data = np.array([x,y])
covMatrix = np.cov(data,bias=False)
print("Covariance Matrix")
print (covMatrix)
w, v = np.linalg.eig(covMatrix)

print("Eigen Values:\n", w)

print("Eigen Vectors:\n",v)