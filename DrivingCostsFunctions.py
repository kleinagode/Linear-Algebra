def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):

    return (miles_driven / miles_per_gallon) * dollars_per_gallon

def gas_cost():

    mph = float(input())
    dpg = float(input())
    
    print(f"{driving_cost(mph,dpg,10.0):.2f}")
    print(f"{driving_cost(mph,dpg,50.0):.2f}")
    print(f"{driving_cost(mph,dpg,400.0):.2f}")




if __name__ == '__main__':
    gas_cost()
    

