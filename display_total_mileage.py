from Truck import truck1, truck2, truck3


##Function to display total mileage of all trucks
def display_total_mileage(trucks):
    #Sums the mileage travelled by each of the trucks
    total_mileage = sum([truck1.mileage + truck2.mileage + truck3.mileage])
    print(f"Truck 1 Mileage: {truck1.mileage}")
    print(f"Truck 2 Mileage: {truck2.mileage}")
    print(f"Truck 3 Mileage: {truck3.mileage}")
    print(f"Total mileage traveled by all trucks: {total_mileage:.2f} miles\n")