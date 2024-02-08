# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu



# loading the saved models

diabetes_model = pickle.load(open('C:\\Users\\User\\Desktop\\Machine Learning\\Malady Augur\\saved models\\diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:\\Users\\User\\Desktop\\Machine Learning\Malady Augur\\saved models\\heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('C:\\Users\\User\\Desktop\\Machine Learning\\Malady Augur\\saved models\\parkinsons_model.sav', 'rb'))




# sidebar for navigation
with st.sidebar:
    
    
    selected = option_menu('Malady Augur',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction',
                           'Hospital Suggestion',
                           'Doctor Suggestion',
                           'Info & Contact No.'],
                          icons=['activity','heart','person',
                                 'hospital', 'hospital', 'phone'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)


# hospital suggestion
if (selected == "Hospital Suggestion"):
    
    st.title("Hospital Suggestion Center")
    
    col1, col2, col3 = st.columns(3)
    input_hos = []
    
      
    with col1:
        Dive_Ops = ["Dhaka", "Barishal", "Chattogram"]
        Division = st.selectbox("Select an option:", Dive_Ops, key="unique_key1")
        input_hos.append(Division)
        st.write("You selected:", Division)
        
    with col2:
        Dis_Ops = ["Dhaka", "Barishal", "Chattogram"]
        District = st.selectbox("Select an option:", Dis_Ops, key="unique_key2")
        input_hos.append(District)
        st.write("You selected:", District)
        
    with col3:
        Upazilla_Ops = ["Mirpur-10", "Shahbag", "Dhanmondi"]
        Upazilla = st.selectbox("Select an option:", Upazilla_Ops, key="unique_key3")
        input_hos.append(Upazilla)
        st.write("You selected:", Upazilla)
        
    if st.button("Suggest Hospitals"):
        
        for i in input_hos:
            if "Dhaka" in input_hos and "Dhaka" in input_hos and "Mirpur-10" in input_hos:
                hos_sugg = "Popular Diagonistic Center Limited"        
            if "Dhaka" in input_hos and "Dhaka" in input_hos and "Shahbag" in input_hos:
                hos_sugg = "BIRDEM"
            if "Dhaka" in input_hos and "Dhaka" in input_hos and "Dhanmondi" in input_hos:
                hos_sugg = "LABAID"
        st.success(hos_sugg)

# Doctor Suggestion
if (selected == "Doctor Suggestion"):
    
    st.title("Doctor Suggestion Center")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    input_hos = []
    
      
    with col1:
        Dive_Ops = ["Dhaka", "Barishal", "Chattogram"]
        Division = st.selectbox("Select an option:", Dive_Ops, key="unique_key1")
        input_hos.append(Division)
        st.write("You selected:", Division)
        
    with col2:
        Dis_Ops = ["Dhaka", "Barishal", "Chattogram"]
        District = st.selectbox("Select an option:", Dis_Ops, key="unique_key2")
        input_hos.append(District)
        st.write("You selected:", District)
        
    with col3:
        Upazilla_Ops = ["Mirpur-10", "Shahbag", "Dhanmondi"]
        Upazilla = st.selectbox("Select an option:", Upazilla_Ops, key="unique_key3")
        input_hos.append(Upazilla)
        st.write("You selected:", Upazilla)
        
    with col4:
        hos_name = ["POPULAR", "BIRDEM", "LABAID"]
        hospital = st.selectbox("Select an option:", hos_name, key="unique_key4")
        input_hos.append(hospital)
        st.write("You selected:", hospital)
        
    with col5:
        disease_name = ["Skin", "Kidney", "Neuro-surgeon"]
        disease = st.selectbox("Select an option:", disease_name, key="unique_key5")
        input_hos.append(disease)
        st.write("You selected:", disease)
        
    if st.button("Suggest Hospitals"):
        
        for i in input_hos:
            if "Dhaka" in input_hos and "Dhaka" in input_hos and "Mirpur-10" in input_hos and "POPULAR" in input_hos and "Skin" in input_hos:
                hos_sugg = "Dr. Munir Rashid"
            elif "Dhaka" in input_hos and "Dhaka" in input_hos and "Shahbag" in input_hos and "BIRDEM" in input_hos and "Kidney" in input_hos:
                hos_sugg = "Prof. Wasim M M Haque"
            elif "Dhaka" in input_hos and "Dhaka" in input_hos and "Dhanmondi" in input_hos and "LABAID" in input_hos and "Neuro-surgeon" in input_hos:
                hos_sugg = "Dr. Rezaul Amin Titu"
            else:
                hos_sugg = "Sorry! Could not find any doctor for given information."
        st.success(hos_sugg)
        
# Doctor Suggestion
if (selected == "Info & Contact No."):
    # Define a list of options for the first select box
    options1 = ["Option A", "Option B", "Option C"]
    
    # Create the first select box
    selected_option1 = st.selectbox("Select an option (Box 1)", options1)
    
    # Depending on the selection in the first select box, create the second select box
    if selected_option1 == "Option A":
        options2 = ["A-1", "A-2", "A-3"]
        selected_option2 = st.selectbox("Select an option (Box 2)", options2)
    elif selected_option1 == "Option B":
        options2 = ["B-1", "B-2", "B-3"]
        selected_option2 = st.selectbox("Select an option (Box 2)", options2)
    else:
        selected_option2 = None  # Set a default value
    
    # Display the selections
    st.write("You selected (Box 1):", selected_option1)
    if selected_option2 is not None:
        st.write("You selected (Box 2):", selected_option2)
