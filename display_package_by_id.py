from find_truck_for_package import find_truck_for_package
from Truck import truck1_packages, truck2_packages, truck3_packages

def display_package_by_id(package_hash_table, trucks, package_id):
    package = package_hash_table.search(package_id)
    if not package:
        print(f"No package found with ID: {package_id}")
        return

    #Calls the function find_truck_for_package to find the truck that has the specific package
    truck_id = find_truck_for_package(truck1_packages, truck2_packages, truck3_packages, package_id)

    #Display the package information
    status = "Delivered" if package.deliveryTime else "En Route" if package.departureTime else "At Hub"
    delivery_time = package.deliveryTime if package.deliveryTime else "N/A"

    print(f"Package {package.packageID} Information:")
    print(f"Address: {package.address}"
          f" City: {package.city}"
          f" State: {package.state}"
          f" Zip: {package.zipCode}"
          f" Delivery Deadline: {package.deadline}"
          f" Mass: {package.weight} kilos"
          f" Status: {status} by Truck {truck_id}"
          f" Delivery Time: {delivery_time}")