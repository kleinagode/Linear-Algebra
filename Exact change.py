
tot_change = int(input())

equals_zero = False

if tot_change == 0:
    equals_zero = True

#penny = 1
#nickel = 5
#dime = 10
#quarter = 25
#dollar = 100

penny = 0
nickle = 0
dime = 0
quarter = 0
dollar = 0

dollar_name = "Dollar"
quarter_name = "Quarter"
dime_name = "Dime"
nickle_name = "Nickel"
penny_name = "Penny"

while True:

    if tot_change / 100 >= 1:
        tot_change -= 100
        dollar += 1
        continue

    if tot_change / 25 >= 1:
        tot_change -= 25
        quarter += 1
        continue

    if tot_change / 10 >= 1:
        tot_change -= 10
        dime += 1
        continue

    if tot_change / 5 >= 1:
        tot_change -= 5
        nickle += 1
        continue

    if tot_change < 5:
        penny += tot_change
        tot_change -= tot_change
        

    if tot_change == 0:
        break

if dollar > 1: dollar_name = "Dollars"
if quarter > 1: quarter_name = "Quarters"
if dime > 1: dime_name = "Dimes"
if nickle > 1: nickle_name = "Nickels"
if penny > 1: penny_name = "Pennies"

if equals_zero:
    print("No change")
else:
    if dollar != 0:
        print(dollar, dollar_name)
    if quarter != 0:
        print(f"{quarter} {quarter_name}")

    if dime != 0:
        print(dime, dime_name)

    if nickle != 0:
        print(nickle, nickle_name)

    if penny != 0:
        print(penny, penny_name)