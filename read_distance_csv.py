import csv

##Creates a new matrix to make the distanceCSV file usable
def read_distance_csv(filename):
    distance_matrix = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for i, row in enumerate(csvreader):
            #Initialize a new row for the matrix
            distance_matrix.append([0.0] * (i + 1))  #Fill with zeros for lower triangle

            for j in range(i):  #Only read up to the current row index (upper triangle)
                if row[j] != '':  #Ignore empty values
                    distance_value = float(row[j])
                    #Set both symmetric positions in the matrix
                    distance_matrix[i][j] = distance_value
                    distance_matrix[j].append(distance_value)  #Append to the existing row in lower triangle

            #Fill out the rest of the row to match the size of the matrix
            distance_matrix[i].extend([0.0] * (len(distance_matrix) - len(distance_matrix[i])))

    return distance_matrix