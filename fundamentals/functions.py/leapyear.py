
def is_leep_year(year):
    if year%100==0  and year%400==0 or year%100!=0 and year%4==0:
        return True


    else:
        return False    



print(is_leep_year(2024))


#create a function nth_digit_max with two parameter
#nth_digit_max(123,480) =>123
#nth_digit_max(546,127)=>127


def nth_digit_max(num1,num2):
    return num1 if num1%10 > num2%10 else num2

print(nth_digit_max(127,450))