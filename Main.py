import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
import numpy as np
import streamlit as st
import datetime
from streamlit_modal import Modal

def diabets_prdict(person_info):
    data=pd.read_csv("Source_data.csv") 
    y=data["diabetes"]
    x=data.drop("diabetes",axis=1)
    x_train,x_test,y_train,y_test = train_test_split (x,y,test_size=0.5)
    model=AdaBoostClassifier().fit(x_train,y_train)
    return model.predict(person_info)
st.set_page_config(layout="wide")
st.write("<h1 style='text-align: center; color: red;'>Diabetes Prediction</h1>", unsafe_allow_html=True)
one,two=st.columns([3,3])
with one:
    gender=st.selectbox(label="Gender",options=["Male","Female","Others"],placeholder="Choose option")
    dob=st.date_input(label="Date of Birth",format="DD-MM-YYYY",min_value=datetime.date(1947,1,1), max_value=datetime.datetime.now())
    hypertension=st.selectbox(label="Hyper tension",options=["Yes","No"])
    heart_disease=st.selectbox(label="Heart disease",options=["Yes","No"])
with two:
    smoking_history=st.selectbox(label="Smoking history",options=['Never', 'No_Info', 'Current', 'Former', 'Ever', 'Not_current'])
    mmodal=Modal(title="BMI Calculator",key="Calculator")
    bmi=st.number_input(label="BMI")
    HbA1c_level=st.number_input(label="HbA1c level",step=0.1,min_value=3.00,max_value=10.00)
    blood_glucose_level=st.number_input(label="Blood Glucose Level")
aaa,bbb,ccc=st.columns([5,3,3])
with bbb:
    check=st.button(label="Check")
modal=Modal(title="Result",key="modal")
if check:
    dict={'Never': 4, 'No_Info': 0, 'Current':1, 'Former':3, 'Ever':2, 'Not_current':5,'Yes':1,'No':0,'Female':0,'Male':1,'Others':2}
    person_data=list()
    person_data.append(dict[gender])
    age=(datetime.date.today().year)-dob.year
    person_data.append(age)
    person_data.append(dict[hypertension])
    person_data.append(dict[heart_disease])
    person_data.append(dict[smoking_history])
    person_data.append(bmi)
    person_data.append(HbA1c_level)
    person_data.append(blood_glucose_level)
    predit=np.array([person_data])
    result=diabets_prdict(predit)
    with modal.container():
        if result[0]==0:
            col,cal,cel=st.columns([1.2,1,1])
            with cal:
                st.image("happy.png")
            st.write("<p style='text-align: center; color: red; font-size:30px;'>As per data You don't have Diabetes</p>",unsafe_allow_html=True)
            st.write("<p style='text-align: center; color: red; font-size:12px;'>Disclaimer:This is not accurate please consult doctor for perfect result</p>",unsafe_allow_html=True)
        elif result[0]==1:
            col,cal,cel=st.columns([1.2,1,1])
            with cal:
                st.image("sad.png")
            st.write("<p style='text-align: center; color: red; font-size:30px;'>As per data You have Diabetes</p>",unsafe_allow_html=True)
            st.write("<p style='text-align: center; color: red; font-size:12px;'>Disclaimer:This is not accurate please consult doctor for perfect result</p>",unsafe_allow_html=True)




