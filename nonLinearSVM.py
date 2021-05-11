import numpy as np
import matplotlib.pyplot as plt
import math

lin=int(input("Enter 1 for Liner & 0 for Non Linear\n"))
if(lin==0):
    print("NonLinear SVM.")
    n = int(input("Enter number of coordinates in x1\n"))
    matrix1=[]
    count=1
    while(n>0):
        n=n-1
        print("Enter",count,"coordinate space seperated")
        count=count+1
        x=[]
        input_x=input()
        x_list = input_x.split()
        for i in range(0,len(x_list)):
            x.append(float(x_list[i]))
        matrix1.append(x)
        
    num = int(input("Enter number of coordinates in x2\n"))
    matrix2=[]
    count2=1
    while(num>0):
        num=num-1
        print("Enter",count2,"coordinate space seperated")
        count2=count2+1
        x=[]
        input_x=input()
        x_list = input_x.split()
        for i in range(0,len(x_list)):
            x.append(float(x_list[i]))
        matrix2.append(x)    
    print("Initial Matrix\n")    
    print("Matrix1=>",matrix1)
    print("Matrix2=>",matrix2)
    print("***************************\n")
        
    matrix3=[]
    matrix4=[]
    for i in range(len(matrix1)):
        a=[]
        sum=0
        for j in range(len(matrix1[i])):
            a.append(matrix1[i][j])
        for i in range(len(a)):
            sum=sum+a[i]**2
        if(math.sqrt(sum)>=2):
            temp1=a[0]
            temp2=a[1]
            a[0]=6-temp1+((temp1-temp2)**2)
            a[1]=6-temp2+((temp1-temp2)**2)
        matrix3.append(a)
        
    for i in range(len(matrix2)):
        a=[]
        sum=0
        for j in range(len(matrix2[i])):
            a.append(matrix2[i][j])
        for i in range(len(a)):
            sum=sum+a[i]**2
        if(math.sqrt(sum)>=2):
            temp1=a[0]
            temp2=a[1]
            a[0]=6-temp1+((temp1-temp2)**2)
            a[1]=6-temp2+((temp1-temp2)**2)
        matrix4.append(a)
        
    
    
    print("New Matrix1=>",matrix3)
    print("New Matrix2=>",matrix4)   
    
    print("***************") 
    
    Xmatrix=[]
    Ymatrix=[]
    
    for i in range(len(matrix3)):
        Xmatrix.append(matrix3[i][0])
    for i in range(len(matrix4)):
        Xmatrix.append(matrix4[i][0])
    
    
    for i in range(len(matrix3)):
        Ymatrix.append(matrix3[i][1])
    for i in range(len(matrix4)):
        Ymatrix.append(matrix4[i][1])
        
        
    '''    
    print("XMatrix=>",Xmatrix)
    print("YMatrix=>",Ymatrix)
    '''
    print("Look at the graph to find S1,S2,S3\n")
    print("***************") 
    plt.scatter(Xmatrix,Ymatrix)
    plt.axvline(0, c='black', ls='--')
    plt.axhline(0, c='black', ls='--')
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.title("Scatter Plot with both negative and positive axes")
    plt.colorbar()
    plt.show()    


s1=[]
s2=[]
s3=[]
input_s1=input("Enter S1 Coordinates\n")
s1_list = input_s1.split()
for i in range(0,len(s1_list)):
    s1.append(float(s1_list[i]))

input_s2=input("Enter S2 Coordinates\n")
s2_list = input_s2.split()
for i in range(0,len(s2_list)):
    s2.append(float(s2_list[i]))
    
input_s3=input("Enter S3 Coordinates\n")
s3_list = input_s3.split()
for i in range(0,len(s3_list)):
    s3.append(float(s3_list[i]))

print("S1=>",s1)
print("S2=>",s2)
print("S3=>",s3)

s1.append(1.0)
s2.append(1.0)
s3.append(1.0)

print("~S1=>",s1)
print("~S2=>",s2)
print("~S3=>",s3)

temp1=int(input("Enter value for S1 (1/-1)\n"))
temp2=int(input("Enter value for S2 (1/-1)\n"))
temp3=int(input("Enter value for S3 (1/-1)\n"))

s1s1=np.dot(s1,s1)
s1s2=np.dot(s1,s2)
s1s3=np.dot(s1,s3)
s2s2=np.dot(s2,s2)
s2s3=np.dot(s2,s3)
s3s3=np.dot(s3,s3)
print()
print("***************Equations*****************")
print("a1",s1s1,"+ a2",s1s2,"+ a3",s1s3,"=",temp1)
print("a1",s1s2,"+ a2",s2s2,"+ a3",s2s3,"=",temp2)
print("a1",s1s3,"+ a2",s2s3,"+ a3",s3s3,"=",temp3)



a = np.array([[s1s1,s1s2,s1s3],[s1s2,s2s2,s2s3],[s1s3,s2s3,s3s3]])
b = np.array([temp1,temp2,temp3])
y = np.linalg.solve(a, b)
x=[]

for i in range(len(y)):
    x.append(float("{:.4f}".format(y[i])))
    
print()
print("a1=>",x[0])
print("a2=>",x[1])
print("a3=>",x[2])

s4=[]
ss1=[]
ss2=[]
ss3=[]
for i in range(len(s1)):
    ss1.append(float("{:.4f}".format(x[0]*s1[i])))
        
for i in range(len(s2)):
    ss2.append(float("{:.4f}".format(x[1]*s2[i])))
    
for i in range(len(s3)):
    ss3.append(float("{:.4f}".format(x[2]*s3[i])))

arr=np.add(ss1,ss2)
s4=np.add(arr,ss3)

print()
print("~w=",x[0],"*",s1,"+",x[1],"*",s2,"+",x[2],"*",s3,"=",s4)
print("***********************")
max=0
for i in range(len(s4)):
    if(s4[i]>max):
        max=s4[i]

s5=[]
for i in range(len(s4)):
    s5.append(float("{:.4f}".format(s4[i]/max)))
    
w=[s5[0],s5[1]]
const=s5[2]

print("W=>",w)
print("b=>",const)




        