#########################################################################
#                                                                       #
# Project           : Network Intrusion Detection System for IoT        #
#                                                                       #
# Program name      : preprocessing-2.py                                #
#                                                                       #
# Authors           : Gustavo Vitral Arbex, Kétly Gonçalves Machado,    #
#                     Daniel Macêdo Batista, Roberto Hirata Junior      #
#                                                                       #
# Date created      : 20200617                                          #
#                                                                       #
# Purpose           : Preprocesses the data from BoT-IoT dataset and    #
#                     generates a .csv file containing all the normal   #
#                     traffic instances and a sample of the DDoS attack #
#                     traffic instances.                                #
#                                                                       #
#########################################################################

import csv

# Generates a .csv file containing all the normal traffic from the BoT-IoT dataset and a sample of the DDoS attack traffic

with open('bot-iot.csv', 'w') as botiot:
    
    spamwriter = csv.writer(botiot, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    with open('botiot-preprocessed-normal.csv', 'r') as n:
        csv_reader = csv.reader(n, delimiter=',')
        for row in csv_reader:
            spamwriter.writerow(row)
    
    with open('botiot-preprocessed.csv', 'r') as a:
        csv_reader = csv.reader(a, delimiter=',')
        i = 0
        for row in csv_reader:
            if i % 100 >= 1 and i % 100 <= 5:
                spamwriter.writerow(row)
            i = i + 1