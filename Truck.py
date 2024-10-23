#from mark_departure_time import mark_departure_times
import datetime

#Creates a new truck object

#Most of these parameters are taken from the written section of the rubric
#Capacity, Speed, Mileage, Departure Time, Current Address, Packages list

#Set the status for the trucks by default as "At Hub"

class Truck:
    def __init__(self, capacity, speed, mileage, departureTime, currentAddress, truck_id):
        self.capacity = capacity
        self.speed = speed
        self.mileage = mileage
        self.departureTime = departureTime
        self.currentAddress = currentAddress
        self.packages = []
        self.original_packages = []
        self.truck_id = truck_id

    #Checks to make sure the capacity is not exceeded and adds the packages to the list
    def load_packages(self, package_objects):
        if len(self.packages) + len(package_objects) <= self.capacity:
            self.packages.extend(package_objects)
            self.original_packages.extend(package_objects)
        else:
            print("Cannot load packages: Exceeds truck capacity.")

    def __str__(self):
        package_ids = [package.packageID for package in self.packages]
        return (f"Truck Info:\n"
                f"Capacity: {self.capacity} packages\n"
                f"Speed: {self.speed} mph\n"
                f"Mileage: {self.mileage} miles\n"
                f"Departure Time: {self.departureTime}\n"
                f"Current Address: {self.currentAddress}\n"
                f"Packages Loaded: {package_ids}\n"
                f"Truck: {self.truck_id}")

##Initialize three instances of the truck object and manually load each of the packages onto the trucks
truck1 = Truck(capacity=16, speed=18, mileage=0, departureTime="08:00 AM", currentAddress="4001 South 700 East", truck_id=1)
truck2 = Truck(capacity=16, speed=18, mileage=0, departureTime="09:05 AM", currentAddress="4001 South 700 East", truck_id=2)
truck3 = Truck(capacity=16, speed=18, mileage=0, departureTime="11:00 AM", currentAddress="4001 South 700 East", truck_id=3)

#Truck 1 contains packages with early deadlines and those without special instructions
truck1_packages = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]

#Truck 2 contains packages with truck 2 only constraints and EOD deadlines
truck2_packages = [2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 18, 25, 36, 38]

#Truck 3 contains packages that have a delayed arrival time
truck3_packages = [9, 17, 21, 22, 23, 24, 26, 27, 28, 32, 33, 35, 39]

#Debugging
#print(f"Truck 1: {truck1.truck_id}, {truck1.capacity}, {truck1.speed}, {truck1.mileage}, {truck1.departureTime}, {truck1.packages}")




