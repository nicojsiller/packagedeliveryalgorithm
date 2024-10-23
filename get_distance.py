from normalize_address import normalize_address

##Returns the distance to the next address as a float
def get_distance(distance_matrix, address_to_index, address1, address2):

    #Normalize the addresses to lowercase before searching
    address1 = normalize_address(address1)
    address2 = normalize_address(address2)
    #Retrieves the indices for the two addresses from the address_to_index dictionary
    index1 = address_to_index.get(address1)
    index2 = address_to_index.get(address2)

    #Check if indices are valid
    if index1 is None or index2 is None:
        raise ValueError(f"One or both addresses not found: {address1}, {address2}")

    #Ensures the smaller index comes first to handle blank cells in the upper triangle of the matrix
    return distance_matrix[max(index1, index2)][min(index1, index2)]