import datetime

##Function to display the status of packages at a specific time when selecting '1' from the CLI
def display_package_status_at_time(package_hash_table, trucks, query_time_str, truck1_packages, truck2_packages, truck3_packages):
    #Converts the query time string to a datetime object
    query_time = datetime.datetime.strptime(query_time_str, '%I:%M %p')

    #Confirm the time that the user has entered
    print(f"Package status as of {query_time_str}:")

    #Sort the package hash table items by package ID in ascending order
    sorted_packages = sorted(package_hash_table.items(), key=lambda item: item[0])

    #Iterate through the sorted packages to display the status at a given time
    for package_id, package in sorted_packages:
        #Ensure the package exists
        if package:
            package_status = package.status_time(query_time, truck1_packages, truck2_packages, truck3_packages)
            print(package_status)