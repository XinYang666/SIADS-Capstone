# SIADS-Capstone

All the scripts and jypyter notebooks are located in the Main folder. 

Sensors' July data is uploaded while Auguest and September data are too big to get uploaded.

## Files

DataPreparation.py: Should be first executed to get data ready
labelData.py: Labeling the data for supervised learning
Model.ipynb: Modeling the data and evaluation

test0-3.py: playing around with different sensors

data07.csv: Sensor source data from 2021 July
data08.csv: Sensor source data from 2021 August
data09.csv: Sensor source data from 2021 September

X_train.csv: train data, be generated by labelData.py
y_train: label for the train data, be generated by labelData.py
X_test: test data, be generated by labelData.py
y_test: label for the test data, be generated by labelData.py



Energy.py: anomaly energy consumption trend detection
meterEnergy.html: energy consumption data from 60 meters (filtered by 200 meters)
meterEnergy_anomaly.html: with anomaly indicators
meterEnergy_anomaly_zoom.html: some zoom in vis
Energy.7z: data source

