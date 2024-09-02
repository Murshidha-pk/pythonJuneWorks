
height_in_cm=int(input("enter your height"))

weight_in_kg=int(input("enter your height"))

height_in_m=height_in_cm/100

height_in_m_sqr=height_in_m**2

bmi=(weight_in_kg/height_in_m_sqr)

print(f"your bmi={bmi}")

if bmi<=19:

    print("you is underweight")

elif bmi<=25:

    print("you is normal weight")

elif bmi<=30:

    print("over weight")

else:

    print("obesity")