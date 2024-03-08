

while True:
    inp = input()
    if inp == "d" or inp == "Done" or inp == "done":
        break
    
    for i in range(len(inp)-1,-1,-1):
        print(f"{inp[i]}",end="")
    print()

