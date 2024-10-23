#Nico Siller 010766597
#C950 Task 2 WGUPS Implementation Program

#Including necessary dependencies and functions
from nearest_neighbor_algorith import nearest_neighbor_algorithm
from cli_interface import cli_interface
from load_package_data import load_package_data
from read_distance_csv import read_distance_csv
from read_address_csv import read_address_csv
from Truck import truck1, truck2, truck3, truck1_packages, truck2_packages, truck3_packages

#Load the package objects into the package hash table
filename = 'packageCSV.csv'
package_hash_table = load_package_data(filename)

#Loads each of the packages into their respective trucks based on the manual assignment in the truck class
truck1.load_packages([package_hash_table.search(packageID) for packageID in truck1_packages])
truck2.load_packages([package_hash_table.search(packageID) for packageID in truck2_packages])
truck3.load_packages([package_hash_table.search(packageID) for packageID in truck3_packages])


class Main:
    def __init__(self):
        print("Loading address and distance data...")
        #Load address data from CSV
        self.address_list, self.address_to_index = read_address_csv()
        #Load distance matrix from CSV
        self.distance_matrix = read_distance_csv('distanceCSV.csv')

        print("Starting delivery process...")
        #Ensure deliveries are run before starting the CLI
        self.run_deliveries()

        print("Starting CLI interface...")
        #Starts the CLI
        cli_interface(package_hash_table, [truck1, truck2, truck3])

    def run_deliveries(self):
        #Runs the delivery process for Truck 1
        print("Running deliveries for truck 1")
        nearest_neighbor_algorithm(truck1, self.address_list, self.distance_matrix, self.address_to_index)

        #Runs the delivery process for Truck 2
        print("Running deliveries for truck 2")
        nearest_neighbor_algorithm(truck2, self.address_list, self.distance_matrix, self.address_to_index)

        #Runs the delivery process for Truck 3
        print("Running deliveries for truck 3")
        nearest_neighbor_algorithm(truck3, self.address_list, self.distance_matrix, self.address_to_index)

if __name__ == "__main__":
    #Instantiate Main to start the program
    main_instance = Main()