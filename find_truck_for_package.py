

def find_truck_for_package(truck1_packages, truck2_packages, truck3_packages, package_id):
    #Check if the package ID is in Truck 1's package list
    if package_id in truck1_packages:
        return "1"
    #Check if the package ID is in Truck 2's package list
    elif package_id in truck2_packages:
        return "2"
    #Check if the package ID is in Truck 3's package list
    elif package_id in truck3_packages:
        return "3"
    #If the package ID is not found in any of the truck lists, return None
    return None
