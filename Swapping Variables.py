
def swap_values(a:int, b:int, c:int, d:int) -> int: 
    i = 0
    i = a
    a = b
    b = i

    j = 0
    j = c
    c = d
    d = j
    
    return a,b,c,d


if __name__ == '__main__': 
    
    a,b,c,d = swap_values(int(input()),int(input()),int(input()),int(input()))
    print(a,b,c,d)