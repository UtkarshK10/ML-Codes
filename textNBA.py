R = int(input("Enter the number of rows:\n"))
C = int(input("Enter the number of columns:\n"))
  

matrix = []
print("Enter the entries rowwise:")
'''  
# For user input
for i in range(R):          
    a =[]
    print("Enter",i+1,"row")
    for j in range(C):
         a.append(int(input()))
    matrix.append(a)
'''  
  
for i in range(R):
    a=[]
    print("**************************")
    print("Enter Row Number",i+1)
    input_x=input()
    x_list = input_x.split()
    for i in range(0,len(x_list)):
        a.append(int(x_list[i]))
    matrix.append(a)
    
'''        
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = " ")
    print()
'''    
sum1=0;
sum0=0;    

for i in range(R):
    for j in range(C):
        if(j==C-1):
            if(matrix[i][j]==0):
                sum0=sum0+1
            else:
                sum1=sum1+1

total=sum0+sum1
pyes=sum1/total
pno=sum0/total
print("***********************")
print("P(no)=>",pno);
print("p(yes)=>",pyes);

ptcount=[]
for j in range(C-1):
    count1=0
    for i in range(R):
        if(matrix[i][j]==1):
            count1=count1+1
    ptcount.append(count1)
pt=[]
for j in range(C-1):
    count1=0
    for i in range(R):
        if(matrix[i][j]==1 and matrix[i][C-1]==1):
            count1=count1+1
    pt.append(count1)
pty=[]
ptn=[]
for i in range(0,len(pt)):
    pty.append(float("{:.2f}".format(pt[i]/sum1)))
    
for i in range(0,len(pt)):
    diff=ptcount[i]-pt[i]
    ptn.append(float("{:.2f}".format(diff/sum0)))

print("            [",end="")
for i in range(1,C-1):
    print("T",i,end=" ,")
print("T",C-1,end="")
print("]")    
    
print("P(t|yes)=>",pty)
print("P(t|no)=>",ptn)

print("***********************")

tc=int(input("Enter number of testcases. \n"))

print("***********************")
print()

tcc=1
while(tc>0):
    print("Testcase number:",tcc)
    tc=tc-1
    tcc=tcc+1
    b=[]
    input_y=input("Enter the Combination Space Seperated.\n")
    y_list = input_y.split()
    for i in range(0,len(y_list)):
        b.append(int(y_list[i]))
    print()
    print("Combination=><",b,">")
    
    pyx=[]
    pyn=[]
    
            
    for k in range(0,len(b)):
        if(b[k]==1):
            pyx.append(pty[k])
        else:
            pyx.append(float("{:.2f}".format(1-pty[k])))
        
    for k in range(0,len(b)):
        if(b[k]==1):
            pyn.append(ptn[k])
        else:
            pyn.append(float("{:.2f}".format(1-ptn[k])))
    '''
    print("PYX",pyx)
    print("PYN",pyn)
    '''
    print("P(yes|x)=>",end="")
    
    for k in range(0,len(pyx)):
        print(pyx[k],"*",end="")
        
    print(pyes,"/P(x)=",end="")
    
    pyxx=1
    for k in range(0,len(pyx)):
        pyxx=pyxx*pyx[k]
    
    pyxx=pyxx*pyes    
    print(float("{:.4f}".format(pyxx)),"/P(x)")
    
    print("P(no|x)=>",end="")
    
    for k in range(0,len(pyn)):
        print(pyn[k],"*",end="")
        
    print(pno,"/P(x)=",end="")
    
    pynn=1
    for k in range(0,len(pyn)):
        pynn=pynn*pyn[k]
    
    pynn=pynn*pno    
    print(float("{:.4f}".format(pynn)),"/P(x)")
    
    pxxx=pynn+pyxx
    print("P(yes/x)+P(no/x) must be equal to 1.")
    print(float("{:.4f}".format(pyxx)),"/P(x)+",float("{:.4f}".format(pynn)),"/P(x)=1")
    print("p(x)=>",float("{:.4f}".format(pyxx)),"+",float("{:.4f}".format(pynn)))
    print("p(x)=>",float("{:.4f}".format(pxxx)))
    
    print("P(yes|x)=>",float("{:.4f}".format(pyxx/pxxx)))
    print("P(no|x)=>",float("{:.4f}".format(pynn/pxxx)))
    if(float("{:.4f}".format(pyxx/pxxx))>float("{:.4f}".format(pynn/pxxx))):
        print("P(yes|x)>p(no|x) so it is spam")
    elif(float("{:.4f}".format(pyxx/pxxx))<float("{:.4f}".format(pynn/pxxx))):
        print("P(yes|x)<p(no|x) so it is not a spam")
    else:
        print("P(yes|x)=p(no|x) so it is not properly classified")
    print("*******************************")
    print()
    










            