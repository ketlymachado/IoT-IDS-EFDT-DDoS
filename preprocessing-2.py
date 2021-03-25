#########################################################################
#                                                                       #
# Project           : Network Intrusion Detection System for IoT        #
#                                                                       #
# Program name      : preprocessing-2.py                                #
#                                                                       #
# Authors           : Gustavo Vitral Arbex, Kétly Gonçalves Machado,    #
#                     Daniel Macêdo Batista, Roberto Hirata Junior      #
#                                                                       #
# Purpose           : Preprocesses the data from BoT-IoT dataset and    #
#                     generates a .csv file containing all the normal   #
#                     traffic instances and a sample (or all) of the    #
#                     DDoS attack traffic instances.                    #
#                                                                       #
#########################################################################

import csv
import time
import argparse

parser = argparse.ArgumentParser(description = 'Preprocessing 2')
parser.add_argument('-p', action = 'store', dest = 'p', 
                    default = '100', required = False,
                    help = 'Percentage of attack instances to be considered.')

args = parser.parse_args()

start_time = round(time.time(), 0)

# Generates a .csv file containing all the normal traffic from the BoT-IoT dataset and a sample (or all) of the DDoS attack traffic

with open('botiot.csv', 'w') as botiot:
    
    count = -1 # Ignores first row which is the feature names
    spamwriter = csv.writer(botiot, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    with open('botiot-preprocessed-normal.csv', 'r') as n:
        csv_reader = csv.reader(n, delimiter=',')
        for row in csv_reader:
            spamwriter.writerow(row)
            count = count + 1
    
    with open('botiot-preprocessed-ddos.csv', 'r') as a:
        csv_reader = csv.reader(a, delimiter=',')
        i = 0
        for row in csv_reader:
            if i > 0 and i % 100 < int(args.p):
                spamwriter.writerow(row)
                count = count + 1
            i = i + 1

    time_final = round(time.time(), 0)
    time_min = int((time_final - start_time) / 60)
    time_sec = int((time_final - start_time) % 60)

    print("\n")
    print(f"Final number of instances (normal + attack) = {count}")
    print("\n")
    print(f"--- {time_min}m{time_sec}s ---")
    print("\n")