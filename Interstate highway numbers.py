
def main():
    
    highway_number = int(input())
    check = True

    if highway_number > 999 or highway_number < 1 or highway_number % 100 == 0:
        check = False    
    

    if highway_number > 0 and highway_number < 100 and check:
        direction = "north/south" if (highway_number % 2 ) else "east/west"
        print(f"I-{highway_number} is primary, going {direction}.")
    elif highway_number >  99 and highway_number < 1000 and check:
        str_num = str(highway_number)
        if str_num[1] == "0":
            i_highway = int(str_num[2])
        else:
            i_highway = int(str_num[1]+str_num[2])
        
        direction = "north/south" if (i_highway % 2 ) else "east/west"
        
        print(f"I-{highway_number} is auxiliary, serving I-{i_highway}, going {direction}.")

    if not check:
        print(f"{highway_number} is not a valid interstate highway number.")

main()