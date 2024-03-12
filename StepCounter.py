

def feet_to_steps(feet_walked: float) -> int:

    return(int(feet_walked//2.5))

if __name__ == "__main__":
    print(feet_to_steps(float(input())))
