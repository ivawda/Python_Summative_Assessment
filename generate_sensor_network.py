import random
import csv
from datetime import datetime

# User message
print('Generating the sensor network dataset...')

# Create a list to hold all the generated sensor date for the entire sensor network
# The sensor network contains 32 clusters and each cluster contains 16 sensors
sensor_network = [[random.random() for i in range(0, 16)] for j in range(0, 32)]

# User message
print('Dataset generated.')


def get_timestamp():
    """Returns the current date and time in the dd/mm/yyyy hh:mm:ss format."""

    # Get the current local date and time
    time_now = datetime.now()

    return time_now.strftime('%d/%m/%Y %H:%M:%S')


# User message
print('Adding a date time stamp to the dataset...')

# Create a variable to hold the current timestamp
current_timestamp = get_timestamp()

# Timestamp the sensor network dataset
timestamp_sensor_network = [current_timestamp]


# User message
print('Writing the dataset to file...')

# Serialise the sensor network dataset to a single list for writing to csv file
for cluster in sensor_network:
    for sensor in cluster:
        timestamp_sensor_network.append(sensor)


# Write the dataset to file
with open('sensor_network_dataset.csv', 'a') as csvfile:
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
    """Creates a new csv file with a header for storing the generated sensor network dataset"""

    with open('sensor_network_dataset.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        header = create_header_list()
        writer.writerow(header)

