
wght_in_kg=int(input("enter your weight"))

hght_in_cm=int(input("enter your height "))

height_in_m=hght_in_cm/100

height_in_m_sqr=height_in_m**2

bmi=(wght_in_kg/height_in_m_sqr)

print(f"your bmi is {wght_in_kg}/{height_in_m_sqr}={bmi}")