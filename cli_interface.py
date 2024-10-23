from display_package_status_at_time import display_package_status_at_time
from display_total_mileage import display_total_mileage
from display_package_by_id import display_package_by_id
from Truck import truck1_packages, truck2_packages, truck3_packages

##Main CLI function
def cli_interface(package_hash_table, trucks):
    print("Welcome to the WGUPS Tracking System")
    print("You can view package statuses and the total mileage traveled by trucks.")

    while True:
        print("\nOptions:")
        print("1. View package statuses at a specific time")
        print("2. View total mileage traveled by all trucks")
        print("3. View details of a specific package by ID")
        print("4. Exit")

        user_choice = input("Enter your choice (1/2/3/4): ")

        #Calls the function 'display_package_status_at_time' based on the input time
        if user_choice == '1':
            query_time_str = input("Enter a time to check the status (e.g., 9:00 AM): ")
            display_package_status_at_time(package_hash_table, trucks, query_time_str, truck1_packages, truck2_packages, truck3_packages)

        #Calls the function 'display_total_mileage'
        elif user_choice == '2':
            display_total_mileage(trucks)

        #Calls the function 'display_package_by_id'
        elif user_choice == '3':
            package_id = int(input("Enter the package ID: "))
            display_package_by_id(package_hash_table, trucks, package_id)

        elif user_choice == '4':
            print("Exiting the WGUPS Tracking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")