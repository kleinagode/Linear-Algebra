
def main():
    inp = input()
    password = inp.replace("i","1").replace("a", "@").replace("m", "M").replace("B", "8").replace("s", "$") + "!"
    print(password)



main()