months=["January","Feburary","March","April","May","June","July","August","September","October","November","December"] 

mth=int(input("Enter a month in Number: ",))

# by default the YEAR value will be
year=2024
yeartemp =int(mth // 12)
year = year + yeartemp

print(mth," is ",months[(mth%12)-1]," ",year)


currentMonth=int(input("Want to enter Current Month? If Yes enter Current Month: "))
mth = currentMonth + mth

yeartemp =int(mth // 12)
year = year + yeartemp

print(mth," is ",months[(mth%12)-1]," ",year)


