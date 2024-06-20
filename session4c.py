#just made a ZOMATO and SWIGGY total and promo_code working application 
# promo_code= "ZOMATO"
min_amount=249
#condition 50% off upto 150

amount=float(input("Enter Amount: "))
promo_code=input("Enter promo_code")
if promo_code=="ZOMATO":
    print("PromoCode is Valid")

    if amount>min_amount:
        print("Promo code is applied ")
        discount
    else:
        print("Amount is low")

#  \u means unicode = special character which were used to define currency and other backgrounds
#  \u unicode for rupee is \u20b9
#   https://symbl.cc/en/unicode-table for unicode