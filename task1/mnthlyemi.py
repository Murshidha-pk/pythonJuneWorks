
#monthly emi
#total payment
#total interest payable
# emi=[P*R*(1+R)^N]/[(1+R)^N-1]
# p=loan amount
#R=interest rate
#tenur(years)--->month

loan_amount=int(input("enter loan amount:")) #p

interest_rate_year=float(input("enter interest year:")) #R

tenure=float(input("enter tenure in years:"))

interest_rate_month=interest_rate_year/(12*100)

tenure_in_month=tenure*12

monthly_emi=loan_amount*interest_rate_month*(1+interest_rate_month)**tenure_in_month//((1+interest_rate_month)**tenure_in_month-1)

print(f"monthly emi---{monthly_emi}")

total_payment=monthly_emi*tenure_in_month

print(f"total pyment----{total_payment}")

total_interest_payable=total_payment-loan_amount

print(f"total interest payable----{total_interest_payable}")






