'''
Created on 16-Jan-2021

@author: VADIRAJ V
'''

def func(no_of_fives,no_of_ones,total_amount):
    five_needed=0;
    one_needed=0;
    flag=0;
    
    if(total_amount<=no_of_fives*5+no_of_ones):
        fives=total_amount//5;
        ones=total_amount%5;
        if(fives<=no_of_fives and ones<=no_of_ones):
            five_needed=fives
            one_needed=ones;
            flag=1;
        elif(fives>no_of_fives):
            five_needed=no_of_fives;
            one_needed=total_amount-(no_of_fives*5)
            flag=1;
    if(flag==1):
        print("no of fives needed", five_needed)
        print("no of ones needed", one_needed)
                
    else:
        print(-1);
        
func(8,5,28)                
              
