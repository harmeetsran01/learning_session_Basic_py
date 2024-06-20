promo_code="GET200"

#Condition1: You can apply promo code only if the amount wil exceed 500 or min 500
#condition2: 

min_amount=500

amount= float(input("Enter your amount: "))

if amount > min_amount:
    print("You can apply the Promocode\nEnter the Promo-_code")
                  #   You get discount off: 200 ","Pay ",amount-200," to procedd the transaction"
    
    
else:
    print("You cannot add the promo code")
    print("Add items worth", min_amount - amount)




