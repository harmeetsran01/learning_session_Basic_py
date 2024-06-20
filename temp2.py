print("^^^^^^^^^^^^^^^^^          Welcome! to Credit Card Installments Calculator          ^^^^^^^^^^^^^^^^^")
print()
debit_amount=float(input("Enter the Amount you want to Calculate: "))
print()
temp_month=int(input("Enter the current month in Number: "))
year=2024
print()
amount_to_be_paid_at_intial=float(input("As you have to pay some Initial Amount to be processed\nEnter Initial Amount: "))
print()
   
    
if amount_to_be_paid_at_intial < (0.10 * debit_amount):
     print("Your Initial Amount is too low...\nMin : ", 0.10 * debit_amount,"\nYour Credit score will be compromised\nKindly change the amount.")

else:
    print("You can processed with : ", amount_to_be_paid_at_intial)
    print()
      
    installment_amount=float(input("Enter Amount to be paid as Installment : "))
    print()
        
    remaining_amount = debit_amount - amount_to_be_paid_at_intial
        
    if installment_amount == (0.10 * debit_amount) or installment_amount >= (0.10 * debit_amount):
        print()
        for i in range (0,38):
            print("-",end="")

        print()
         
        print("Credit Amount : ",debit_amount)
        print("\nStarting From : ",temp_month)
        print("\nIntial Amount : ", amount_to_be_paid_at_intial )
        print("\nInstallment per Month : ", installment_amount)

        loan_amout_to_be_return = (0.15 * remaining_amount) + remaining_amount
        #declare months
        months=["January","Feburary","March","April","May","June","July","August","September","October","November","December"] 
        print()

        #function
        def calculation(val,mth):
            global year
            if val <=0 or val <=installment_amount :

                print()
                print()

                if mth >= 12:
                    yeartemp = mth // 12
                    year = year + yeartemp
                    print("Your Installments will be 0 in : ",months[mth % 12]," ",year)

                elif mth < 12:
                    print("Your Installments will be 0 in : ",months[mth % 12])
                return val
                    
            val = val - installment_amount

            print("Your Balance in ",mth+1," Month is : ",val)

            mth +=1

            calculation(val,mth)
                
        calculation(loan_amout_to_be_return,temp_month-1)


    else:
        print("Sorry Installment Amount is too low...")
