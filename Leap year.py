is_leap_year = False

is_century = False
   
input_year = int(input())

if input_year % 100 == 0:
    is_century = True

if is_century and input_year % 400 == 0:
    is_leap_year = True  

if not is_century and input_year % 4 == 0:
    is_leap_year = True

if is_leap_year:
    print(f"{input_year} - leap year") 
else:
    print(f"{input_year} - not a leap year") 
    
