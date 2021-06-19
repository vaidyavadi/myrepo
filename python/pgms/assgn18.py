'''
Created on 19-Jan-2021

@author: VADIRAJ V
'''

#PF-Assgn-23
def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    for item in reqd_gems:
        if item in gems_list:
            index1=gems_list.index(item)
            index2=reqd_gems.index(item)
            bill_amount=bill_amount+(price_list[index1]*reqd_quantity[index2])
    #Write your logic here
    return bill_amount

#List of gems available in the store
gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[1760,2119,1599,3920,3999]

#List of gems required by the customer
reqd_gems=["Ivory","Emerald","Garnet"]

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[3,10,12]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)

list1=[2,3,4,5,6]
list2=[6,7,8,9,3]
list=[]
for i in list1:
    index=list1.index(i)
    list.append(list1[index]*list2[index])
print(list)  

num=0;
for i in range(6,0,-1):
    for y in range(1,i+1):
        num=num+1;
        print(num,end=" ")
        
    print() 
    
for row in range(7):
    for col in range(5):
        if (col==0) or (col==4 and (row!=0 and row!=3 and row!=6)) or ((row==0 or row==3 or row==6) and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")    
    print()
    
for i in range(6):
    for y in range(6):
        print("*",end="")
    print()
def func(num1,num2):
    if num1>num2:
        smaller=num2            
    else:
        smaller=num1
        for i in range(1,smaller+1):
            if((num1%i==0) and (num2%i==0)):
                hcf=i
    return hcf                    
print(func(2,4))

def factorial(num):
    fact=1
    for i in range(num,1,-1):
        fact*=i
    return fact
print(factorial(6))  


def palin(word):
    rev=''.join(reversed(word))
    if rev==word:
        print("palindrome")
    else:
        print("not a plaindrome")
palin('malayalama') 

def fib(num):
    a=0;
    b=1;
    if num==1:
        print(a)
    else:
        print(a)
        print(b)
        
        
        for i in range(2,num):
            c=a+b;
            a=b;
            b=c;
            print(c)
fib(9)  


def leap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print("its a leap year")
            else:
                print("not a leap year")
        else:
            print("its a leap year")
    else:
        print("its not a leap year") 
leap(2008)                                                      


        
 
        

        
