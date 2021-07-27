# deepnav_model

A Neural Network model trained on motion sensor data and gps data from phones while driving a car.
The Network trained to regress acceleration of the car using motion sensor data(gyroscope and accelerometer).  
the end goal is to create a basic inertial navigation system.

# current phase  
Regression isn't reliable enough on the current architecture. Experimenting on different architectures.

# data pipeline 
The data is collected on the phone and when the drive is over is sent by email to a pre Defined email.  
an email crawler using python grabs all the data from the detected email and saves it.  
a python scipt extracts and organize all the relevant data.
