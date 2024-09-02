employee={"name":"hari","dept":"r&D","salary":50000,"combo_offer":1000,"extra_working_days":2}

#print all key values

for k,v in employee.items():

    print(k,v)

#check extra working days present

if("extra_working_days"in employee):

    print("present")

else:

    print("not present")

#=> print employee net pay

if"extra_working_days "in employee:

    net_pay=employee.get("salary")+employee.get("combo_offer")*employee.get("extra_working_days")

    print(net_pay)

else:

    net_pay=employee.get("salary")

    print(net_pay)




