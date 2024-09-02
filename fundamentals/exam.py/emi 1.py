#monthly emi?
#total intrest payable?
#total payment?
#p=> loan amount
#r=>interest rate(p.a)
#t=>tenure(years)=>mont
loan_amount=int(input("total loan amount:"))
interest_rate_year=float(input("enter the yearly interest reate:"))
tenure=float(input("enter the tenure in years:"))
interest_rate_month=interest_rate_year/(12*100)
tenure_in_months=tenure*12
monthly_emi=loan_amount*interest_rate_month*(1+interest_rate_month)**tenure_in_months//((1+interest_rate_month)**tenure_in_months-1)
print(f"your monthly emi is{monthly_emi}")
total_amount_payable=monthly_emi*tenure_in_months
print(f"your total amount payable is{total_amount_payable}")
total_interest=total_amount_payable-loan_amount
print(f"your total interest is{total_interest}")

