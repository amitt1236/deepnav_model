# deepnav_model

A Neural Network model trained on motion sensor data and gps data from phones while driving a car.
The Network trained to regress acceleration of the car using motion sensor data(gyroscope and accelerometer).  
the end goal is to create a basic inertial navigation system.

# current phase  
Regression isn't reliable enough on the current architecture. Experimenting on different architectures.

# data collection 
https://github.com/amitt1236/deep-nav

# data pipeline 
After the data is collected on the phone is sent by email to a pre Defined email Address.  
an email crawler using python grabs all the data from the detecated email and saves it localy.(email_crawler.py)  
a python scipt extracts and organize all the relevant data.(data_to_model.py)

# data format
accel = accelerometer   
gyro = gyroscope   

Data format before prossesing

| Longitude     | latitude      | accel x axis | accel y axis | accel z axis | gyro x axis | gyro y axis | gyro z axis|
| ------------- |:-------------:| ------------:|-------------:|-------------:|------------:|------------:|-----------:|

Data format before prossesing

| Longitude     | latitude      | accel x axis | accel y axis | accel z axis | gyro x axis | gyro y axis | gyro z axis| acceleration | azimuth diff |
| ------------- |:-------------:| ------------:|-------------:|-------------:|------------:|------------:|-----------:|-------------:|-------------:|

speed(m/s) is calculated by measuring the distance between two points on one secound interval.  
acceleration  is calculated by the difference in speed between intervals.  
  
azimuth is the direction of driving, and calculated by two Gps Coordinates on one secound interval.  
azimut difference is calculated by the difference in azimuth  between intervals.  

