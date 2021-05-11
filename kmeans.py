import collections  
import numpy as np
r = int(input("Enter number of rows\n"))
a=[]
x=[]
y=[]
for i in range(1,r+1):
    a.append(i)

input_x=input("Enter elements in x in space seperated\n")
input_y=input("Enter elements in y in space seperated\n")

x_list = input_x.split()
y_list = input_y.split()

for i in range(0,len(x_list)):
    x.append(float(x_list[i]))
    
print("x=>",x)
    
for i in range(0,len(y_list)):
    y.append(float(y_list[i]))
    
print("y=>",y)

centres=[]
input_centres=input("Enter centroids in space seperated\n")
centres_list=input_centres.split()

for i in range(0,len(centres_list)):
    centres.append(int(centres_list[i]))
    
print("centres: =>",centres)

iter=1;
new=[]
old=[]

#mean array
c1=[x[centres[0]-1],y[centres[0]-1]]
c2=[x[centres[1]-1],y[centres[1]-1]]


print("c1=>",c1)
print("c2=>",c2)
print("\n\n")
#centroid table
centroid1=[]
centroid2=[]
iter=1
print("iteration",iter)

for i in range (0,len(a)): 
    point=np.array([x[i],y[i]])
    centroid1.append("{:.2f}".format(np.linalg.norm(point - c1)))
    centroid2.append("{:.2f}".format(np.linalg.norm(point - c2)))
    
for i in range(0,len(centroid1)):
    centroid1[i]=float(centroid1[i])
    centroid2[i]=float(centroid2[i])
    
    
    
clas=[]
count1=0
count2=0
for i in range(0,len(centroid1)):
    if(centroid1[i]<=centroid2[i]):
        count1=count1+1
        clas.append(1)
    else:
        count2=count2+1
        clas.append(2)
        
print("a=>",a)    
print("centroid1=>",centroid1)
print("centroid2=>",centroid2)
print("class=>",clas)

temp=[]
for i in range(0,len(a)):
    temp.append(i)
    
nmean1=[]
nmean2=[]
sumx1=0
sumy1=0
sumx2=0
sumy2=0
for i in range (0,len(clas)):
    if(clas[i]==1):
        sumx1=sumx1+x[i]
        sumy1=sumy1+y[i]
    else:
        sumx2=sumx2+x[i]
        sumy2=sumy2+y[i]
nmean1=[float("{:.2f}".format(sumx1/count1)),float("{:.2f}".format(sumy1/count1))]
nmean2=[float("{:.2f}".format(sumx2/count2)),float("{:.2f}".format(sumy2/count2))]



print("new mean 1 =>",nmean1)
print("new mean 2 =>",nmean2)

ntemp=[]        
iter=2
print("\n\n")
while collections.Counter(temp) != collections.Counter(ntemp):
    print("iteration",iter)
    print("a=>",a)
    ntemp.clear()
    for i in range(0,len(clas)):
        ntemp.append(clas[i])
    centroid1.clear()
    centroid2.clear()
    clas.clear()
    count1=0
    count2=0
    sumx1=0
    sumy1=0
    sumx2=0
    sumy2=0
    for i in range (0,len(a)): 
        point=np.array([x[i],y[i]])
        centroid1.append(float("{:.2f}".format(np.linalg.norm(point - nmean1))))
        centroid2.append(float("{:.2f}".format(np.linalg.norm(point - nmean2))))    
    print("centroid1=>",centroid1)
    print("centroid2=>",centroid2)
    for i in range(0,len(centroid1)):
        if(centroid1[i]<=centroid2[i]):
            count1=count1+1
            clas.append(1)
        else:
            count2=count2+1
            clas.append(2)
    print("class=>",clas)
    for i in range (0,len(clas)):
        if(clas[i]==1):
            sumx1=sumx1+x[i]
            sumy1=sumy1+y[i]
        else:
            sumx2=sumx2+x[i]
            sumy2=sumy2+y[i]
    nmean1=[float("{:.2f}".format(sumx1/count1)),float("{:.2f}".format(sumy1/count1))]
    nmean2=[float("{:.2f}".format(sumx2/count2)),float("{:.2f}".format(sumy2/count2))]
    print("new mean 1 =>",nmean1)
    print("new mean 2 =>",nmean2)
    temp=clas 
    print("\n\n")
    iter=iter+1

print("\n\n")    
print("Iteration Ended In ",iter-1,"iteration.")
cluster1=[]
cluster2=[]

for i in range(0,len(clas)):
    if(clas[i]==1):
        cluster1.append(a[i])
    else:
        cluster2.append(a[i])

print("Cluster1 consists of ",cluster1)
print("Cluster2 consists of ",cluster2)


    
    

