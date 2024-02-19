# Preprocessing of BoT-IoT Dataset

- Download all files from [here](https://unsw-my.sharepoint.com/personal/z5131399_ad_unsw_edu_au/_layouts/15/onedrive.aspx?ga=1&id=%2Fpersonal%2Fz5131399%5Fad%5Funsw%5Fedu%5Fau%2FDocuments%2FBot%2DIoT%5FDataset%2FDataset%2FEntire%20Dataset)
- Execute preprocessing.py
    - It will generate a new .csv file containing feature names + all normal instances and a new .csv file containing feature names + all DDoS attack instances

- Execute preprocessing-2.py
    - It will generate a single .csv file containing feature names + all normal instances + a sample or all of the DDoS attack instances

- Execute adasyn.py
    - It will generate a new .csv file with the resampled data after applying the ADASYN technique
