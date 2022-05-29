from optparse import Option
import streamlit as st 
import pandas as pd
import os
import plotly.graph_objects as go
import numpy as np
import plotly.express as px
from natsort import index_natsorted

@st.cache
def get_cars_data():
     return pd.read_csv(os.path.join(os.getcwd(),'cars_engage_2022.csv'))

st.set_page_config(layout="wide")
df = get_cars_data()


original_title = '<p style="font-family:Courier; color:Yellow; font-size: 30px;">"Welcome!",Data analytics on automotive industry</p>'
st.markdown(original_title, unsafe_allow_html=True)

add_selectbox = st.sidebar.selectbox(
    "Select the Query",
    ("Which cars have","Which types of Fuel types cars are using most", "Model vs Fuel Tank",
    "saftey in Forward Collision Prevention",
    "saftey in Braking Tire Pressure and Anti Rollover","saftey in Driver State Monitoring & Communication"
    ,"saftey in Lane and Side Assisting","saftey in Parking and Backing Assisting",
    "More engine performance","Performance in Brakes","Performance in Mileage",
    "Performance in Power steering","Technology features in communication","Technology features in Parking and controlling assistance"
    ,"Technology features in seating and stearing","Technology features in Safety"," best in Quality","kerb weight vs milage"
    )
)
     
     
with st.sidebar:
     options = st.multiselect(
     'Choose which are columns You want',df.columns)
if(options!="Choose an option"):
     st.dataframe(df[options])



def modelvsFuel_tank():
     model=df['Model'].tolist()
     Fuel_Tank=df['Fuel_Tank_Capacity'].tolist()
     fig=px.bar(
        x=model, 
        y=Fuel_Tank
    )
     st.plotly_chart(fig)
def Power():
     Power=[]
     power=df['Power'].tolist()
     for i in power:
        Power.append(i[0:2])
     displacement=df['Displacement'].tolist()
     fig=px.line(
        x=Power, 
        y=displacement
    )
     st.plotly_chart(fig)

def kerb_weight_vs_milage():
    kerb=df["Kerb_Weight"].tolist()
    mileage=df["City_Mileage"].tolist()
    fig=px.line(
         x=kerb,
         y=mileage
    )
    st.plotly_chart(fig)


def Safety(key):
     if(key==0):
         Forward_Collision_Prevention=df[(df[("Headlight_Reminder")]=="Yes") & (df["High_Speed_Alert_System"]=="Yes") &(df["Cruise_Control"]=="Yes") &(df["EBA_(Electronic_Brake_Assist)"]=="Yes") &(df["ASR_/_Traction_Control"]=="Yes")]
         Forward_Collision_Prevention.groupby("Make").first()
         st.dataframe(Forward_Collision_Prevention.head(5).iloc[:,[1,2,3]])
     elif(key==1):
         Braking_Tire_Pressure_and_Anti_Rollover=df[(df[("ABS_(Anti-lock_Braking_System)")]=="Yes") & (df["EBA_(Electronic_Brake_Assist)"]=="Yes")  ]
         st.dataframe(Braking_Tire_Pressure_and_Anti_Rollover.head(5).iloc[:,[1,2,3]])
     elif(key==2):
         DriverState_MonitoringandCommunication=df[(df["High_Speed_Alert_System"]=="Yes") & (df["Tyre_Pressure_Monitoring_System"]=="Yes")]
         st.dataframe(DriverState_MonitoringandCommunication.head(5).iloc[:,[1,2,3]])
     elif(key==3):
          Lane_and_Side_Assisting=df[(df["High_Speed_Alert_System"]=="Yes")]
          st.dataframe(Lane_and_Side_Assisting.head(5).iloc[:,[1,2,3]])
     
def Performance(key):
    if(key==4):
        power_torque=df.sort_values(["Power","Torque"],ascending=False,key=lambda x: np.argsort(index_natsorted(df["Power"])))
        st.dataframe(power_torque.head(5).iloc[:,[1,2,3]])
    if(key==5):
         performance=df.sort_values(by=["Displacement","Cylinders","Valves_Per_Cylinder","Power","Torque"],ascending=False,key=lambda x: np.argsort(index_natsorted(df["Power"]))).groupby(["Make"])
         st.dataframe(performance.head(5).iloc[:,[1,2,3]])
    if(key==6):
         Brakes=df.groupby(["Front_Brakes","Rear_Brakes"])
         st.dataframe(Brakes.head(5).iloc[:,[1,2,3]])
    if(key==7):
         mileage=df.sort_values(by="City_Mileage",ascending=False,key=lambda x: np.argsort(index_natsorted(df["City_Mileage"])))
         st.dataframe(mileage.head(5).iloc[:,[1,2,3]])
    if(key==8):
         Power_steering=df[(df["Power_Steering"]=="Yes") & (df["Power_Seats"]=="Yes")]
         st.dataframe(Power_steering.head(5).iloc[:,[1,2,3]])

#Technology
def Technology(key):
     if(key==9):
         tech_communication=df[(df["Voice_Recognition"]=="Yes") & (df["Navigation_System"]=="Yes") & (df["Bluetooth"]=="Yes") ]
         st.dataframe(tech_communication.head(5).iloc[:,[1,2,3]])
     elif(key==10):
         tech_Parking_and_controlling_assistance=df[(df["Parking_Assistance"]=="Front and rear sensors with camera") & (df["Lane_Watch_Camera/_Side_Mirror_Camera"]=="Yes")& (df["Cruise_Control"]=="Yes")&(df["Headlight_Reminder"]) ]
         st.dataframe(tech_Parking_and_controlling_assistance.head(5).iloc[:,[1,2,3]])
     elif(key==11):
          tech_seating_and_stearing=df[(df["Heated_Seats"]=="Yes" ) & (df["ISOFIX_(Child-Seat_Mount)"]=="Yes") & (df["Ventilation_System"]=="Fully automatic climate control")]
          st.dataframe(tech_seating_and_stearing.head(5).iloc[:,[1,2,3]])
     elif(key==12):
          tech_safety=df[(df["Walk_Away_Auto_Car_Lock"]=="Yes") & (df["Passenger_Side_Seat-Belt_Reminder"]=="Yes") & (df["Gear_Indicator"]=="Yes") & (df["Automatic_Headlamps"]) &(df["Android_Auto"]=="Yes")]
          st.dataframe(tech_safety.head(5).iloc[:,[1,2,3]])

def Quality():
     Quality=df.sort_values(by="Number_of_Airbags",ascending=False,key=lambda x: np.argsort(index_natsorted(df["Number_of_Airbags"]))).groupby(["Central_Locking","Airbags","Ventilation_System","Third_Row_AC_Vents","Model","Make"])
     st.dataframe(Quality.head(5).iloc[:,[1,2,3]])
Options={"saftey in Forward Collision Prevention":0,"saftey in Braking Tire Pressure and Anti Rollover":1,"saftey in Driver State Monitoring & Communication":2
    ,"saftey in Lane and Side Assisting":3,"saftey in Parking and Backing Assisting":4,
    "More engine performance":5,"Performance in Brakes":6,"Performance in Mileage":7,
    "Performance in Power steering":8,"Technology features in communication":9,"Technology features in Parking and controlling assistance":10
    ,"Technology features in seating and stearing":11,"Technology features in Safety":12," best in Quality":13,"Which types of Fuel types cars are using most":14,"Model vs Fuel Tank":15,"kerb weight vs milage":16}
def Fuel_Type():
     st.sidebar.header('Select what to display')
     fuel=df['Fuel_Type'].tolist()
     dict={"Petrol":0,"Diesel":0,'CNG + Petrol':0,'CNG':0,'Hybrid':0,'Electric':0}
     for i in fuel:
          dict[i]+=1
     countries=list(dict.keys())
     values = list(dict.values())

     fig = go.Figure(
     go.Pie(
          labels = countries,
          values = values,
          hoverinfo = "label+percent",
          textinfo = "value"
     ))
     st.header("Pie chart")
     st.plotly_chart(fig)
for i in Options:
     if add_selectbox==i and Options[i]>=0 and Options[i]<=3:
          st.write('You selected: ',i)
          Safety(Options[i])
     elif(add_selectbox==i and Options[i]>=4 and Options[i]<=8):
          st.write('You selected: ',i)
          Performance(5)
     elif(add_selectbox==i and Options[i]>=9 and Options[i]<=12):
          st.write('You selected: ',i)
          Technology(Options[i])
     elif(add_selectbox==i and Options[i]==13):
          st.write('You selected: ',i)
          Quality()
     elif(add_selectbox==i and Options[i]==14):
          st.write('You selected: ',i)
          Fuel_Type()
     elif(add_selectbox==i and Options[i]==15):
          st.write('You selected: ',i)
          modelvsFuel_tank()
     elif(add_selectbox==i and Options[i]==16):
          kerb_weight_vs_milage()


