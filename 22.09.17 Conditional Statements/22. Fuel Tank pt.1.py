fuel_type = str(input())
fuel_available = float(input())

if fuel_type == "Diesel" or "Gasoline" or "Gas":
    if fuel_type != "Diesel" and fuel_type != "Gasoline" and fuel_type != "Gas":
        print("Invalid fuel!")
    elif fuel_available >= 25:
        if fuel_type == "Diesel":
            print("You have enough diesel.")
        if fuel_type == "Gasoline":
            print("You have enough gasoline.")
        if fuel_type == "Gas":
            print("You have enough gas.")
    elif fuel_available < 25:
        if fuel_type == "Diesel":
            print("Fill your tank with diesel!")
        if fuel_type == "Gasoline":
            print("Fill your tank with gasoline!")
        if fuel_type == "Gas":
            print("Fill your tank with gas!")
            