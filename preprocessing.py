#########################################################################
#                                                                       #
# Project           : Network Intrusion Detection System for IoT        #
#                                                                       #
# Program name      : preprocessing.py                                  #
#                                                                       #
# Authors           : Gustavo Vitral Arbex, Kétly Gonçalves Machado,    #
#                     Daniel Macêdo Batista, Roberto Hirata Junior      #
#                                                                       #
# Purpose           : Preprocesses the data from BoT-IoT dataset and    #
#                     generates 2 .csv files containing normal and DDoS #
#                     attack traffic instances.                         #
#                                                                       #
#########################################################################

import csv
from progress.bar import Bar

# Generates a .csv file containing all the normal traffic instances in the BoT-IoT dataset

with open('UNSW_2018_IoT_Botnet_Dataset_Feature_Names.csv') as f:
    with open('botiot-preprocessed-normal.csv', 'w') as n:
        n.write(f.read() + "\n")

with open('botiot-preprocessed-normal.csv', 'a', newline='') as n:

    spamwriter = csv.writer(n, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    print("\n")

    count_normal = 0
    bar = Bar('Processing', max = 74)
    for i in range(1, 75):
        with open('UNSW_2018_IoT_Botnet_Dataset_' + str(i) + '.csv') as d:

            csv_reader = csv.reader(d, delimiter=',')

            for row in csv_reader:
                if row[33] == 'Normal':
                    spamwriter.writerow(row)
                    count_normal = count_normal + 1
        bar.next()
    bar.finish()
    print(f"Total normal instances = {count_normal}")

# Generates a .csv file containing all the DDoS attack traffic instances in the BoT-IoT dataset

with open('UNSW_2018_IoT_Botnet_Dataset_Feature_Names.csv') as f:
    with open('botiot-preprocessed-ddos.csv', 'w') as a:
        a.write(f.read() + "\n")

with open('botiot-preprocessed-ddos.csv', 'a', newline='') as a:

    spamwriter = csv.writer(a, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    print("\n")

    count_ddos = 0
    bar = Bar('Processing', max = 74)
    for i in range(1, 75):
        with open('UNSW_2018_IoT_Botnet_Dataset_' + str(i) + '.csv') as d:

            csv_reader = csv.reader(d, delimiter=',')

            for row in csv_reader:
                if row[33] == 'DDoS':
                    spamwriter.writerow(row)
                    count_ddos = count_ddos + 1
        bar.next()
    bar.finish()
    print(f"Total DDoS attack instances = {count_ddos}")
    print("\n")