#Normalizes the address data from the address CSV file
#Used to solve an issue I was having with the address not properly being identified
def normalize_address(address):
    return address.strip().lower()