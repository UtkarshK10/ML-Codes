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


#mean array
c1=[x[centres[0]-1],y[centres[0]-1]]
c2=[x[centres[1]-1],y[centres[1]-1]]
c3=[x[centres[2]-1],y[centres[2]-1]]
c4=[x[centres[3]-1],y[centres[3]-1]]

print("c1=>",c1)
print("c2=>",c2)
print("c3=>",c3)
print("c4=>",c4)

print("\n")
#centroid table
centroid1=[]
centroid2=[]
centroid3=[]
centroid4=[]
iter=1
print("iteration",iter)

for i in range (0,len(a)): 
    point=np.array([x[i],y[i]])
    centroid1.append("{:.2f}".format(np.linalg.norm(point - c1)))
    centroid2.append("{:.2f}".format(np.linalg.norm(point - c2)))
    centroid3.append("{:.2f}".format(np.linalg.norm(point - c3)))
    centroid4.append("{:.2f}".format(np.linalg.norm(point - c4)))
    
for i in range(0,len(centroid1)):
    centroid1[i]=float(centroid1[i])
    centroid2[i]=float(centroid2[i])
    centroid3[i]=float(centroid3[i])
    centroid4[i]=float(centroid4[i])
    
    
clas=[]
count1=0
count2=0
count3=0
count4=0
for i in range(0,len(centroid1)):
    if(centroid1[i]<=centroid2[i] and centroid1[i]<=centroid3[i] and centroid1[i]<=centroid4[i]):
        count1=count1+1
        clas.append(1)
    elif(centroid2[i]<=centroid1[i] and centroid2[i]<=centroid3[i] and centroid2[i]<=centroid4[i]):
        count2=count2+1
        clas.append(2)
    elif(centroid3[i]<=centroid1[i] and centroid3[i]<=centroid2[i] and centroid3[i]<=centroid4[i]):
        count3=count3+1
        clas.append(3) 
    elif(centroid4[i]<=centroid1[i] and centroid4[i]<=centroid2[i] and centroid4[i]<=centroid1[i]):
        count4=count4+1
        clas.append(4)
print("a=>",a)    
print("centroid1=>",centroid1)
print("centroid2=>",centroid2)
print("centroid3=>",centroid3)
print("centroid4=>",centroid4)
print("class=>",clas)

cluster1=[]
cluster2=[]
cluster3=[]
cluster4=[]

for i in range(0,len(clas)):
    if(clas[i]==1):
        cluster1.append(a[i])
    elif(clas[i]==2):
        cluster2.append(a[i])
    elif(clas[i]==3):
        cluster3.append(a[i])
    else:
        cluster4.append(a[i])
print("Cluster1 consists of ",cluster1)
print("Cluster2 consists of ",cluster2)
print("Cluster3 consists of ",cluster3)
print("Cluster4 consists of ",cluster4)


temp=[]
for i in range(0,len(a)):
    temp.append(i)
    
nmean1=[]
nmean2=[]
nmean3=[]
nmean4=[]
sumx1=0
sumy1=0
sumx2=0
sumy2=0
sumx3=0
sumy3=0
sumx4=0
sumy4=0
for i in range (0,len(clas)):
    if(clas[i]==1):
        sumx1=sumx1+x[i]
        sumy1=sumy1+y[i]
    elif(clas[i]==2):
        sumx2=sumx2+x[i]
        sumy2=sumy2+y[i]
    elif(clas[i]==3):
        sumx3=sumx3+x[i]
        sumy3=sumy3+y[i]
    else:
        sumx4=sumx4+x[i]
        sumy4=sumy4+y[i]
nmean1=[float("{:.2f}".format(sumx1/count1)),float("{:.2f}".format(sumy1/count1))]
nmean2=[float("{:.2f}".format(sumx2/count2)),float("{:.2f}".format(sumy2/count2))]
nmean3=[float("{:.2f}".format(sumx3/count3)),float("{:.2f}".format(sumy3/count3))]
nmean4=[float("{:.2f}".format(sumx4/count4)),float("{:.2f}".format(sumy4/count4))]


print("new mean 1 =>",nmean1)
print("new mean 2 =>",nmean2)
print("new mean 3 =>",nmean3)
print("new mean 4 =>",nmean4)

ntemp=[]        
iter=2
print("\n")
while collections.Counter(temp) != collections.Counter(ntemp):
    print("iteration",iter)
    print("a=>",a)
    ntemp.clear()
    for i in range(0,len(clas)):
        ntemp.append(clas[i])
    centroid1.clear()
    centroid2.clear()
    centroid3.clear()
    centroid4.clear()
    cluster1.clear()
    cluster2.clear()
    cluster3.clear()
    cluster4.clear()
    clas.clear()
    count1=0
    count2=0
    count3=0
    sumx1=0
    sumy1=0
    sumx2=0
    sumy2=0
    sumx3=0
    sumy3=0
    sumx4=0
    sumy4=0
    for i in range (0,len(a)): 
        point=np.array([x[i],y[i]])
        centroid1.append(float("{:.2f}".format(np.linalg.norm(point - nmean1))))
        centroid2.append(float("{:.2f}".format(np.linalg.norm(point - nmean2))))
        centroid3.append(float("{:.2f}".format(np.linalg.norm(point - nmean3))))
        centroid4.append(float("{:.2f}".format(np.linalg.norm(point - nmean4))))
    print("centroid1=>",centroid1)
    print("centroid2=>",centroid2)
    print("centroid3=>",centroid3)
    print("centroid4=>",centroid4)
    for i in range(0,len(centroid1)):
        if(centroid1[i]<=centroid2[i] and centroid1[i]<=centroid3[i] and centroid1[i]<=centroid4[i]):
            count1=count1+1
            clas.append(1)
        elif(centroid2[i]<=centroid1[i] and centroid2[i]<=centroid3[i] and centroid2[i]<=centroid4[i]):
            count2=count2+1
            clas.append(2)
        elif(centroid3[i]<=centroid1[i] and centroid3[i]<=centroid2[i] and centroid3[i]<=centroid4[i]):
            count3=count3+1
            clas.append(3) 
        elif(centroid4[i]<=centroid1[i] and centroid4[i]<=centroid2[i] and centroid4[i]<=centroid1[i]):
            count4=count4+1
            clas.append(4) 
    print("class=>",clas)
    for i in range(0,len(clas)):
        if(clas[i]==1):
            cluster1.append(a[i])
        elif(clas[i]==2):
            cluster2.append(a[i])
        elif(clas[i]==3):
            cluster3.append(a[i])
        else:
            cluster4.append(a[i])
    for i in range (0,len(clas)):
        if(clas[i]==1):
            sumx1=sumx1+x[i]
            sumy1=sumy1+y[i]
        elif(clas[i]==2):
            sumx2=sumx2+x[i]
            sumy2=sumy2+y[i]
        elif(clas[i]==3):
            sumx3=sumx3+x[i]
            sumy3=sumy3+y[i]
        else:
            sumx4=sumx4+x[i]
            sumy4=sumy4+y[i]
    nmean1=[float("{:.2f}".format(sumx1/count1)),float("{:.2f}".format(sumy1/count1))]
    nmean2=[float("{:.2f}".format(sumx2/count2)),float("{:.2f}".format(sumy2/count2))]
    nmean3=[float("{:.2f}".format(sumx3/count3)),float("{:.2f}".format(sumy3/count3))]
    nmean4=[float("{:.2f}".format(sumx4/count4)),float("{:.2f}".format(sumy4/count4))]
    print("Cluster1 consists of ",cluster1)
    print("Cluster2 consists of ",cluster2)
    print("Cluster3 consists of ",cluster3)
    print("Cluster4 consists of ",cluster4)
    print("new mean 1 =>",nmean1)
    print("new mean 2 =>",nmean2)
    print("new mean 3 =>",nmean3)
    print("new mean 4 =>",nmean4)
    
    temp=clas 
    print("\n")
    iter=iter+1

print("\n")    
print("Iteration Ended In ",iter-1,"iteration.")

cluster1.clear()
cluster2.clear()
cluster3.clear()
cluster4.clear()


for i in range(0,len(clas)):
    if(clas[i]==1):
        cluster1.append(a[i])
    elif(clas[i]==2):
        cluster2.append(a[i])
    elif(clas[i]==3):
        cluster3.append(a[i])
    else:
        cluster4.append(a[i])

print("Final Cluster1 consists of ",cluster1)
print("Final Cluster2 consists of ",cluster2)
print("Final Cluster3 consists of ",cluster3)
print("Final Cluster4 consists of ",cluster4)


    
    




