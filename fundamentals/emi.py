#write a program to calculate monthly emi
loan_amount=200000 #P
tenure=10 #N
interest_rate=9 #R
#emi=[P*R*(1+R)^N]/[(1+R)^N-1]
monthly_interest_rate=interest_rate/(12*100)
tenure_in_month=tenure*12

emi=loan_amount*monthly_interest_rate*(1+monthly_interest_rate)**tenure_in_month/((1+monthly_interest_rate)**tenure_in_month-1)
print(f"monthly emi={emi}")

#total interest payable
