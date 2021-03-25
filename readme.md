# Preprocessing of BoT-IoT Dataset

- Download all files from https://cloudstor.aarnet.edu.au/plus/s/umT99TnxvbpkkoE?path=%2FCSV%2FEntire%20Dataset

- Execute preprocessing.py
    - It will generate a new .csv file containing feature names + all normal instances and a new .csv file containing feature names + all DDoS attack instances

- Execute preprocessing-2.py
    - It will generate a single .csv file containing feature names + all normal instances + a sample or all of the DDoS attack instances

- Execute adasyn.py
    - It will generate a new .csv file with the resampled data after applying the ADASYN technique