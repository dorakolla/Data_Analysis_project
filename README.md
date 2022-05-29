# Data_Analysis_project
## How to setup the Project in your Local System
There is only one file in project.You can use any texteditor or IDE to run the app.py file
### packages to install
```python
pip install streamlit
pip install plotly
```
Test that the installation worked:
```python
streamlit hello
```
Create virtual environment 
```python
python -m venv .venv
```
After that run the following command in terminal
```python
streamlit run app.py
```
It open a new localhost that runs on a browser.

### About the Project
This a web app which is based on data anlysis on automative industry dataset.
***
This project majorly classified on four major categories on anlysis of car in automative Industry
* Safety and security
* Technology
* Performance
* Quality

For each factor there associated regarding sub factors in each section of handing that factor.
#### In safety
***
* Forward_Collision_Prevention
* Braking_Tire_Pressure_and_Anti_Rollover
* DriverState_MonitoringandCommunication
* Lane_and_Side_Assisting

#### In Performance
***
* power_torque
* Engine performance
* Brakes
* Mileage
* Power_steering

#### In Technology
***
* Communication
* tech_Parking_and_controlling_assistance
* tech_seating_and_stearing
* Saftey

For Quality there is only few features.
I made seperate query for each subfactor.
First while entering into the app,there is a side bar Where you can two sections.
Choosing the query and Downside of that there is column selections where you can choose the columns that to deploy on screen of a dataset.





