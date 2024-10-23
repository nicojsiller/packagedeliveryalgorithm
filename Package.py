#Create a new package object
#Provided columns on the CSV file: Package ID, Address, City, State, Zip, Delivery Deadline, Weight, Special Notes
#Additional required fields: Status, Departure Time, Delivery Time
from find_truck_for_package import find_truck_for_package

class Package:

    #Initializes a new package object with the necessary fields
    #Sets the departureTime and deliveryTime as 'None' since these won't be initialized immediately
    def __init__(self, packageID, address, city, state, zipCode, deadline, weight, status, departureTime=None, deliveryTime=None, truck_id=None):
        self.packageID = packageID
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.departureTime = departureTime
        self.deliveryTime = deliveryTime
        self.truck_id = truck_id


    def __str__(self):
        return (f"Package ID: {self.packageID}\n"
                f"Address: {self.address}\n"
                f"City: {self.city}\n"
                f"State: {self.state}\n"
                f"ZIP Code: {self.zipCode}\n"
                f"Deadline: {self.deadline}\n"
                f"Weight: {self.weight}\n"
                f"Status: {self.status}\n"
                f"Departure Time: {self.departureTime if self.departureTime else 'N/A'}\n"
                f"Delivery Time: {self.deliveryTime if self.deliveryTime else 'N/A'}\n"
                f"Truck: {self.truck_id}"
                )

    def status_time(self, query_time, truck1_packages, truck2_packages, truck3_packages):
        import datetime

        #Convert departureTime and deliveryTime to datetime objects if they exist
        departure_time = datetime.datetime.strptime(self.departureTime, '%I:%M %p') if self.departureTime else None
        delivery_time = datetime.datetime.strptime(self.deliveryTime, '%I:%M %p') if self.deliveryTime else None

        #Uses temporary variables for address details to dynamically switch based on query time
        address, city, zipCode = self.address, self.city, self.zipCode

        #Sets the update time for package 9
        update_time = datetime.datetime.strptime('10:20 AM', '%I:%M %p')

        if query_time < update_time:
            #Before 10:20 AM, use incorrect address details
            address = "300 State St"
            city = "Salt Lake City"
            zipCode = "84103"
            temp_status = "At Hub" if departure_time and query_time < departure_time else "En Route"
        else:
            #After 10:20 AM, use correct address details
            address = "410 S State St"
            city = "Salt Lake City"
            zipCode = "84111"
            temp_status = "At Hub" if departure_time and query_time < departure_time else "Delivered"

        #Finds the truck ID for the package
        truck_id = find_truck_for_package(truck1_packages, truck2_packages, truck3_packages, self.packageID)

        #Returns the required package information on a single line
        return (f"Package ID:{self.packageID} Status:{temp_status} Truck #:{truck_id} "
                f"Depart Time:{self.departureTime} Delivery Time:{self.deliveryTime} "
                f"Deadline:{self.deadline} Weight:{self.weight} "
                f"Address:{address} City:{city} Zip:{zipCode}")

