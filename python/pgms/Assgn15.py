'''
Created on 16-Jan-2021

@author: VADIRAJ V
'''
def func(num1,num2,num3):
    product=0;
    if num1==7:
        product=num2*num3;
    elif num2==7:
        product=num3
    else:
        product=-1;
    return product
print(func(1,2,3))             
        
