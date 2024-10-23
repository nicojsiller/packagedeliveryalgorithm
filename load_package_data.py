from ChainingHashTable import ChainingHashTable
from Package import Package
import csv

##Read and save the data in the package CSV file directly into a hash map
def load_package_data(filename):
    #Creates a hash table for packages
    package_hash_table = ChainingHashTable()
    with open('packageCSV.csv', mode ='r') as package_csv:
        package_data = csv.reader(package_csv)
        for package in package_data:
            packageID = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zipCode = package[4]
            deadline = package[5]
            weight = package[6]
            #All packages will initially be located at the hub
            status = "At Hub"

            #Create package object using the existing Package class
            package = Package(packageID, address, city, state, zipCode, deadline, weight, status)

            #Insert the package object into the hash table
            package_hash_table.insert(packageID, package)

            #Debugging
            #print(f"Package Manifest Data: {package}")
        return package_hash_table