
def exact_change(ammount: int):
    
    penny = 0
    nickle = 0
    dime = 0
    quarter = 0
    #dollar = 0

    tot_change = ammount
    
    
    while True:

        #if tot_change / 100 >= 1:
        # tot_change -= 100
        # dollar += 1
        #  continue

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

    return penny,nickle,dime,quarter


if __name__ == "__main__":
    
    tot_change = int(input())   

    if tot_change == 0:
        print("no change")
    else:

        penny,nickle,dime,quarter = exact_change(tot_change)
        
        #penny = 1
        #nickel = 5
        #dime = 10
        #quarter = 25
        #dollar = 100


        #dollar_name = "Dollar"
        quarter_name = "quarter"
        dime_name = "dime"
        nickle_name = "nickel"
        penny_name = "penny"


        #if dollar > 1: dollar_name = "dollars"
        if quarter > 1: quarter_name = "quarters"
        if dime > 1: dime_name = "dimes"
        if nickle > 1: nickle_name = "nickels"
        if penny > 1: penny_name = "pennies"

    
  
        #if dollar != 0:
        #  print(dollar, dollar_name)
        
        if penny != 0:
            print(penny, penny_name)

        if nickle != 0:
            print(nickle, nickle_name)

        if dime != 0:
            print(dime, dime_name)

        if quarter != 0:
            print(f"{quarter} {quarter_name}")
    

 

    

    