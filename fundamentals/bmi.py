#write a programe to calculate bmi
#bmi=(weight_in_kg/height_in_meter_square)

weight_in_kg=72
height_in_cm=165
height_in_m=165/100 #1.65
height_in_meter_square=1.65**2

bmi_result=(weight_in_kg/height_in_meter_square)
print(f"{weight_in_kg}/{height_in_meter_square}={bmi_result}")