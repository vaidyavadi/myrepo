'''
Created on 16-Jan-2021

@author: VADIRAJ V
'''
def func(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    if food_type=="Veg":
        if quantity_ordered>0:
            if distance_in_kms>6:
                bill_amount=quantity_ordered*120+((distance_in_kms-6)*6)+9
            elif distance_in_kms>3:
                bill_amount=quantity_ordered*120+((distance_in_kms-3)*3)
            elif distance_in_kms>0:
                bill_amount=quantity_ordered*120
            else:
                bill_amount=-1
        else:
            bill_amount=-1
    elif food_type=="Non-Veg":
        if quantity_ordered>0:
            if distance_in_kms>6:
                bill_amount=quantity_ordered*150+((distance_in_kms-6)*6)+9
            elif distance_in_kms>3:
                bill_amount=quantity_ordered*150+((distance_in_kms-3)*3)
            elif distance_in_kms>0:
                bill_amount=quantity_ordered*150
            else:
                bill_amount=-1 
        else:
            bill_amount=-1;
    else:
        bill_amount=-1;
    return bill_amount

print("total bill amount to be paid",func("Non-Veg",4,9))            
                       
                                    
                     
    
