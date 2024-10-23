import datetime

from get_distance import get_distance

##Use submitted pseudocode as inspiration to recursively check the distance of each package in the package list
def nearest_neighbor_algorithm(truck, address_list, distance_matrix, address_to_index):
    current_address = truck.currentAddress
    total_mileage = truck.mileage
    current_time = datetime.datetime.strptime(truck.departureTime, '%I:%M %p')

    while truck.packages:
        nearest_package = None
        nearest_distance = float('inf')
        for package in truck.packages:
            package.status = "En Route"
            package_address = package.address
            distance_to_package = get_distance(distance_matrix, address_to_index, current_address, package_address)
            #Debugging
            #print(f"Distance from '{current_address}' to '{package_address}': {distance_to_package}")

            #The core of the nearest neighbor algorithm which checks distances between the points
            if distance_to_package < nearest_distance:
                nearest_distance = distance_to_package
                nearest_package = package

        #Update truck mileage and current address
        total_mileage += nearest_distance
        truck.mileage = total_mileage
        current_address = nearest_package.address

        time_taken = datetime.timedelta(hours=(nearest_distance / truck.speed))
        current_time += time_taken

        #Updates the package status and delivery time
        nearest_package.status = "Delivered"
        nearest_package.deliveryTime = current_time.strftime('%I:%M %p')
        nearest_package.departureTime = truck.departureTime
        #Debugging
        print(f"Package: {nearest_package.packageID} Status: {nearest_package.status} TimeStamp: {nearest_package.deliveryTime}")


        #Removes the most recently delivered package to ensure it doesn't go there again
        truck.packages.remove(nearest_package)
        #Debugging to confirm delivery updates
        # print(f"Delivered package {nearest_package.packageID} to {nearest_package.address}.")
        # print(f"Distance to nearest package: {nearest_distance}")
        # print(f"Truck mileage: {truck.mileage:.2f} miles.")
        # print(f"Current time: {current_time.strftime('%I:%M %p')}")

    return total_mileage