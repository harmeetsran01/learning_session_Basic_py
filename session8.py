I have hdfc bank credit Card 
HDFC Bank will charge 15% interest on outstanding amount
Min, you should be able to pay 10% of outstanding amount else your credit score will be compromised

April,2024 -> 50000
I can only pay max of 8000 per month -> Input by User 
April, 2024 min, ->5000 (cannot choose amount less than 10%)
    pending 45000
        + 15% OF 45000
            6750

Your Job is to find, in which month whole amount will become 0




Here are the point to be noted:

    credit_card:
        debit_amout: , 
        amount_to_be_paid_at_intial: ( ! =< 10% of amount )  ,  
        remaining_amount: debit - amount_to_be_paid_at_intial
        installment_amount:  ( ! =< 10% of amount )  ,  


now:

    total_money= loan_amout_to_be_return + amount_to_be_paid_at_intial
    loan_amout_to_be_return : + %15 of remaining_amount
    loan_amout_to_be_return = loan_amout_to_be_return - installment_amount , using recursive function
    
    
    months={1:"January",2:"Feburary",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"Nomber",12:"December"} using loop
    months=["January","Feburary","March","April","May","June","July","August","September","October","Nomber","December"] 
    month +=1
    year= if month==months[11], then year + 1

    if loan_amout_to_be_return <= 0, print month



yeartemp = mth // 12
mth= mth % 12
year = year + yeartemp
for i in range (0,11):
    months[i]