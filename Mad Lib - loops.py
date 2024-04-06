
while True:
    input_string = input().split()

    if input_string[0] == "quit":
        break

    print(f"Eating {input_string[1]} {input_string[0]} a day keeps you happy and healthy.")