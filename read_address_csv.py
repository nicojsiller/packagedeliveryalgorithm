from normalize_address import normalize_address
import csv

##Read and save the data in the address CSV file to a list
def read_address_csv():
    #Stores the address data in a list
    address_list = []
    #Allows the get_distance function to look up an index based on the given address
    address_to_index = {}

    with open('addressCSV.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        # Appends each new row into the address list
        for i, row in enumerate(csv_reader):
            index = row[0]
            building_name = row[1]
            street_address = row[2]
            #Normalizing the address to lowercase to prevent typecase errors
            normalized_address = normalize_address(street_address)
            address_list.append(normalized_address)
            #Map the normalized address to its index
            address_to_index[normalized_address] = i

            #print("Address to Index Mapping:")
            #for address, idx in address_to_index.items():
                #print(f"{address}: {idx}")

            # Debugging
            # print(f"Loaded index: {index}")
            # print(f"Loaded building: {building_name}")
            # print(f"Loaded address: {normalized_address}")

    return address_list, address_to_index