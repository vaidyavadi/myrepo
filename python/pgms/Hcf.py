def func(num1,num2):
    if num1<num2:
        smaller=num1;
    else:
        smaller=num2;
    for i in range(1,smaller+1):
        if ((num1%i==0) and (num2%i==0)):
            hcf=i
    return hcf


num1=54
num2=24
print(func(num1,num2))    

fact=1
for i in range(6,0,-1):
    fact*=i
print(fact)

string="nakkan"
rev=(string[::-1])
if (rev==string):
    print("its palindrome");
else:
    print("its not palindrome")    
           
       
