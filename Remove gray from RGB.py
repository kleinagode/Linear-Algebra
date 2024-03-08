
def main():
    
    R = int(input())
    G = int(input())
    B = int(input())

    RGB_List = [R, G, B]

    gray = min(RGB_List)

    R -= gray
    G -= gray
    B -= gray

    print(R, G, B)


main()