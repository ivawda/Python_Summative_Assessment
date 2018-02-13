import random
import csv
from datetime import datetime

# User message
print('Generating the sensor network dataset...')

# Create a list to hold all the generated sensor date for the entire sensor network
# The sensor network contains 32 clusters and each cluster contains 16 sensors
sensor_network = [[random.random() for i in range(0, 16)] for j in range(0, 32)]

# User message
print('Dataset generated.\nCorrupting the dataset...')

# Corrupt the dataset whereby a random entries in the sensor network will have an 'err' string value
# The 'err' value indicates a broken sensor
randomList = [n for n in range(0, 16)]

a = random.choice(randomList)
b = random.choice(randomList)
sensor_network[a][b] = 'err'

# User message
print('Created an error at Cluster{0}_Sensor{1}.'.format(a+1, b+1))


def get_timestamp():
    """Returns the current date and time in the dd/mm/yyyy hh:mm:ss format."""

    # Get the current local date and time
    time_now = datetime.now()

    return time_now.strftime('%d/%m/%Y %H:%M:%S')


# Create a variable to hold the current timestamp
current_timestamp = get_timestamp()

# Timestamp the sensor network dataset
timestamp_sensor_network = [current_timestamp]

# User message
print('Testing the dataset for any errors...')


def test_sensor_network(sensor_network_dataset):
    """Test the sensor network dataset for any 'err' values. Create or append the log file if there are any errors."""

    for x, cluster in enumerate(sensor_network_dataset):
        for y, sensor_value in enumerate(cluster):
            try:
                # Convert each sensor value to an int, an error will occur when 'err' string is passed
                test = int(sensor_value)
            except ValueError:
                # User message
                print('Error detected!\nWriting error message to log file...')

                # Change the error string to a identifiable numeric value i.e. error = -1
                sensor_network_dataset[x][y] = -1

                # Write an error message in the log file
                with open('error.log', 'a') as logfile:
                    logfile.write('{0}\t\tError at Cluster{1}_Sensor{2}'.format(current_timestamp, x+1, y+1))
                    logfile.write('\n')


# Call the function to test the sensor network
test_sensor_network(sensor_network)

# User message
print('Writing the corrupt data set to file...')

# Serialise the sensor network dataset to a single list for writing to csv file
for cluster in sensor_network:
    for value in cluster:
        timestamp_sensor_network.append(value)

# Write the dataset to file
with open('corrupt_dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(timestamp_sensor_network)

# User message
print('Dataset written to file.\nDone!')


# OPTIONAL CODE:
# The code below is used to generated a csv file with a header for storing the sensor network


def create_header_list():
    """Returns a list containing the parameters for the csv header"""

    # The first header parameter is the date time stamp
    header = ['Timestamp']

    for i in range(1, 33):
        for j in range(1, 17):
            value = 'Cluster{0}_Sensor{1}'.format(i, j)
            header.append(value)

    return header


def create_new_csv_file():
    """Creates a new csv file with a header for storing the corrupt sensor network dataset"""

    with open('corrupt_dataset.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        header = create_header_list()
        writer.writerow(header)
